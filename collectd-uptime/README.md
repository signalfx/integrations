# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_collectd.png) Uptime collectd Plugin

Metadata associated with the Tail collectd plugin can be found [here](https://github.com/signalfx/integrations/tree/release/collectd-uptime). The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/uptime.c).

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Uptime)

> The Uptime plugin keeps track of the system uptime, providing informations such as the average running time or the maximum reached uptime over a certain period of time. It can be useful especially on Linux based routers/firewalls.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
|  collectd    |  4.7+  |

### INSTALLATION

**If you are using the new SmartAgent, see the docs for [the collectd/uptime
monitor](https://github.com/signalfx/signalfx-agent/tree/master/docs/monitors/collectd-uptime.md)
for more information.  The configuration documentation below may be helpful as
well, but consult the SmartAgent repo's docs for the exact schema.**


Installation and initial configuration options are available as part of the [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd).


### CONFIGURATION

There are no configuration options for this plugin.

### USAGE

This plugin provide the time that an individual host has been up since last boot.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

License for this plugin can be found [in the header of the plugin](https://github.com/signalfx/collectd/blob/master/src/uptime.c)
