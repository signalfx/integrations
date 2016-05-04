---
title: collectd ActiveMQ Plugin
brief: ActiveMQ metrics for collectd.
---

#![](https://github.com/signalfx/integrations/blob/master/collectd-activemq/img/integrations_activemq.png) ActiveMQ collectd Plugin   

_This is a directory consolidate all the metadata associated with the ActiveMQ collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/activemq-integration)_

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

 ```
 yum install collectd-java
 ```

 #### Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:

 This plugin is included with [SignalFx's collectd package](https://github.com/signalfx/integrations/tree/master/collectd).

1. Download SignalFx's sample JMX configuration file and sample ActiveMQ configuration files:

 - [JMX.conf](https://github.com/signalfx/integrations/blob/master/collectd-java/10-jmx.conf)
 - [ActiveMQ.conf](https://github.com/signalfx/integrations/blob/master/collectd-activemq/20-activemq.conf)

1. Modify 20-activemq.conf to provide values that make sense for your environment, as described in the header.

1. Add the following lines to /etc/collectd.conf, replacing the example paths with the locations of the configuration files you downloaded in step 2:

 ```
 include '/path/to/10-jmx.conf'
 include '/path/to/20-activemq.conf'
 ```

1. Restart collectd.

Metrics from ActiveMQ will begin streaming into SignalFx, and new built-in dashboards will be created for you. Check the status of your new integration on the Integrations page.

### CONFIGURATION

The following configuration options are *required* and have generic defaults. This means that you must update values in configuration for production use.

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| Host | This is the host that is running the ActiveMQ service | `Host "ActiveMQ_Host1[hostHasService=activemq]"` |
| ServiceURL | This is the URL for where the service is running | `ServiceURL "service:jmx:rmi:///jndi/rmi://localhost:1099/jmxrmi"` |

### USAGE

Sample of pre-built dashboard in SignalFx:

![](././img/dashboard_activemq.png)

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This plugin is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/activemq-integration/blob/master/LICENSE) for more details.
