# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_collectd.png) StatsD

_This is a directory that consolidates all the metadata associated with the StatsD collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/statsd.c)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

The StatsD plugin for collectd listens for StatsD events, aggregates them and transmits them according to collectd's configuration. Use this plugin to send data from StatsD to SignalFx.

From [collectd's manpage](https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_statsd):

> The statsd plugin listens to a UDP socket, reads "events" in the statsd protocol and dispatches rates or other aggregates of these numbers periodically.

> The plugin implements the `Counter`, `Timer`, `Gauge` and `Set` types which are dispatched as the collectd types `derive`, `latency`, `gauge` and `objects` respectively.

For more information about StatsD, see https://github.com/etsy/statsd/.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd |  5.4+  |

### INSTALLATION

1. On RHEL/CentOS and Amazon Linux systems, run the following command to install this plugin:

         yum install collectd-statsd
         
   On Ubuntu and Debian systems, this plugin is included by default with the [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd). 

1. Download SignalFx's [sample StatsD configuration file](https://github.com/signalfx/integrations/blob/master/collectd-statsd/10-statsd.conf) to `/etc/collectd/managed_config`.

1. Restart collectd.

#### Verifying installation

You can send StatsD metrics locally with `netcat` as follows, then verify in SignalFx that the metric arrived.

```
$ echo "statsd.test:1|g" | nc -w 1 -u 127.0.0.1 8125 
```

### CONFIGURATION

SignalFx's example configuration file for this plugin can be used as-is, without modification. To read more about available configuration options, see [collectd's manpage for this plugin](https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_statsd).

### USAGE

#### Deployment options

SignalFx recommends deploying the SignalFx collectd agent including this plugin on every host that is reporting StatsD metrics. Having done so, configure all StatsD clients to direct metrics from individual reporters to `localhost`, on the port specified in `10-statsd.conf` (by default: 8125). In this scenario, all metrics are aggregated locally, reducing network traffic.

This plugin can also listen for and aggregate StatsD metrics from remote hosts. By default, SignalFx's default configuration of the StatsD plugin only opens the StatsD port for local processes. To listen for StatsD metrics sent from remote hosts, configure the StatsD plugin to open the port publicly by modifying `10-statsd.conf` as follows:

```
LoadPlugin statsd
<Plugin statsd>
 Host "0.0.0.0" # changed from "127.0.0.1"
 DeleteSets true
 TimerPercentile 90.0
 TimerLower true
 # ...
</Plugin>
```

#### Adding dimensions to StatsD metrics

Add dimensions to your metrics by adding key-value pairs to your statsd metric names as follows:

```
$ echo "statsd.[foo=bar,dim=val]test:1|g" | nc -w 1 -u 127.0.0.1 8125
```

This creates a metric called `statsd.test` of type gauge, with dimensions `foo=bar` and `dim=val`.

StatsD's python API allows you to construct your StatsClient with a prefix. This can simplify the configuration of dimensions. Note that you may specify the bracketed dimensions either in the prefix, or on each metric, but not both: SignalFx supports only one bracketed dimension section and will use the one closest to the right. 

The examples below produce the same metric and dimensions.

```python
>>> c = statsd.StatsClient('localhost', 8125, prefix="test[dim1=val1]")
>>> c.gauge("gaugor", 400)
```
or

```python 
>>> c = statsd.StatsClient('localhost', 8125, prefix="test")
>>> c.gauge("[dim1=val1]gaugor", 400)
```

#### Using StatsD metrics in SignalFx

SignalFx supports using the components of dot-delimited metric names as dimensions for the purposes of filtering and aggregation in a chart. [Click here to read more](http://docs.signalfx.com/en/latest/charts/chart-advanced-config.html#graphite-options-for-plots). However, it may be more efficient to use the SignalFx metric proxy to transform StatsD's long dot-delimited metric names into metrics with dimensions before transmission to SignalFx. This allows you to specify the transformation once at transmission, rather than many times during chart building. [Click here to read more about the SignalFx metric proxy](https://signalfx.github.com/integrations/tree/master/metricproxy).

#### Deleting unused metric names from collectd's internal cache

SignalFx's default configuration for this plugin sets all `Delete[Type]s` configuration options to `True`. We strongly recommend this in order to ensure that metrics that have stopped reporting are not reported as 0 in perpetuity. Setting these parameters to `False` results in collectd's memory usage increasing over time, as the set of metrics reported from StatsD grows indefinitely. This is especially important in environments that are long-running or whose metrics change frequently. 

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
