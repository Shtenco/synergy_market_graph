import json
from fastapi.testclient import TestClient
from synergy_market_graph.api import app
from synergy_market_graph.enterprise.auth import sign_token
from synergy_market_graph.enterprise.models import Role

SECRET="dev-only-change-me-not-for-production"

def token(role):
    return sign_token(SECRET,subject="fund-user",roles=[Role(role)],tenant_id="fund-a",ttl_seconds=3600)

def test_product_enterprise_endpoint_and_audit_linkage():
    c=TestClient(app)
    request_id="acceptance-123"
    res=c.post('/enterprise/v1/graph/analyze',json={'src': 'USD', 'dst': 'EUR', 'edges': [{'src': 'USD', 'dst': 'EUR', 'rate': 0.92, 'fee_bps': 1}, {'src': 'USD', 'dst': 'GBP', 'rate': 0.78, 'fee_bps': 1}, {'src': 'GBP', 'dst': 'EUR', 'rate': 1.18, 'fee_bps': 1}, {'src': 'EUR', 'dst': 'USD', 'rate': 1.0875, 'fee_bps': 1}], 'max_hops': 3},headers={"Authorization":"Bearer "+token('researcher'),"X-Request-ID":request_id})
    assert res.status_code==200, res.text
    body=res.json()
    for key in ['fair_value', 'cycles', 'request_id']: assert key in body
    assert body["request_id"]==request_id
    admin=token("admin")
    audit=c.get('/enterprise/audit',headers={"Authorization":"Bearer "+admin})
    assert audit.status_code==200
    assert any(e["request_id"]==request_id for e in audit.json())

def test_product_endpoint_requires_authorized_role():
    c=TestClient(app)
    res=c.post('/enterprise/v1/graph/analyze',json={'src': 'USD', 'dst': 'EUR', 'edges': [{'src': 'USD', 'dst': 'EUR', 'rate': 0.92, 'fee_bps': 1}, {'src': 'USD', 'dst': 'GBP', 'rate': 0.78, 'fee_bps': 1}, {'src': 'GBP', 'dst': 'EUR', 'rate': 1.18, 'fee_bps': 1}, {'src': 'EUR', 'dst': 'USD', 'rate': 1.0875, 'fee_bps': 1}], 'max_hops': 3},headers={"Authorization":"Bearer "+token("viewer")})
    assert res.status_code==403

def test_api_exposes_enterprise_control_routes():
    paths={r.path for r in app.routes}
    assert '/enterprise/health' in paths
    assert '/enterprise/v1/graph/analyze' in paths
