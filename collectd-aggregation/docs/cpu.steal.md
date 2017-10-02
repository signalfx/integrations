---
title: Steal CPU time
brief: CPU time spent by a hypervisor handling requests in other virtual machines (in jiffies)
metric_type: cumulative_counter
---
### Steal CPU usage

> CPU time spent waiting for a hypervisor to service requests from other virtual machines

This metric is only present on virtual machines. This metric records how much time this virtual machine had to wait to have the hypervisor kernel service a request.

In order to get a percentage this value must be compared against the sum of all CPU states.

A sustained high value for this metric may be caused by:

* Another VM on the same hypervisor using too many resources
* An underpowered hypervisor
