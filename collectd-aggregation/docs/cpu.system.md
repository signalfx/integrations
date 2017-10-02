---
title: System CPU time
brief: CPU time spent running in the kernel (in jiffies)
metric_type: cumulative_counter
---
### System CPU time

> CPU time spent running in the kernel

This value reflects how often processes are calling into the kernel for services (e.g to log to the console).

In order to get a percentage this value must be compared against the sum of all CPU states.

A sustained high value for this metric may be caused by:

* A process that needs to be re-written to use kernel resources more efficiently
* A userspace driver that is broken
