---
title: sf.org.numEventsIngested
brief: Number of custom events received via the API
metric_type: counter
---
### sf.org.numEventsIngested

Number of custom events received by SignalFx through the /event POST API.
     
Dimension(s): `orgId` **NOTE TO REVIEWERS: These also have a category dimension, which apparently is a bug/artifact to be ignored. Values for category I have seen include ALERT, AUDIT, and COLLECTD.This means there could be multiple values when there should only be one, and they need to be summed like metrics with "real" categories, etc. How should I explain this?**

Data Resolution: 1 second

