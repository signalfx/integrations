---
title: I/O Wait CPU time
brief: CPU time spent idle while waiting for an I/O operation to complete (in jiffies)
metric_type: cumulative_counter
---
### I/O CPU time

> Amount of total CPU time spent idle while waiting for an I/O operation to complete

In order to get a percentage this value must be compared against the sum of all CPU states.

A high value for a sustained period may be caused by:

* A slow hardware device that is taking too long to service requests
* Too many requests being sent to an I/O device
