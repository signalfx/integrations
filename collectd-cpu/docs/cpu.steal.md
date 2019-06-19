
---
title: cpu.steal
brief: CPU time spent waiting for a hypervisor to service requests from other virtual machines
metric_type: cumulative
custom: true
---
### cpu.steal

CPU time spent waiting for a hypervisor to service requests from other virtual machines. This metric is only present on virtual machines. This metric records how much time this virtual machine had to wait to have the hypervisor kernel service a request. In order to get a percentage this value must be compared against the sum of all CPU states. A sustained high value for this metric may be caused by: 1) Another VM on the same hypervisor using too many resources, or 2) An underpowered hypervisor

