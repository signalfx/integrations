---
title: Per-core CPU usage
brief: Jiffies of CPU time spent by the container, per CPU core
metric_type: cumulative_counter
---
### Per-core CPU usage

Superseded by `cpu.percpu.usage`.

How much CPU time is spent by the container, per CPU core. This metric is reported for each core as `cpu.percpu.usage.cpuX` where _X_ is the number of the core. For example, a two-core machine would have `cpu.percpu.usage.cpu0` and `cpu.percpu.usage.cpu1`.
