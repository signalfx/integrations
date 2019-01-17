---
title: sf.org.numEventsDroppedThrottleByToken
brief: Per token number of events over per-minute limit 
metric_type: counter
---
### sf.org.numEventsDroppedThrottleByToken

One value per token; number of custom events you sent to SignalFx but that SignalFx didn't accept, because your organization significantly exceeded its per-minute limit.

Dimension(s): `orgId, tokenId`

Data Resolution: 1 second

Note that the sum of all the values may be less than the value of `sf.org.numEventsDroppedThrottle`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).
