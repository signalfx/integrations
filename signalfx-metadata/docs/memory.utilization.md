---
title: Memory utilization
brief: Percent of memory in use on this host. 
metric_type: gauge
---
### Memory utilization

This metric shows the amount of memory in use on this machine, as a percent of total memory available. 

The SignalFx metadata plugin computes this metric based on the metrics output by the `memory` plugin for collectd and the `mem` plugin for Telegraf. The calculation used is as follows:

collectd
```
1.0 * memory.used / sum (memory.*) * 100
```

Telegraf
```
1.0 * mem.used / sum (mem.*) * 100
```