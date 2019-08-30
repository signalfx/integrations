---
title: Apache Kafka Broker Metrics
brief: Metrics collected from Apache Kafka Broker 0.8.2 and above.
---
### Kafka Broker Metrics

Use the [generic-jmx](https://collectd.org/wiki/index.php/Plugin:GenericJMX) collectd plugin to collect metrics about Apache Kafka. An example config file for collecting data about Kafka using this plugin can be found in our [collectd configs repo](https://github.com/signalfx/signalfx-collectd-configs/blob/master/managed_config/20-kafka_82.conf).

Use this plugin to monitor the following types of information from Kafka broker nodes:

* bytes in
* bytes out
* messages in
* request queue size
* log flush latency
* producer request times
* consumer request times
* follower request times
* number of active controllers

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| Kafka     | 0.8.2 or later |
