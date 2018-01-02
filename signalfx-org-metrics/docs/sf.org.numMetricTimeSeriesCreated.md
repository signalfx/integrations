---
title: sf.org.numMetricTimeSeriesCreated
brief: Number of time series created
metric_type: counter
---
### sf.org.numMetricTimeSeriesCreated


Dimension(s): `category, orgId`

Data Resolution: 15 seconds **REVIEWER: Correct? Or 1 second, like all the others?**

One value per metric type, each representing the number of time series created of that type. 

You can have up to three MTS for this metric; each MTS is sent with a dimension named  ``category`` with a value of Counter, Cumulative Counter, or Gauge. For more information, see [About "per metric type" metrics](../readme.md#about-per-metric-type-metrics).
