# Aggregation

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Configuration](#configuration)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use the <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:Aggregation">aggregation</a> plugin to aggregate metrics. This plugin provides aggregates, by default average and summary.

### REQUIREMENTS AND DEPENDENCIES

| Software           | Version               |
|--------------------|-----------------------|
| collectd           |  1.3 or later         |
| aggregation plugin | collectd 5.2 or later |


### CONFIGURATION
By default the CPU plugin will assign each CPU a number and use that as the plugin\_instance. This gives a very detailed report of CPU usage, but it is not generally useful. Use the <a target="_blank" href="https://github.com/signalfx/Integrations/blob/master/collectd-aggregation/10-aggregation-cpu.conf">following configuration</a> to aggregate CPU metrics.


### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
