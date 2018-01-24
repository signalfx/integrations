---
title: sf.org.numDatapointsDroppedThrottle
brief: Number of datapoints not processed by SignalFx; exceeded DPM limit
metric_type: counter
---
### sf.org.numDatapointsDroppedThrottle

Total number of datapoints you sent to SignalFx but that SignalFx didn't accept, because your organization significantly exceeded its DPM limit.

Note that unlike `sf.org.numDatapointsDroppedExceededQuota`, this metric represents datapoints for both existing and new MTS. In other words, if your organization is being throttled, SignalFx is not accepting any data at all. Contact [support](https://support.signalfx.com/hc/en-us/requests/new) to determine how to rectify this issue.

Dimension(s): `orgId`

Data Resolution: 1 second
