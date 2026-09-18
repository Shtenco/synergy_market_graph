from __future__ import annotations
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ..core import Edge, MarketGraph
from .models import Principal, Role
from .service import EnterpriseRuntime, principal_dependency, request_id_header

class EdgeModel(BaseModel):
    src:str; dst:str; rate:float; fee_bps:float=0; capacity:float=1e18; slippage_bps:float=0; latency_ms:float=0; venue:str=""
class AnalyzeRequest(BaseModel): src:str; dst:str; edges:list[EdgeModel]; max_hops:int=4; min_cycle_bps:float=0.0

def build_product_router(runtime:EnterpriseRuntime)->APIRouter:
    router=APIRouter(prefix="/enterprise/v1/graph",tags=["enterprise-market-graph"])
    @router.post("/analyze")
    async def analyze(req:AnalyzeRequest, principal:Principal=Depends(principal_dependency(runtime,{Role.RESEARCHER,Role.TRADER})), request_id:str=Depends(request_id_header)):
        g=MarketGraph([Edge(**e.model_dump()) for e in req.edges]);fair=g.fair_value(req.src,req.dst,req.max_hops)
        raw=g.cycles(req.src,req.max_hops,req.min_cycle_bps)[:20]
        cycles=[{"edge_bps":bps,"path":[f"{e.src}->{e.dst}@{e.venue or 'na'}" for e in path]} for bps,path in raw]
        runtime.record(principal,action="market_graph.analyze",request_id=request_id,payload={"src":req.src,"dst":req.dst,"paths":len(g.paths(req.src,req.dst,req.max_hops)),"cycles":len(cycles)})
        return {"request_id":request_id,"fair_value":fair,"cycles":cycles}
    return router
