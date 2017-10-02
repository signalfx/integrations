---
title: Asynchronous block I/O volume
brief: Volume, in bytes, of asynchronous block I/O
metric_type: cumulative_counter
---
### Asynchronous block I/O volume

Tracks the volume, in bytes, of serviced asynchronous block I/O requests
in that container.

This metric is reported with dimensions `device_major` and `device_minor` to indicate the major and minor device numbers respectively.
