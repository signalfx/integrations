---
title: CPU Usage Total
brief: Jiffies of CPU time used by the container
metric_type: cumulative_counter
---
### CPU Usage Total

Tracks how much CPU time, in jiffies, a container has used. To get a CPU
utilization percentage, compute against
[`cpu.usage.system`](cpu.usage.system.md):

```
CPU usage % = 100 * cpu.usage.total / cpu.usage.system
```
