---
title: Disk utilization
brief: Percent of disk used on this volume. 
metric_type: gauge
---
### Disk utilization

This metric shows the amount of disk space in use on this volume, as a percentage of total disk space available on the volume. 

The SignalFx metadata plugin computes this metric based on the disk space metrics output by the `df` plugin for collectd, as follows:

collectd
```
100 * [df_complex.used / (df_complex.free + df_complex.used)] 
```

On Telegraf, the SignalFx metadata plugin reports `disk.utilization` with the value of the `disk` plugin's `used_percent` metric.
