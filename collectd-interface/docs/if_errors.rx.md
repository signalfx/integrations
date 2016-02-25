---
title: Receive errors
brief: Count of receive errors on the interface
metric_type: cumulative_counter
---
### Receive Errors

> Count of receive errors on the interface.

Errors happen due to various reasons. Some reasons are [explained here](http://platforms.infostruction.com/interface-errors-on-linux-centosredhat/)

**Rate/sec rollup** provides the current rate of receive errors on the interface in errors/sec.

**Max rollup** provides total number of receive errors since the beginning. Note that since this is a
cumulative counter, its value will periodically restart from zero when the 
maximum possible value of the counter is exceeded.
