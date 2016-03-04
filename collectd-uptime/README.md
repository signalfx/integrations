---
title: Uptime collectd Plugin
brief: Uptime plugin for collectd.
---
![](https://github.com/signalfx/Integrations/blob/master/collectd/img/integrations_collectd.png)
# Uptime collectd Plugin

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

- collectd 4.7+

### INSTALLATION

This plugin is included with [SignalFx collectd](https://github.com/signalfx/Integrations/tree/master/collectd).

### CONFIGURATION

There are no configuration options for this plugin.

### USAGE

>This section contains information about how best to monitor the software in question, using the data from this plugin. In this section, the plugin author shares experience and expertise with the software to be monitored, for the benefit of users of the plugin. This section includes:
>
>- Important conditions to watch out for in the software
>- Common failure modes, and the values of metrics that will allow the user to spot them
>- Chart images demonstrating each important condition or failure mode

This plugin is an example that emits values on its own, and does not connect to software. It emits a repeating sine wave in the metric gauge.sine. The metric should look like this:

![Example chart showing gauge.sine](http://fixme)

The following conditions may be cause for concern:

*You see a straight line instead of a curve.*

This may indicate a period of missing data points. In the example chart shown above, some data points are missing between 16:40 and 16:41, and SignalFx is interpolating a straight line through the gap.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

License for this plugin can be found [in the header of the plugin](https://github.com/collectd/collectd/blob/master/src/uptime.c)
