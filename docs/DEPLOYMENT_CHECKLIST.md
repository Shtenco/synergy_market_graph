# Deployment checklist — SYNERGY Market Graph

- [ ] Pin commit/image and rerun tests.
- [ ] Integrate customer TLS + OIDC/mTLS/JWKS.
- [ ] Restrict DB and market-data network paths.
- [ ] Validate graph edge semantics: fees, slippage, capacity, latency, venue.
- [ ] Exercise `/enterprise/v1/graph/analyze` on representative graph sizes.
- [ ] Trace request ID to audit store.
- [ ] Drill DB outage, restart, timeout and large-payload rejection.
- [ ] Keep execution outside this research endpoint unless separately approved.