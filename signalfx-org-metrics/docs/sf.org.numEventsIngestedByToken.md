---
title: sf.org.numEventsIngestedByToken
brief: Per token number of custom events received via the /event POST API
metric_type: counter
---
### sf.org.numEventsIngestedByToken

One value per token; number of custom events received by SignalFx through the /event POST API 

Dimension(s): `orgId, tokenId, category`

Data Resolution: 1 second

Note that the sum of all the values may be less than the value of `sf.org.numEventsIngested`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).

