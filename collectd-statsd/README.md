---
title: StatsD collectd Plugin
brief: StatsD plugin for collectd.
---


# ![](https://github.com/signalfx/Integrations/blob/master/collectd/img/integrations_collectd.png) StatsD collectd Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:StatsD):

> The StatsD plugin implements the StatsD network protocol to allow clients to report "events", such as the serving of a web page. These events are aggregated by collectd and dispatched regularly.

> The plugin supports four event types:

> * Counter
* Timer
* Gauge
* Set

> It also supports "multi metric pakets", i.e. packets containing multiple metrics and different metric types with the same name.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd |  5.4+  |

### INSTALLATION

1. Install the collectd plugin.
 ##### Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:
 This plugin is included with [SignalFx's collectd package](https://github.com/signalfx/Integrations/tree/master/collectd).

 ##### RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09
 Run the following command to install this plugin:
 ```
 yum install collectd-statsd
 ```
1. Download SignalFx's [sample statsd configuration file](https://github.com/signalfx/Integrations/blob/master/collectd-statsd/10-statsd.conf)

  Modify the sample configuration file to provide values that make sense for your environment, as described in the header.

1. Add the following line to /etc/collectd.conf, replacing the example path with the location of the configuration file you downloaded in step 2:
```
include '/path/to/10-statsd.conf'
```
1. Restart collectd.

Metrics from statsd will begin streaming into SignalFx, and new built-in dashboards will be created for you.

### CONFIGURATION

Configuration for this plugin is kept in the main [collectd.conf](https://github.com/signalfx/Integrations/blob/master/collectd/collectd.conf) file.

From the [collectd wiki](https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_statsd):

> The statsd plugin listens to a UDP socket, reads "events" in the statsd protocol and dispatches rates or other aggregates of these numbers periodically.

> The plugin implements the _Counter_, _Timer_, _Gauge_ and _Set_ types which are dispatched as the collectd types `derive`, `latency`, `gauge` and `objects` respectively.


| Configuration Option | Type | Definition |
|----------------------|------|------------|
|Host| Host| Bind to the hostname / address Host. By default, the plugin will bind to the "any" address, i.e. accept packets sent to any of the hosts addresses.|
|Port |Port|UDP port to listen to. This can be either a service name or a port number. Defaults to 8125.|
|DeleteCounters |false/true| Controls what happens if metrics are not updated in an interval. If set to False, the default, metrics are dispatched unchanged, i.e. the rate of counters and size of sets will be zero, timers report NaN and gauges are unchanged. If set to True, the such metrics are not dispatched and removed from the internal cache.|
|DeleteTimers |false/true|Controls what happens if metrics are not updated in an interval. If set to False, the default, metrics are dispatched unchanged, i.e. the rate of counters and size of sets will be zero, timers report NaN and gauges are unchanged. If set to True, the such metrics are not dispatched and removed from the internal cache. |
|DeleteGauges |false/true|Controls what happens if metrics are not updated in an interval. If set to False, the default, metrics are dispatched unchanged, i.e. the rate of counters and size of sets will be zero, timers report NaN and gauges are unchanged. If set to True, the such metrics are not dispatched and removed from the internal cache. |
|DeleteSets| false/true|Controls what happens if metrics are not updated in an interval. If set to False, the default, metrics are dispatched unchanged, i.e. the rate of counters and size of sets will be zero, timers report NaN and gauges are unchanged. If set to True, the such metrics are not dispatched and removed from the internal cache. |
|TimerPercentile |Percent|Calculate and dispatch the configured percentile, i.e. compute the latency, so that Percent of all reported timers are smaller than or equal to the computed latency. This is useful for cutting off the long tail latency, as it's often done in Service Level Agreements (SLAs). Different percentiles can be calculated by setting this option several times. If none are specified, no percentiles are calculated / dispatched.|
|TimerLower |false/true| Calculate and dispatch various values out of Timer metrics received during an interval. If set to False, the default, these values aren't calculated / dispatched.|
|TimerUpper |false/true| Calculate and dispatch various values out of Timer metrics received during an interval. If set to False, the default, these values aren't calculated / dispatched.|
|TimerSum |false/true| Calculate and dispatch various values out of Timer metrics received during an interval. If set to False, the default, these values aren't calculated / dispatched. |
|TimerCount |false/true|Calculate and dispatch various values out of Timer metrics received during an interval. If set to False, the default, these values aren't calculated / dispatched.|

### USAGE


### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

License for this plugin can be found [in the header of the plugin](https://github.com/signalfx/collectd/blob/master/src/statsd.c).
