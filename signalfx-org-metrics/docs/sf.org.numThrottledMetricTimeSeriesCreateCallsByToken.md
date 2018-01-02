---
title: sf.org.numThrottledMetricTimeSeriesCreateCallsByToken
brief: Per token number of MTS not processed by SignalFx
metric_type: counter
---
### sf.org.numThrottledMetricTimeSeriesCreateCallsByToken

Per token number of metric time series (MTS) you sent to SignalFx but that SignalFx didn't accept, because your organization significantly exceeded its per-minute or per-hour MTS creation limit.

Dimension(s): `orgId, tokenId`

Data Resolution: 1 second

Note that the sum of all the values may be less than the value of `sf.org.numThrottledMetricTimeSeriesCreateCalls`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).

