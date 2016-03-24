---
title: Redis Metrics
brief: Metrics collected from Redis nodes
---
### Redis Metrics

Use the [redis-collectd-plugin](https://github.com/signalfx/redis-collectd-plugin) collectd plugin to collect metrics for Redis.

Use this plugin to monitor the following types of information from a Redis node:

* cpu/memory used
* net input/output bytes count
* keyspace hits/misses
* replication stats

Original Redis Documentation http://redis.io/commands/INFO

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| Redis     | 2.8.19         |

### Configuration
If you have more than one instance of Redis running on the box they will be distinguished by the port they're being talked to over.  The hostname:port will 
become the **plugin_instance** in SignalFx.

Example master config located at https://github.com/signalfx/signalfx-collectd-configs/blob/master/managed_config/10-redis_master.conf
Example slave config located at https://github.com/signalfx/signalfx-collectd-configs/blob/master/managed_config/10-redis_slave.conf
