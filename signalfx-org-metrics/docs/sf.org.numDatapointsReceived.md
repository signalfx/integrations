---
title: sf.org.numDatapointsReceived
brief: Number of datapoints SignalFx received
metric_type: counter
---
### sf.org.numDatapointsReceived

One value per metric type, each representing the number of datapoints SignalFx received and processed. 

The sum of the values represents the total number of datapoints you sent to SignalFx minus any datapoints that were not accepted due to limits exceeded.


Dimension(s): `category, orgId`

Data Resolution: 1 second

You can have up to three MTS for this metric; each MTS is sent with a dimension named  ``category`` with a value of Counter, Cumulative Counter, or Gauge. For more information, see [About "per metric type" metrics](../readme.md#about-per-metric-type-metrics).
