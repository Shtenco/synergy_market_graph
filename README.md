# SYNERGY Market Graph

> **Graph fair value, executable-cycle discovery and causal/relative-value market representation**

**Enterprise v2.0.0** · Python 3.11+ · FastAPI/OpenAPI · Docker/Compose · RBAC/JWT · PostgreSQL/ClickHouse audit

**Designed for:** Market makers, FX/crypto quant desks, exchanges and liquidity providers  
**Primary endpoint:** `POST /enterprise/v1/graph/analyze`

> [!IMPORTANT]
> Graph-derived fair value/cycles are research evidence. They do not guarantee executable arbitrage, fills or profit.

## Institutional package
Deterministic graph core · tenant RBAC · request-ID audit · health/metrics · Docker/Compose · demo/load harnesses · customer pilot documentation.

## Verification
**20 tests passed** · health smoke **80/80 200** · local p95 **87.7 ms** (~526 req/s). Health smoke only.

## Quick start
```bash
pip install -e '.[dev,enterprise]'
pytest -q
python -m synergy_market_graph.api
```

## CTO package
[Due diligence](docs/CTO_DUE_DILIGENCE.md) · [Architecture](docs/ARCHITECTURE_DIAGRAMS.md) · [API](docs/API_EXAMPLES.md) · [Security](SECURITY.md) · [Benchmarks](docs/BENCHMARKS_AND_ACCEPTANCE.md) · [SLA/SLO](docs/SLA_SLO.md) · [Deployment](docs/DEPLOYMENT_CHECKLIST.md) · [Pilot](docs/CUSTOMER_PILOT.md)
