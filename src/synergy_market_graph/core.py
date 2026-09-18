from __future__ import annotations
from dataclasses import dataclass
from math import log,exp
from collections import defaultdict

@dataclass(frozen=True)
class Edge:
    src:str; dst:str; rate:float; fee_bps:float=0.0; capacity:float=float('inf'); slippage_bps:float=0.0; latency_ms:float=0.0; venue:str=''
    def executable_rate(self): return self.rate*(1-(self.fee_bps+self.slippage_bps)/10000.0)

class MarketGraph:
    def __init__(self,edges:list[Edge]):
        self.adj=defaultdict(list)
        for e in edges:
            if e.rate<=0: raise ValueError('rate must be positive')
            self.adj[e.src].append(e)
    def paths(self,src,dst,max_hops=4):
        out=[]
        def dfs(node,path,seen):
            if len(path)>max_hops:return
            if node==dst and path: out.append(tuple(path)); return
            for e in self.adj.get(node,[]):
                if e.dst in seen and e.dst!=dst:continue
                dfs(e.dst,path+[e],seen|{e.dst})
        dfs(src,[],{src}); return out
    def path_rate(self,path):
        r=1.0
        for e in path:r*=e.executable_rate()
        return r
    def fair_value(self,src,dst,max_hops=4):
        ps=self.paths(src,dst,max_hops)
        rs=[self.path_rate(p) for p in ps if self.path_rate(p)>0]
        if not rs:return None
        return exp(sum(log(x) for x in rs)/len(rs))
    def cycles(self,start,max_hops=4,min_edge_bps=0.0):
        found=[]
        def dfs(node,path,seen):
            if len(path)>=max_hops:return
            for e in self.adj.get(node,[]):
                if e.dst==start and path:
                    cyc=path+[e]; rate=self.path_rate(cyc); bps=(rate-1)*10000
                    if bps>=min_edge_bps:found.append((bps,tuple(cyc)))
                elif e.dst not in seen:
                    dfs(e.dst,path+[e],seen|{e.dst})
        dfs(start,[],{start})
        return sorted(found,key=lambda x:x[0],reverse=True)
