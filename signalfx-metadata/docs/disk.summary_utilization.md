---
title: Disk utilization summary
brief: Percent of disk space utilized on all volumes on this host. 
metric_type: gauge
---
### Disk utilization summary

This metric shows the percent of disk space utilized on this host, aggregated across all volumes. 

The SignalFx metadata plugin computes this metric based on the disk space metrics output by the `df` plugin for collectd and the `disk` plugin for Telegraf as follows, initially summing all metrics by host: 

collectd
```
100 * [df_complex.used / (df_complex.free + df_complex.used)] 
```

Telegraf
```
100 * disk.used / disk.total
```