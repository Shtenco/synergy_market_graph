# MARKET GRAPH / EXECUTABLE LIQUIDITY

## Научная задача и собственный исследовательский вклад

Directed conversion routes / capacity / latency. Edge includes src/dst, rate, fee_bps, capacity, slippage_bps, latency_ms and venue. MarketGraph enumerates paths, multiplies net conversion rates, computes a geometric mean across candidate paths and finds cycles. The fair value is a path-ensemble heuristic, not executable quote for a given amount.

## Фактический вычислительный механизм

Executable edge rate = raw_rate*(1-(fee_bps+slippage_bps)/10000); path rate = product(edge_rate). Reported fair value = exp(mean(log(path_rate))). Cycle bps = (path_rate-1)*10000. Finite liquidity capacity is stored but not yet enforced in the path arithmetic.

## Почему этот компонент важен для единой федерации

Это отдельный специализированный компонент — источник ограниченного, объяснимого исследования или решения. Его выводы можно передавать по типизированному контракту, не делая саму модель хозяином клиентских средств или бухгалтерского результата.

## Программа воспроизводимого эксперимента

Compare top executable path to the geometric-mean heuristic, include quote age and shared edge capacities, test no-arbitrage synthetic books and arbitrary input size, then add partial fills and external execution costs.

## Экспериментальный протокол и измеримые результаты

Зафиксировать исходный commit, датированные входы и их SHA-256, строгий baseline, независимую валидационную и тестовую выборки, граничные случаи, стоимость вычисления и неблагоприятные сценарии. Сравнивать на одном времени и идентичном объёме ресурсов. Публиковать не только mean score, но и распределение ошибок, устойчивость, отказные сценарии и экономические издержки. Наличие исполняемых тестов и enterprise API не доказывает реальную финансовую эффективность или production deployment.

## Подтверждающие исходники

- [`src/synergy_market_graph/core.py`](../src/synergy_market_graph/core.py)
- [`src/synergy_market_graph/synergy_contracts.py`](../src/synergy_market_graph/synergy_contracts.py)
- [`tests/`](../tests/)

## Критерий следующей версии

Перейти от предметного реализованного ядра к эксперименту с отдельным воспроизводимым manifest, автоматической CI-проверкой и фактическими доказательствами из конечной интеграции. Прежняя корневая документация сохранена полностью.
