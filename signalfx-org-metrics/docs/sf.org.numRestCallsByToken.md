---
title: sf.org.numRestCallsByToken
brief: Per token number of REST calls made to the SignalFx API
metric_type: counter
---
###  sf.org.numRestCallsByToken

One value per token; number of REST calls made to the SignalFx API. 

Dimension(s): `orgId, tokenId`

Data Resolution: 1 second

Note that the sum of all the values may be less than the value of `sf.org.numRestCalls`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).

