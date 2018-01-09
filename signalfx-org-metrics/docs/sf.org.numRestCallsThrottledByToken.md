---
title:  sf.org.numRestCallsThrottledByToken
brief: Per token number of REST calls not accepted by SignalFx; exceeded per-minute limit
metric_type: counter
---
###  sf.org.numRestCallsThrottledByToken

One value per token; number of REST calls you made to the SignalFx API that were not accepted by SignalFx, because your organization significantly exceeded its per-minute limit.

Dimension(s): `orgId, tokenId`

Data Resolution: 1 second

Note that the sum of all the values may be less than the value of `sf.org.numRestCallsThrottled`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).
