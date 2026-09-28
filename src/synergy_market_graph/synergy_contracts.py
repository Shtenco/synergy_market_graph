from __future__ import annotations
from typing import Any

from .core import Edge, MarketGraph

CONTRACT_ID = "synergy.trading.fair-value/v1"
AUTHORITY = "market_graph"


def fair_value_payload(
    *,
    observation_id: str,
    src: str,
    dst: str,
    edges: list[dict[str, Any]],
    max_hops: int = 4,
) -> dict[str, Any]:
    if not observation_id.strip():
        raise ValueError("observation_id required")
    graph = MarketGraph([Edge(**edge) for edge in edges])
    value = graph.fair_value(src, dst, max_hops)
    if value is None:
        raise ValueError("no executable path for fair value")
    return {
        "observation_id": observation_id,
        "src": src.upper(),
        "dst": dst.upper(),
        "fair_value": float(value),
        "max_hops": int(max_hops),
        "authorization": False,
    }
