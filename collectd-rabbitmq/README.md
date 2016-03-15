---
title: RabbitMQ collectd Plugin
brief: RabbitMQ plugin for collectd.
---

# ![](https://github.com/signalfx/Integrations/blob/master/collectd-rabbitmq/img/integrations_rabbitmq.png) RabbitMQ collectd Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION


### REQUIREMENTS AND DEPENDENCIES

>In this section, list:
>- collectd version requirements
>- Version and configuration requirements for the application being monitored
>- Other plugins that this plugin depends on (like the Python or Java plugins for collectd)
>- Any other dependencies that this plugin requires in order to run successfully

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd | 4.9+ |
| Python plugin for collectd | (match with collectd version) |
| Python |  2.6+  |

### INSTALLATION

1. Install the Python plugin for collectd.

 ##### RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09

 Run the following command to install the Python plugin for collectd:
 ```
 yum install collectd-python
 ```
 ##### Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:

 This plugin is included with [SignalFx's collectd package](https://github.com/signalfx/Integrations/tree/master/collectd).

1. Download the [RabbitMQ Python module]( https://github.com/signalfx/collectd-rabbitmq/)

1. Download SignalFx’s [sample configuration file](https://github.com/signalfx/Integrations/collectd-docker/10-rabbitmq.conf).

1. Modify the configuration file as follows:

 1. Modify the fields “TypesDB and “ModulePath” to point to the location on disk where you downloaded the Python module in step 2.

 1. Provide values that make sense for your environment, as described [below](#configuration).

1. Add the following line to /etc/collectd.conf, replacing the example path with the location of the configuration file you downloaded in step 3:
 ```
 include '/path/to/10-rabbitmq.conf'
 ```
1. Restart collectd.

collectd will begin emitting metrics from RabbitMQ.

### CONFIGURATION

#### REQUIRED CONFIGURATION

| Configuration Option | Type | Definition |
|----------------------|------|------------|
| Username | username| name of authorized user |
| Password | password| password for authorized user|
|Host | host| name of host |
|Port| number | port number to listen for RabbitMQ |

#### OPTIONAL Configuration

| Configuration Option | Type | Definition |
|----------------------|------|------------|
|CollectChannels| true/false| toggles the collection of `channels` metrics |
|CollectConnections| true/false| toggles the collection of `connections` metrics|
|CollectExchanges |true/false| toggles the collection of `exchanges` metrics|
|CollectNodes |true/false| toggles the collection of `nodes` metrics|
|CollectQueues | true/false | toggles the collection of `queues` metrics|
| HTTPTimeout | time (seconds) | will set a timeout value for connecting to the RabbitMQ Management API|

### USAGE


### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This plugin is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/collectd-rabbitmq/blob/master/LICENSE) for more details.
