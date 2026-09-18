# Architecture — SYNERGY Market Graph

```mermaid
flowchart LR
A[Market edges]-->B[RBAC API]
B-->C[Graph Core]
C-->D[Fair value]
C-->E[Bounded cycles]
D-->F[Audit + request ID]
E-->F
F-->G[(PostgreSQL)]
F-->H[(ClickHouse)]
```

Primary endpoint: `/enterprise/v1/graph/analyze`. Cycle discovery remains research evidence until executable constraints, settlement and venue state are independently verified.