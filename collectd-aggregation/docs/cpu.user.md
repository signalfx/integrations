---
title: User CPU time
brief: CPU time spent running in userspace (in jiffies)
metric_type: cumulative_counter
---
### User CPU time

> CPU time spent running in userspace

In order to get a percentage this value must be compared against the sum of all CPU states.

If this value is high:

* A process requires more CPU to run than is available on the server
* There is an application programming error which is causing the CPU to be used unexpectedly
