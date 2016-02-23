# ActiveMQ Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This is the SignalFx ActiveMQ plugin. Follow these instructions to configure the Java plugin for collectd to monitor ActiveMQ. This will send data about ActiveMQ to SignalFx, enabling built-in ActiveMQ monitoring dashboards.

Use this plugin to monitor the following types of information from ActiveMQ:

* Broker (Totals per broker)
* Queue (Queue status)
* Topic (Topic status)


### REQUIREMENTS AND DEPENDENCIES

Use the [generic-jmx](https://collectd.org/wiki/index.php/Plugin:GenericJMX) collectd plugin to collect metrics about Apache ActiveMQ. An example config file for collecting data about ActiveMQ using this plugin can be found in our [collectd configs repo](https://github.com/signalfx/signalfx-collectd-configs/blob/master/managed_config/20-activemq.conf).

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| ActiveMQ  | 5.8.0 or later |


### INSTALLATION

1. Install the Java plugin.

#### RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09

Run the following command to install the Java plugin for collectd:

`yum install collectd-java`

#### Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:

This plugin is included with SignalFx's collectd package.

1. Download SignalFx's sample JMX configuration file and sample ActiveMQ configuration file from the following URLs:

https://github.com/signalfx/signalfx-collectd-configs/blob/master/managed_config/10-jmx.conf

https://github.com/signalfx/signalfx-collectd-configs/blob/master/managed_config/20-activemq.conf

1. Modify 20-activemq.conf to provide values that make sense for your environment, as described in the header.

1. Add the following lines to /etc/collectd.conf, replacing the example paths with the locations of the configuration files you downloaded in step 2:

`include '/path/to/10-jmx.conf'`
`include '/path/to/20-activemq.conf'`

1. Restart collectd.

Metrics from ActiveMQ will begin streaming into SignalFx, and new built-in dashboards will be created for you. Check the status of your new integration on the Integrations page.

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

