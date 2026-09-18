# Benchmarks and acceptance — SYNERGY Market Graph

**20 tests passed**. Local health smoke: **80/80 HTTP 200**, p50 **13.1 ms**, p95 **87.7 ms**, p99 **105.8 ms**, ~**526 req/s** at 80 requests/concurrency 16.

Health smoke only. It does not measure graph size scaling, venue latency, settlement risk or executable PnL. Customer acceptance must freeze graph size/hop limits, cost/slippage fields, capacity semantics and cycle-validation rules before evaluation.