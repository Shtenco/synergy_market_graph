# SYNERGY Market Graph

**Graph fair-value, executable-cycle discovery and causal/relative-value market representation**

Version: `2.0.0` · Python 3.11+ · REST API · Docker · CI · automated tests

## Why this exists
Fragmented markets create relative-value, routing and risk relationships that are hard to model pair-by-pair.

## Commercial buyer
Market makers, FX/crypto quant desks, exchanges and liquidity providers.

## Core guarantee
The software guarantees deterministic interface behavior covered by tests. **It does not guarantee trading profit.** Live-market deployment requires customer-specific OOS validation, fees/spread/slippage/latency/capacity modelling, security review and legal/compliance approval.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest -q
python -m synergy_market_graph.api
```

Then open `http://localhost:8000/docs`.

## Commercial package
- standalone installable Python package;
- versioned FastAPI boundary;
- deterministic reference core;
- Dockerfile and GitHub Actions CI;
- sales one-pager, security boundary, deployment notes and provenance;
- proprietary evaluation licence ready for a paid pilot.

## Research lineage
Shtenco/algotrading_graph_system + Shtenco/synergy_graph_print_money + MQL5 28-pair graph / causal graph research

See `docs/PRODUCT_STATUS.md`, `docs/SALES_ONE_PAGER.md`, `docs/SECURITY.md` and `docs/PROVENANCE.md`.

## Enterprise v2.0.0

The repository now includes a separate enterprise boundary around the product core:

- JWT/RBAC roles (`viewer`, `researcher`, `trader`, `risk`, `operator`, `admin`);
- request-id propagation and auditable product actions;
- PostgreSQL and ClickHouse audit stores;
- Bybit V5, CCXT multi-CEX and MetaTrader 5 adapters with live execution disabled by default;
- retry/circuit breaker controls;
- health and Prometheus-compatible metrics;
- Docker Compose deployment reference;
- deterministic synthetic customer dataset and HTTP/k6 load harnesses.

See `docs/ENTERPRISE_ARCHITECTURE.md`, `docs/ENTERPRISE_DEPLOYMENT.md` and `docs/CUSTOMER_ACCEPTANCE.md` before any customer deployment.
