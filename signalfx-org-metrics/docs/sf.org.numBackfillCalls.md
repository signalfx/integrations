---
title: sf.org.numBackfillCalls
brief: Number of calls to the backfill API
metric_type: counter
---
### sf.org.numBackfillCalls

One value per metric type, each representing the number of times a backfill API call was used to send metrics. 

Dimension(s): `category, orgId`

Data Resolution: 1 second

You can have up to three MTS for this metric; each MTS is sent with a dimension named  ``category`` with a value of Counter, Cumulative Counter, or Gauge. For more information, see [About "per metric type" metrics](../readme.md#about-per-metric-type-metrics).
