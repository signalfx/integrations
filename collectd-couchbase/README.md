---
title: collectd Couchbase Plugin
brief: Couchbase metrics for collectd.
---

# Couchbase Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

`collectd-couchbase` is a [collectd](http://www.collectd.org/) plugin that
collects statistics from Couchbase.

### REQUIREMENTS AND DEPENDENCIES

#### Required Configuration

The following mandatory configuration options describe how the plugin will
connect to the Couchbase Server:

* CollectTarget - Required option. Define the plugin running instance, has two options: 'NODE' -
get nodes related metrics or 'BUCKET' - get bucket related metrics. Target 'BUCKET' requires to have username and
password to connect to selected bucket
* Host - Required option. Hostname or IP address of the Couchbase server, default is 'localhost'
* Port - Required option. The port of the Couchbase server, default is '8091'

#### Optional Configuration

The following optional settings may be specified to control the behavior of the plugin:

* Username - the username for authentication to selected bucket, default is None.
If your bucket has not set up username and password just ignore this parameter otherwise define them
* Password - the password for authentication to selected bucket, default is None
If your bucket has not set up username and password just ignore this parameter otherwise define them
* Interval - interval between sync metrics calls, default is 10 seconds
* CollectMode - define the mode of plugin running, has two options: 'default' -
get basics metrics or 'detailed' - get all available metrics. See details in `metric_info.py`
* CollectBucket - bucket name for retrieving metrics.
* FieldLength - Set the number of characters used to encode dimension data. This option should only ever be set if
you specifically compiled collectd with a non-default value for DATA_MAX_NAME_LEN in plugin.h

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| python | 2.7 or later |
| couchbase | 4.1 or later |


### INSTALLATION

1. Install the Python plugin for collectd.

 ##### RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09

 Run the following command to install the Python plugin for collectd:
 ```
 yum install collectd-python
 ```
 ##### Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:

 This plugin is included with [SignalFx's collectd package](https://github.com/signalfx/Integrations/tree/master/collectd).

1.
1.
1.
1. #NEED TO ADD ADDITIONAL STEPS
1.
1.


1. Restart collectd.

 Metrics from couchbase will begin streaming into SignalFx, and new built-in dashboards will be created for you. Check the status of your new integration on the Integrations page.
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

### METRICS

For full documentation of the metrics and dimensions emitted by this plugin, see the `docs` directory in this repository.

### LICENSE

This plugin is released under the Apache 2.0 license. See LICENSE for more details.
