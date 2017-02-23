---
title: CPU utilization
brief: Percent of CPU used on this host.
metric_type: gauge
---
### CPU utilization

This metric shows the amount of CPU in use on this machine, as a percent of total CPU available. 

The SignalFx metadata plugin computes this metric based on the CPU metrics output by the `aggregation` plugin for collectd or the `cpu` plugin for Telegraf. First, compute the ratio of `cpu.idle` to the sum of all CPU metrics. Next, subtract that number from 1 to yield the ratio of CPU that is not idle, and multiply by 100 to display as percent, as follows: 

```
[1 - cpu.idle / sum(cpu.*)] * 100
```