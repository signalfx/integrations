---
title: sf.org.numThrottledEventTimeSeriesCreateCallsByToken
brief: Per token number of events not processed by SignalFx; exceeded per-minute event creation limit
metric_type: counter
---
### sf.org.numThrottledEventTimeSeriesCreateCallsByToken

One value per token; number of event time series (ETS) SignalFx was unable to create because you significantly exceeded your per-minute event creation limit.

Dimension(s): `orgId, tokenId`

Data Resolution: 1 second

Note that the sum of all the values may be less than the value of `sf.org.numThrottledEventTimeSeriesCreateCalls`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).

