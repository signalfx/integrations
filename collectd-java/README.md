#![](https://github.com/signalfx/integrations/blob/master/collectd-java/img/integrations_java.png) Java

_This directory consolidates all the metadata associated with the Java plugin for collectd. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/java.c)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

The Java plugin for collectd is required to use SignalFx's integrations with Java applications like [ActiveMQ](../collectd-activemq), [Cassandra](../collectd-cassandra) and [Kafka](../collectd-kafka).

From the [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Java):

> The Java plugin embeds a Java virtual machine (JVM) into collectd and exposes the application programming interface (API) to Java programs. This allows to write own plugins in the popular language, which are then loaded and executed by the daemon without the need to start a new process and JVM every few seconds. Java classes written for the Java plugin are therefore more powerful and efficient than scripts executed by the Exec plugin.

### REQUIREMENTS AND DEPENDENCIES

| Software  | Version        |
|-----------|----------------|
| collectd  | 4.7+ |

### INSTALLATION

1. On RHEL/CentOS and Amazon Linux systems, run the following command to install this plugin:

         yum install collectd-java
         
    On Ubuntu and Debian systems, this plugin is included by default with the [SignalFx collectd agent](../collectd). 

1. Download SignalFx's example configuration file for the Java plugin to `/etc/collectd/managed_config`: [10-jmx.conf](https://github.com/signalfx/integrations/blob/master/collectd-java/10-jmx.conf)

1. Restart collectd. 

### CONFIGURATION

No additional configuration is required if using the example configuration file [`10-jmx.conf`](./10-jmx.conf).

Full configuration details for this plugin are available on the [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Java).

### USAGE

Use the Java collectd plugin to collect metrics from Java applications using JMX. SignalFx supports several integrations that depend on this plugin:

* [ActiveMQ](https://github.com/signalfx/integrations/tree/master/collectd-activemq) 
* [Cassandra](https://github.com/signalfx/integrations/tree/master/collectd-cassandra)
* [Kafka](https://github.com/signalfx/integrations/tree/master/collectd-kafka)

### METRICS

The metrics emitted by this plugin depend on its configuration and the metrics emitted by the Java application that it is configured to monitor. Examples of SignalFx integrations that rely on this plugin are [ActiveMQ](../collectd-activemq), [Cassandra](../collectd-cassandra) and [Kafka](../collectd-kafka).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
