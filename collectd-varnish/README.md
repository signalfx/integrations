---
title: Varnish collectd Plugin
brief: Varnish plugin for collectd.
---


# ![](https://github.com/signalfx/Integrations/blob/master/collectd-varnish/img/integrations_varnish.png) Varnish collectd Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION


### REQUIREMENTS AND DEPENDENCIES


### INSTALLATION

1. Install the collectd plugin.

##### Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:

 This plugin is included with [SignalFx's collectd package](https://github.com/signalfx/Integrations/tree/master/collectd).

##### RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09

 Run the following command to install this plugin:
 ```
 yum install collectd-varnish
 ```
1. Download SignalFx's [sample varnish configuration file](https://github.com/signalfx/Integrations/blob/master/collectd-varnish/10-varnish.conf)

 Modify the sample configuration file to provide values that make sense for your environment, as described in the header.

1. Add the following line to /etc/collectd.conf, replacing the example path with the location of the configuration file you downloaded in step 2:
```
include '/path/to/10-varnish.conf'
```
1. Restart collectd.

Metrics from Varnish will begin streaming into SignalFx, and new built-in dashboards will be created for you. Check the status of your new integration on the Integrations page.

### CONFIGURATION

>Provide in this section instructions on how to configure the plugin, before and after installation. If this plugin has a configuration file with properties, list each property, define its purpose and give an example or list the default value.

#### Required configuration

The following configuration options are *required* and have no defaults. This means that you must supply values for them in configuration in order for the plugin to work.

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| required_option | An example of a required configuration property. | 12345 |

#### Optional configuration

The following configuration options are *optional*. You may specify them in the configuration file in order to override default values provided by the plugin.

| configuration option | definition | default value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | "/opt/example" |
| Frequency  | Cycles of the sine wave per minute. | 0.5 |

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

>This section refers to the metrics documentation found in the `/docs` subdirectory. See [`/docs/README.md`](././docs/readme.md) for formatting instructions.

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

> Include licensing information for the plugin in this section.

This plugin is released under the Apache 2.0 license. See LICENSE for more details.
