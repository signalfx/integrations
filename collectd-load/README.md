# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_collectd.png) Load

Metadata associated with the Load collectd plugin can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-load">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/load.c">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:Load">collectd wiki</a>:

> The Load plugin collects the system load. These numbers give a rough overview over the utilization of a machine, though their meaning is mostly overrated.
The system load is defined as the number of runnable tasks in the run-queue and is provided by many operating systems as a one, five or fifteen minute average.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd |  1.0+ |

### INSTALLATION

**If you are using the new Smart Agent, see the docs for [the collectd/load
monitor](https://github.com/signalfx/signalfx-agent/tree/master/docs/monitors/collectd-load.md)
for more information.  The configuration documentation below may be helpful as
well, but consult the Smart Agent repo's docs for the exact schema.**


Installation and initial configuration options are available as part of the <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd">SignalFx collectd agent</a>.


### CONFIGURATION

The Load plugin does not have any configuration settings.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

License for this plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/load.c">in the header of the plugin</a>
