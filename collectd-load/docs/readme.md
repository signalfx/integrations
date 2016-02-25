---
title: CPU Load Average Metrics
brief: Metrics related to load on the CPU in the recent past.
---
### CPU Load Average Metrics

CPU load represents CPU contention - the average number of schedulable processes at any given time. 
This is reported as an average value for all CPU cores on the host. Each CPU core can only execute one 
process at a time. Therefore, a CPU load average above 1.0 indicates that the CPUs have 
more work than they can perform, and the system is overloaded. 

CPU load is reported over short term (last one minute), medium term (last five minutes) and long 
term (last fifteen minutes). While it is normal for a host's short term load average to exceed 1.0,
sustained load average above 1.0 on a host may indicate a problem. 

SignalFx recommends looking at CPU load in conjunction with CPU utilization metrics reported by
the plugin:cpu

### Dimensions associated with plugin:interface metrics
* **host**: host/server from which this metric is being collected, e.g. 'i-1234abcd' or 'myappserver'.

### Further Reading
* [Wikipedia article](https://en.wikipedia.org/wiki/Load_%28computing%29) on CPU Load
* [LinuxJournal article](http://www.linuxjournal.com/article/9001) explaining CPU load
* collectd documentation for [Plugin:Load](https://collectd.org/wiki/index.php/Plugin:Load)
