from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from .core import Edge,MarketGraph
app=FastAPI(title='SYNERGY Market Graph',version='2.0.0')
class E(BaseModel):src:str;dst:str;rate:float;fee_bps:float=0;capacity:float=1e18;slippage_bps:float=0;latency_ms:float=0;venue:str=''
class FairReq(BaseModel):src:str;dst:str;edges:list[E];max_hops:int=4
@app.get('/health')
def health():return {'ok':True,'service':'market-graph'}
@app.post('/v1/fair-value')
def fair(req:FairReq):return {'fair_value':MarketGraph([Edge(**e.model_dump()) for e in req.edges]).fair_value(req.src,req.dst,req.max_hops)}

# Enterprise v2 control/data plane
from .enterprise.service import EnterpriseRuntime, build_enterprise_router, install_observability
from .enterprise.product import build_product_router
enterprise_runtime=EnterpriseRuntime.from_env(service_name='synergy-market-graph')
install_observability(app,enterprise_runtime)
app.include_router(build_enterprise_router(enterprise_runtime))
app.include_router(build_product_router(enterprise_runtime))

if __name__=='__main__':uvicorn.run(app,host='0.0.0.0',port=8000)
