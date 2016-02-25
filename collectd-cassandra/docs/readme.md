---
title: Apache Cassandra Metrics
brief: Metrics collected from Apache Cassandra 2.0.10 and above
---
### Apache Cassandra Metrics

Use the [generic-jmx](https://collectd.org/wiki/index.php/Plugin:GenericJMX) collectd plugin to collect metrics about Apache Cassandra. An example config file for collecting data about Cassandra using this plugin can be found in our [collectd configs repo](https://github.com/signalfx/signalfx-collectd-configs/blob/master/managed_config/20-cassandra.conf).

Use this plugin to monitor the following types of information from Cassandra nodes:

* read/write/range-slice requests
* read/write/range-slice errors (timeouts and unavailable)
* read/write/range-slice latency (median, 99th percentile, maximum)
* compaction activity
* hint activity

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| cassandra | 2.0.10 or later|
