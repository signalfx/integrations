---
title: Total block I/O volume
brief: Total volume, in bytes, of all block I/O
metric_type: cumulative_counter
---
### Total block I/O volume

Tracks the total volume, in bytes, of all serviced block I/O requests in
that container.

This metric is reported with dimensions `device_major` and `device_minor` to indicate the major and minor device numbers respectively.
