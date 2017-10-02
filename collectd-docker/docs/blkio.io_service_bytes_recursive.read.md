---
title: Read volume from block devices
brief: Volume, in bytes, of reads from block devices
metric_type: cumulative_counter
---
### Read volume from block devices

Tracks the volume, in bytes, read from block devices by that container.

This metric is reported with dimensions `device_major` and `device_minor` to indicate the major and minor device numbers respectively.
