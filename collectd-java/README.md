# ![](./img/integrations_java.png) Java

_This directory consolidates all the metadata associated with the Java plugin for collectd. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/java.c)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

The Java plugin for collectd is required to use SignalFx's integrations with Java applications like [ActiveMQ](https://github.com/signalfx/integrations/tree/master/collectd-activemq)[](sfx_link:collectd-activemq), [Cassandra](https://github.com/signalfx/integrations/tree/master/collectd-cassandra)[](sfx_link:collectd-cassandra) and [Kafka](https://github.com/signalfx/integrations/tree/master/collectd-kafka)[](sfx_link:collectd-kafka).

Read more about the Java plugin for collectd on the [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Java).

### REQUIREMENTS AND DEPENDENCIES

| Software  | Version        |
|-----------|----------------|
| collectd  | 4.7+ |

### INSTALLATION

1. On RHEL/CentOS and Amazon Linux systems, run the following command to install this plugin:

         yum install collectd-java

    On Ubuntu and Debian systems, this plugin is included by default with the [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd).

1. Download SignalFx's example configuration file for the Java plugin to `/etc/collectd/managed_config`: [10-jmx.conf](https://github.com/signalfx/integrations/blob/master/collectd-java/10-jmx.conf)

1. Download [signalfx_types_db](https://github.com/signalfx/integrations/tree/master/collectd-java/signalfx_types_db) and configure its location as described inside of the `10-jmx.conf` configuration file (Default location is  `/usr/share/collectd/java-collectd-plugin/signalfx_types_db`).

1. Restart collectd.

### CONFIGURATION

No additional configuration is required, however full configuration details for this plugin are available on the [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Java).

### USAGE

Use the Java collectd plugin to collect metrics from Java applications using JMX. SignalFx supports several integrations that depend on this plugin:

* [ActiveMQ](https://github.com/signalfx/integrations/tree/master/collectd-activemq)[](sfx_link:collectd-activemq)
* [Cassandra](https://github.com/signalfx/integrations/tree/master/collectd-cassandra)[](sfx_link:collectd-cassandra)
* [Kafka](https://github.com/signalfx/integrations/tree/master/collectd-kafka)[](sfx_link:collectd-kafka)

### METRICS

The metrics emitted by this plugin depend on its configuration and the metrics emitted by the Java application that it is configured to monitor. Examples of SignalFx integrations that rely on this plugin are [ActiveMQ](https://github.com/signalfx/integrations/tree/master/collectd-activemq)[](sfx_link:collectd-activemq), [Cassandra](https://github.com/signalfx/integrations/tree/master/collectd-cassandra)[](sfx_link:collectd-cassandra) and [Kafka](https://github.com/signalfx/integrations/tree/master/collectd-kafka)[](sfx_link:collectd-kafka).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
