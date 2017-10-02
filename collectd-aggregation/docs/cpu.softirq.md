---
title: Software Interrupt CPU time
brief: CPU time spent servicing software interrupts (in jiffies)
metric_type: cumulative_counter
---
### Software Interrupt CPU time

> CPU time spent while servicing software interrupts

Unlike a hardware interrupt, a software interrupt happens at the sofware layer. Usually it is a userspace program requesting a service of the kernel. This metric measures how many jiffies were spent by the CPU handling these interrupts.

In order to get a percentage this value must be compared against the sum of all CPU states.

A sustained high value for this metric may be caused by:

* A programming error which causes a process to unexpectedly request too many services from the kernel.
