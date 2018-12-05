# ![](./img/integrations_java.png) Java

Metadata associated with the Java plugin for collectd can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-java">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/java.c">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

The Java plugin for collectd is required to use SignalFx's integrations with Java applications like [ActiveMQ](https://github.com/signalfx/integrations/tree/master/collectd-activemq)[](sfx_link:collectd-activemq), [Cassandra](https://github.com/signalfx/integrations/tree/master/collectd-cassandra)[](sfx_link:collectd-cassandra) and [Kafka](https://github.com/signalfx/integrations/tree/master/collectd-kafka)[](sfx_link:collectd-kafka).

Read more about the Java plugin for collectd on the <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:Java">collectd wiki</a>.

### REQUIREMENTS AND DEPENDENCIES

| Software  | Version        |
|-----------|----------------|
| collectd  | 4.7+ |

### INSTALLATION

1. Install the plugin:

    * On RHEL/CentOS and Amazon Linux systems, run the following command to install this plugin:

            yum install collectd-java


    * On Ubuntu and Debian systems, this plugin is included by default with the [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd).

2. Download SignalFx's example configuration file for the Java plugin to `/etc/collectd/managed_config`: <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/collectd-java/10-jmx.conf">10-jmx.conf</a>

3. Download [signalfx\_types\_db](https://github.com/signalfx/integrations/tree/master/collectd-java/signalfx_types_db) and configure its location as described inside of the `10-jmx.conf` configuration file (Default location is  `/usr/share/collectd/java-collectd-plugin/signalfx_types_db`).

4. Restart collectd.

### CONFIGURATION

No additional configuration is required, however full configuration details for this plugin are available on the <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:Java">collectd wiki</a>.

### USAGE

Use the Java collectd plugin to collect metrics from Java applications using JMX. SignalFx supports several integrations that depend on this plugin:

* [ActiveMQ](https://github.com/signalfx/integrations/tree/master/collectd-activemq)[](sfx_link:collectd-activemq)
* [Cassandra](https://github.com/signalfx/integrations/tree/master/collectd-cassandra)[](sfx_link:collectd-cassandra)
* [Kafka](https://github.com/signalfx/integrations/tree/master/collectd-kafka)[](sfx_link:collectd-kafka)

### METRICS

The metrics emitted by this plugin depend on its configuration and the metrics emitted by the Java application that it is configured to monitor. Examples of SignalFx integrations that rely on this plugin are [ActiveMQ](https://github.com/signalfx/integrations/tree/master/collectd-activemq)[](sfx_link:collectd-activemq), [Cassandra](https://github.com/signalfx/integrations/tree/master/collectd-cassandra)[](sfx_link:collectd-cassandra) and [Kafka](https://github.com/signalfx/integrations/tree/master/collectd-kafka)[](sfx_link:collectd-kafka).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
