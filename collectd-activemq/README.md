---
title: collectd ActiveMQ Plugin
brief: ActiveMQ metrics for collectd.
---

#![](https://github.com/signalfx/integrations/blob/master/collectd-activemq/img/integrations_activemq.png) ActiveMQ collectd Plugin   

_This is a directory that consolidates all the metadata associated with the ActiveMQ collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/activemq-integration)_

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

To monitor the age of messages inside ActiveMQ queues, see [ActiveMQ message age listener](../amq-message-age).

#### FEATURES

##### Built-in dashboards

- **ActiveMQ Hosts**: Overview of all data from ActiveMQ hosts.

  [<img src='./img/dashboard_activemq_hosts.png' width=200px>](./img/dashboard_activemq_hosts.png)

- **ActiveMQ Host**: Focus on a single ActiveMQ host.

  [<img src='./img/dashboard_activemq_host.png' width=200px>](./img/dashboard_activemq_host.png)

- **ActiveMQ Queue**: Focus on a single ActiveMQ queue.

  [<img src='./img/dashboard_activemq_queue.png' width=200px>](./img/dashboard_activemq_queue.png)

- **ActiveMQ Topic**: Focus on a single ActiveMQ topic.

  [<img src='./img/dashboard_activemq_topic.png' width=200px>](./img/dashboard_activemq_topic.png)

- **ActiveMQ Message Age**: (if enabled) Shows the average age of messages in ActiveMQ queues. See [ActiveMQ message age listener](../amq-message-age).

  [<img src='./img/dashboard_activemq_messageage.png' width=200px>](./img/dashboard_activemq_messageage.png)

### REQUIREMENTS AND DEPENDENCIES

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| ActiveMQ  | 5.8.0 or later |
| Java plugin for collectd |  (match collectd version) | 
       
### INSTALLATION

#### RHEL/CentOS and Amazon Linux: Install Java plugin for collectd

This integration requires the [Java plugin for collectd](../collectd-java/), which is not included with the SignalFx collectd agent on RHEL/CentOS or Amazon Linux. 

1. Run the following command to install the Java plugin for collectd:

  `yum install collectd-java`

1. Download SignalFx's example configuration file for the Java plugin to `etc/collectd/managed_config`: [10-jmx.conf](https://github.com/signalfx/integrations/blob/master/collectd-java/10-jmx.conf)

1. Restart collectd. 

#### Install ActiveMQ integration 

1. Download SignalFx's example ActiveMQ configuration file to `/etc/collectd/managed_config`:  [20-activemq.conf](https://github.com/signalfx/integrations/blob/master/collectd-activemq/20-activemq.conf)

1. Modify `20-activemq.conf` to provide values that make sense for your environment, as described in [Configuration](#configuration), below.

1. Restart collectd.

### CONFIGURATION

Using the example configuration file [`20-activemq.conf`](././20-activemq.conf) as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the ActiveMQ instance to be monitored.

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| Host | The name of this ActiveMQ broker. Appears as dimension `host` in SignalFx. Note: Do not modify or remove the `[hostHasService=activemq]` section. | `"ActiveMQ_Host1[hostHasService=activemq]"` |
| ServiceURL | URL of the ActiveMQ service. | `ServiceURL "service:jmx:rmi:///jndi/rmi://localhost:1099/jmxrmi"` |

### USAGE

Sample of pre-built dashboard in SignalFx:

![](././img/dashboard_activemq.png)

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
