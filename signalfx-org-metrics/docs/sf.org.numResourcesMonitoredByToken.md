---
title: sf.org.numResourcesMonitoredByToken
brief: Per token number of host-based resources monitored
metric_type: counter
---
### sf.org.numResourcesMonitoredByToken

One value per token; number of hosts or containers that are being monitored. This metric will not be created until a host or container actually starts sending a host or container metric.

The `resourceType` dimension indicates whether the value represents hosts or containers.

Dimension(s): `orgId, resourceType, tokenId`

Data Resolution: 10 minutes

Note that the sum of all the values may be less than the value of `sf.org.numResourcesMonitored`. For an explanation, see [About ByToken metrics](../readme.md#about-bytoken-metrics).

