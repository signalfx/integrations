
---
title: cpu.wait
brief: Amount of total CPU time spent idle while waiting for an I/O operation to complete.
metric_type: cumulative
custom: true
---
### cpu.wait

Amount of total CPU time spent idle while waiting for an I/O operation to complete. In order to get a percentage this value must be compared against the sum of all CPU states. A high value for a sustained period may be caused by: 1) A slow hardware device that is taking too long to service requests, or 2) Too many requests being sent to an I/O device

