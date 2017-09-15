---
title: Write volume to block devices
brief: Volume, in bytes, of writes to block devices
metric_type: cumulative_counter
---
### Write volume to block devices

Tracks the volume, in bytes, written to block devices by that container.

This metric is reported with dimensions `device_major` and `device_minor` to indicate the major and minor device numbers respectively.
