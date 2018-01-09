---
title: sf.org.numLimitedEventTimeSeriesCreateCallsByToken
brief: Per token number of event time series over maximum ETS allowed
metric_type: counter
---
### sf.org.numLimitedEventTimeSeriesCreateCallsByToken

One value per token, each representing the number of event time series (ETS) SignalFx was unable to create, because you have exceeded the maximum number of ETS allowed. 

Dimension(s): `category, orgId, tokenId`

Data Resolution: 1 second

Note that the sum of all the values may be less than the value of `sf.org.numLimitedEventTimeSeriesCreateCalls`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).
