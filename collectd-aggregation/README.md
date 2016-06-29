---
title: Aggregated CPU Metrics
brief: Metrics collected about CPU usage as a whole instead of per-cpu
---
### Aggregated CPU Metrics

Use the [aggregation](https://collectd.org/wiki/index.php/Plugin:Aggregation) to aggregate metrics.

See the [cpu](https://github.com/signalfx/Integrations/collectd-cpu) plugin for information on the specific metrics.  This plugin provides aggregates, by default average and summary.

#### Version information

| Software           | Version               |
|--------------------|-----------------------|
| collectd           |  1.3 or later         |
| aggregation plugin | collectd 5.2 or later |


### Configuration
By default the CPU plugin will assign each CPU a number and use that as the plugin_instance. This gives a very detailed report of CPU usage, but it is not generally useful. Use the [following configuration](https://github.com/signalfx/Integrations/blob/master/collectd-aggregation/10-aggregation-cpu.conf) to aggregate CPU metrics.
