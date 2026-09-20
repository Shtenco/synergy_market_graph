# Market Graph V3 Final Product Design

**Version:** 3.0.0  
**Branch:** `production/v3.0.0`  
**Status:** architecture specification for human review  
**Master:** `synergy-midas-institutional/docs/superpowers/specs/2026-09-21-final-product-line-3.0-master.md`

## Goal
Convert Market Graph from a stateless `edges[] -> fair_value/cycles` endpoint into a persistent market-graph intelligence product with immutable snapshots, provenance, freshness, and reproducible analysis artifacts.

## Current gap
Today the full graph is supplied by the caller on each request. The service owns neither the graph snapshot nor edge provenance/freshness, so a result cannot be reproduced later from an authoritative snapshot.

## Durable resources
- MarketUniverse
- Venue
- Instrument
- DataSource
- GraphSnapshot
- EdgeSnapshot
- GraphAnalysisArtifact

## Core invariants
1. A GraphAnalysisArtifact always references one immutable GraphSnapshot.
2. Every edge stores source, observed_at, freshness TTL, capacity, fees, slippage, latency and venue.
3. Stale snapshots are rejected or explicitly analyzed with `allow_stale=true`; stale state is visible in the artifact.
4. Snapshot ingestion is idempotent by tenant + canonical graph hash.
5. Cross-tenant snapshot/analysis access is forbidden.
6. Arithmetic cycles are never labeled guaranteed executable profit.

## V3 API
- `POST /enterprise/v3/graph-snapshots`
- `GET /enterprise/v3/graph-snapshots/{id}`
- `POST /enterprise/v3/graph-analyses`
- `GET /enterprise/v3/graph-analyses/{id}`
- `GET /enterprise/v3/graph-analyses?universe_id=...`

## Persistence
PostgreSQL tables:
- market_universes
- venues
- instruments
- data_sources
- graph_snapshots
- graph_edges
- graph_analysis_artifacts
- idempotency_keys
- audit_events

## Analysis artifact
Stores:
- analysis_id
- tenant_id
- snapshot_id
- src/dst/max_hops/min_cycle_bps
- snapshot freshness status
- fair value
- selected path summaries
- cycle summaries
- code version
- created_at
- request_id

## Input safety
Reject non-finite rates/fees/slippage/latency/capacity; non-positive rates; duplicate malformed instrument IDs; invalid timestamps; negative TTL; impossible capacities.

## Common production contract
Must implement master V3 AuthVerifier/JWKS, /live, /ready, PostgreSQL pool/migrations, runtime idempotency, JSON logs, Prometheus, trace propagation, audit, tenant isolation and security/deployment requirements.

## Acceptance gates
- snapshot survives restart;
- same snapshot id reproduces same analysis under same code version;
- stale snapshot behavior is explicit and tested;
- edge provenance is queryable;
- same idempotency key/different snapshot request -> 409;
- DB outage -> readiness 503;
- cross-tenant lookup fails;
- V2 tests remain green.
