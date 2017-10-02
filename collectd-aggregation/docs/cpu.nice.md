---
title: Nice CPU time
brief: CPU time spent in userspace running 'nice'-ed processes (in jiffies)
metric_type: cumulative_counter
---
### Hardware Interrupt CPU usage

> CPU time spent in userspace running 'nice'-ed processes.

In order to get a percentage this value must be compared against the sum of all CPU states.

A sustained high value for this metric may be caused by:

* The server not having enough CPU capacity for a process
* A programming error which causes a process to use an unexpected amount of CPU
