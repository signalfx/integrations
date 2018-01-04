---
title:sf.org.numMetricTimeSeriesCreatedByToken
brief: Per token number of MTS created
metric_type: counter
---
### sf.org.numMetricTimeSeriesCreatedByToken


Dimension(s): `category, orgId, tokenId`

Data Resolution: 5 seconds

One value per metric type per token, each representing the number of metric time series (MTS) created of that type. 


You can have up to three MTS associated with each token; each MTS is sent with a dimension named  ``category`` with a value of Counter, Cumulative Counter, or Gauge. For more information, see [About "per metric type" metrics](../readme.md#about-per-metric-type-metrics).

Note that the sum of all the values may be less than the value of `sf.org.numMetricTimeSeriesCreated`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).
