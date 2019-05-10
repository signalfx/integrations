
---
title: cpu.softirq
brief: CPU time spent while servicing software interrupts -- unlike a hardware interrupt, a software interrupt happens at the sofware layer. Usually it is a userspace program requesting a service of the kernel. This metric measures how many jiffies were spent by the CPU handling these interrupts. In order to get a percentage this value must be compared against the sum of all CPU states. A sustained high value for this metric may be caused by a programming error which causes a process to unexpectedly request too many services from the kernel.

metric_type: cumulative
custom: true
---
### cpu.softirq

CPU time spent while servicing software interrupts -- unlike a hardware interrupt, a software interrupt happens at the sofware layer. Usually it is a userspace program requesting a service of the kernel. This metric measures how many jiffies were spent by the CPU handling these interrupts. In order to get a percentage this value must be compared against the sum of all CPU states. A sustained high value for this metric may be caused by a programming error which causes a process to unexpectedly request too many services from the kernel.

