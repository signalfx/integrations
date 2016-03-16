---
title: Disk ops total
brief: Total number of disk read and write operations on this host. 
metric_type: cumulative_counter
---
### Disk ops total

This metric shows the total number of disk read and write operations on this host, summed across all volumes. The SignalFx metadata plugin computes this metric based on the disk operations metrics output by the `disk` plugin for collectd as follows, initially summing all metrics by host:

```
disk_ops.read + disk_ops.write
```
