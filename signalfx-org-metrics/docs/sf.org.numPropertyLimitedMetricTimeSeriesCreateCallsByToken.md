---
title: sf.org.numPropertyLimitedMetricTimeSeriesCreateCallsByToken
brief: Per token number of MTS SignalFx was not able to create; exceeded dimension name maximum
metric_type: counter
---
### sf.org.numPropertyLimitedMetricTimeSeriesCreateCallsByToken

One value per token; number of metric time series (MTS) SignalFx was unable to create because you reached your maximum number of unique dimension names.

Dimension(s): `orgId, tokenId`

Data Resolution: 1 second

Note that the sum of all the values may be less than the value of `sf.org.numPropertyLimitedMetricTimeSeriesCreateCalls`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).
