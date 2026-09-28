from synergy_market_graph.synergy_contracts import CONTRACT_ID, fair_value_payload

def test_fair_value_payload_is_advisory():
    p=fair_value_payload(
        observation_id="obs-1",src="EUR",dst="USD",
        edges=[{"src":"EUR","dst":"USD","rate":1.1,"fee_bps":1.0}]
    )
    assert CONTRACT_ID=="synergy.trading.fair-value/v1"
    assert p["src"]=="EUR" and p["dst"]=="USD"
    assert p["fair_value"]>0
    assert p["authorization"] is False
