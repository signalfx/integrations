---
title: sf.org.numEventTimeSeriesCreatedByToken
brief: Per token number of event time series created
metric_type: counter
---
### sf.org.numEventTimeSeriesCreatedByToken

One value per token; number of event time series (ETS) created. For MTS values, see `sf.org.numMetricTimeSeriesCreatedByToken`.

Dimension(s): `orgId, tokenId`

Data Resolution: 1 second

Note that the sum of all the values may be less than the value of `sf.org.numEventTimeSeriesCreated`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).

