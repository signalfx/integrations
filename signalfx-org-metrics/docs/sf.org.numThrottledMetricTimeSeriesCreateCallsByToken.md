---
title: sf.org.numThrottledMetricTimeSeriesCreateCallsByToken
brief: Per token number of MTS not processed by SignalFx; exceeded per-minute or per-hour MTS creation limit
metric_type: counter
---
### sf.org.numThrottledMetricTimeSeriesCreateCallsByToken

Per token number of metric time series (MTS) SignalFx was unable to create because your organization significantly exceeded its per-minute or per-hour MTS creation limit.

Dimension(s): `orgId, tokenId`

Data Resolution: 1 second

Note that the sum of all the values may be less than the value of `sf.org.numThrottledMetricTimeSeriesCreateCalls`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).

