---
title: sf.org.numLimitedMetricTimeSeriesCreateCallsByToken
brief: Per token of MTS not sent; over maximum allowed
metric_type: counter
---
### sf.org.numLimitedMetricTimeSeriesCreateCallsByToken

One value per metric type per token, each representing the number of metric time series (MTS) not sent to SignalFx because you've reached your maximum active MTS allowed.

Dimension(s): `category, orgId, tokenId`

Data Resolution: 1 second

You can have up to three MTS associated with each token; each MTS is sent with a dimension named  ``category`` with a value of Counter, Cumulative Counter, or Gauge. For more information, see [About "per metric type" metrics](../readme.md#about-per-metric-type-metrics).

Note that the sum of all the values may be less than the value of `sf.org.numLimitedMetricTimeSeriesCreateCalls`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).
