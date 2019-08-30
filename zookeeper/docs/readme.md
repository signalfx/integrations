---
title: Apache ZooKeeper Metrics
brief: Metrics collected from ZooKeeper nodes
---
### Apache ZooKeeper Metrics

Use the [collectd-zookeeper](https://github.com/signalfx/collectd-zookeeper) collectd plugin to collect metrics for Apache ZooKeeper.

Use this plugin to monitor the following types of information from a ZooKeeper node:

* node count
* sent/received packet count
* request latency statistic.
* watch counts
* data size
* open file descriptors

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| ZooKeeper | 3.4.0 or later |

### Configuration
If you have more than one instance of ZooKeeper running on the box then you can distinguish them by specifying a Instance variable in your Module configuration. This will appear in SignalFx as values of the **plugin_instance** dimension.
