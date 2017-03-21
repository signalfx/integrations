---
title: CPU utilization per core
brief: Percent of CPU used on each core.
metric_type: gauge
---
### CPU utilization per core

This metric shows the amount of CPU in use on each core, as a percent of total CPU available per core. 

The SignalFx metadata plugin computes this metric based on the CPU metrics output by the `cpu` plugin for collectd and Telegraf. First, compute the ratio of `cpu.idle` to the sum of all CPU metrics. Next, subtract that number from 1 to yield the ratio of CPU that is not idle, and multiply by 100 to display as percent, as follows: 

```
[1 - cpu.idle / sum(cpu.*)] * 100
```
