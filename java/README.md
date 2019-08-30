# ![](./img/integrations_java.png) Java

Metadata associated with the Java plugin for collectd can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-java">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/java.c">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)


### USAGE

Use the Java collectd plugin to collect metrics from Java applications using JMX. SignalFx supports several integrations that depend on this plugin:

* [ActiveMQ](https://github.com/signalfx/integrations/tree/master/activemq)[](sfx_link:activemq)
* [Cassandra](https://github.com/signalfx/integrations/tree/master/cassandra)[](sfx_link:cassandra)
* [Kafka](https://github.com/signalfx/integrations/tree/master/kafka)[](sfx_link:kafka)

### METRICS

The metrics emitted by this plugin depend on its configuration and the metrics emitted by the Java application that it is configured to monitor. Examples of SignalFx integrations that rely on this plugin are [ActiveMQ](https://github.com/signalfx/integrations/tree/master/activemq)[](sfx_link:activemq), [Cassandra](https://github.com/signalfx/integrations/tree/master/cassandra)[](sfx_link:cassandra) and [Kafka](https://github.com/signalfx/integrations/tree/master/kafka)[](sfx_link:kafka).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
