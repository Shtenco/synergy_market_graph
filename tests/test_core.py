from synergy_market_graph.core import *

def test_fair_value():
    g=MarketGraph([Edge('A','B',2),Edge('A','C',4),Edge('C','B',.5)])
    assert abs(g.fair_value('A','B')-2)<1e-12

def test_profitable_cycle():
    g=MarketGraph([Edge('USD','EUR',.9),Edge('EUR','JPY',160),Edge('JPY','USD',.0071)])
    assert g.cycles('USD',4,1)
