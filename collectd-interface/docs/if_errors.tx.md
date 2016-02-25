---
title: Transmit errors
brief: Count of transmit errors on the interface
metric_type: cumulative_counter
---
### Transmit Errors

> Count of transmit errors on the interface.

Errors happen due to various reasons. Some reasons are [explained here](http://platforms.infostruction.com/interface-errors-on-linux-centosredhat/)

**Rate/sec rollup** provides the current rate of transmit errors on the interface in errors/sec.

**Max rollup** provides total number of transmit errors since the beginning. Note that since this is a
cumulative counter, its value will periodically restart from zero when the 
maximum possible value of the counter is exceeded.
