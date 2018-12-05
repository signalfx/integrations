# ![](https://github.com/signalfx/integrations/blob/master/collectd-statsd/img/integrations_statsd.png) StatsD

Metadata associated with the StatsD collectd plugin can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-statsd">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/statsd.c">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

### DESCRIPTION

The StatsD plugin for collectd listens for StatsD events, aggregates them and transmits them according to collectd's configuration. Use this plugin to send data from StatsD to SignalFx.

From <a target="_blank" href="https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_statsd">collectd's manpage</a>:

> The statsd plugin listens to a UDP socket, reads "events" in the statsd protocol and dispatches rates or other aggregates of these numbers periodically.

> The plugin implements the `Counter`, `Timer`, `Gauge` and `Set` types which are dispatched as the collectd types `derive`, `latency`, `gauge` and `objects` respectively.

For more information about StatsD, see <a target="_blank" href="https://github.com/etsy/statsd/">https://github.com/etsy/statsd/</a>.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd |  5.4+  |

### INSTALLATION

NOTE: This plugin is included by default with all versions of the [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd).

1. Download SignalFx's <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/collectd-statsd/10-statsd.conf">sample StatsD configuration file</a> to `/etc/collectd/managed_config`.

2. Restart collectd.

#### Verifying installation

You can send StatsD metrics locally with `netcat` as follows, then verify in SignalFx that the metric arrived.

```
$ echo "statsd.test:1|g" | nc -w 1 -u 127.0.0.1 8125
```

### CONFIGURATION

SignalFx's example configuration file for this plugin can be used as-is, without modification. To read more about available configuration options, see <a target="_blank" href="https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_statsd">collectd's manpage for this plugin</a>.

#### Deployment options

SignalFx recommends deploying the [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd), including this plugin, on every host that is reporting StatsD metrics. Having done so, configure all StatsD clients to direct metrics from individual reporters to `localhost`, on the port specified in `10-statsd.conf` (by default: 8125). In this scenario, all metrics are aggregated locally, reducing network traffic.

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

### USAGE

#### Adding dimensions to StatsD metrics

Add dimensions to your metrics by adding key-value pairs to your StatsD metric names as follows:

```
$ echo "statsd.[foo=bar,dim=val]test:1|g" | nc -w 1 -u 127.0.0.1 8125
```

This creates a metric called `statsd.test` of type gauge, with dimensions `foo=bar` and `dim=val`.

StatsD's python API allows you to construct your StatsClient with a prefix. This can simplify the configuration of dimensions.

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

Note that you may specify dimensions by adding bracketed key-value pairs either in the prefix, or on each metric, but not both. If bracketed dimension sections are included in both the prefix and metric name, SignalFx will use the one specified in the metric name.

The following example produces a metric called `test.gaugor` of type gauge, with dimension `foo=bar`. Dimension `dim=val`, specified in the prefix, is ignored.

```python
>>> c = statsd.StatsClient('localhost', 8125, prefix="test[dim=val]")
>>> c.gauge("[foo=bar]gaugor", 400)
```

#### Using StatsD metrics in SignalFx

SignalFx supports using the components of dot-delimited metric names as dimensions for the purposes of filtering and aggregation in a chart. <a target="_blank" href="http://docs.signalfx.com/en/latest/charts/chart-advanced-config.html#graphite-options-for-plots">Click here to read more</a>.

#### Deleting unused metric names from collectd's internal cache

SignalFx's default configuration for this plugin sets all `Delete[Type]s` configuration options to `True`. We strongly recommend this in order to ensure that metrics that have stopped reporting are not reported as 0 in perpetuity. Setting these parameters to `False` results in collectd's memory usage increasing over time, as the set of metrics reported from StatsD grows indefinitely. This is especially important in environments that are long-running or whose metrics change frequently.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
