---
title: Total Query Time
brief: Total time spent in search queries (milliseconds)
metric_type: counter
---
### Total Query Time

> How much time has been spent in search queries on this node since it started.

This metric indicates the cumulative time that the node spent executing search requests since the system started. The ratio between this metric and counter.indices.search.query-total can be used as a rough indicator for how efficient your queries are. The larger the ratio, the more time each query is taking, and you should consider tuning or optimization.
