---
title: sf.org.numDatapointsReceived
brief: Number of 
metric_type: counter
---
### sf.org.numDatapointsReceived

One value per metric type, each representing the number of datapoints SignalFx received and processed. 

The sum of the values represents the total number of datapoints you sent to SignalFx minus any datapoints that were not accepted (i.e. `sf.org.numDatapointsDroppedExceededQuota`, `sf.org.numDatapointsDroppedThrottle`).


**NOTE FOR REVIEWERS: Confirm rewrite is OK to replace this original text: One value per metric type, each representing the number of datapoints SignalFx received after all throttling and filtering is done.**


Dimension(s): `category, orgId`

Data Resolution: 1 second

You can have up to three MTS for this metric; each MTS is sent with a dimension named  ``category`` with a value of Counter, Cumulative Counter, or Gauge. For more information, see [About "per metric type" metrics](../readme.md#about-per-metric-type-metrics).
