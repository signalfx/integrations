---
title: sf.org.numDatapointsReceivedByToken
brief: Per token number of datapoints SignalFx received
metric_type: counter
---
### sf.org.numDatapointsReceivedByToken

One value per metric type per token, each representing the number of datapoints SignalFx received and processed. 

The sum of the values for a token represents the total number of datapoints you sent to SignalFx minus any datapoints that were not accepted due to limits exceeded.


Dimension(s): `category, orgId, tokenId`

Data Resolution: 1 second

You can have up to three MTS per token for this metric; each MTS is sent with a dimension named  ``category`` with a value of Counter, Cumulative Counter, or Gauge. For more information, see [About "per metric type" metrics](../readme.md#about-per-metric-type-metrics).

Note that the sum of all the values may be less than the value of `sf.org.numDatapointsReceived`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).
