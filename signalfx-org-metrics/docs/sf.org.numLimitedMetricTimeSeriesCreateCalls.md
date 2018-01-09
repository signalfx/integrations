---
title: sf.org.numLimitedMetricTimeSeriesCreateCalls
brief: Number of MTS not sent; over maximum allowed
metric_type: counter
---
### sf.org.numLimitedMetricTimeSeriesCreateCalls

One value per metric type, each representing the number of metric time series (MTS) not sent to SignalFx because you've reached your maximum active MTS allowed.

Dimension(s): `category, orgId`

Data Resolution: 1 second

You can have up to three MTS for this metric; each MTS is sent with a dimension named  ``category`` with a value of Counter, Cumulative Counter, or Gauge. For more information, see [About "per metric type" metrics](../readme.md#about-per-metric-type-metrics).
