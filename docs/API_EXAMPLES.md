# API examples — SYNERGY Market Graph

`POST /enterprise/v1/graph/analyze` — roles **researcher, trader**.

```json
{"src":"USD","dst":"EUR","edges":[{"src":"USD","dst":"EUR","rate":0.92,"fee_bps":1},{"src":"USD","dst":"GBP","rate":0.78,"fee_bps":1},{"src":"GBP","dst":"EUR","rate":1.18,"fee_bps":1}],"max_hops":3}
```

```bash
curl -X POST http://127.0.0.1:8000/enterprise/v1/graph/analyze -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -H "X-Request-ID: pilot-001" -d @request.json
```

Expected fields: `fair_value`, `cycles`, `request_id`. Canonical schema: `/docs`.