---
title: MongoDB Metrics
brief: Metrics collected from collectd MongoDB plugin.
---
### MongoDB Metrics

Use the [mongodb](https://github.com/signalfx/collectd-mongodb) collectd 
plugin to collect metrics from MongoDB nodes.

The plugin uses collectd to capture following statistical data:

* memory
* network input/output bytes count
* heap usage
* db connections
* operations count
* active client connections
* queued operations
    
The plugin also captures following DB-specific metrics:

* db size
* db counters
    
Original MongoDB Documentation http://docs.mongodb.org/manual/

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| MongoDB   |  2.4 or later  |

### Configuration

Download SignalFx's example configuration for this plugin here: https://github.com/signalfx/signalfx-collectd-configs/tree/master/managed_config

The value of **Instance** in the plugin configuration file will appear as the dimension called **plugin_instance** in 
SignalFx. Use this dimension to distinguish between MongoDB nodes.

If the MongoDB node is part of a cluster, then cluster name will appear as the dimension called **cluster** in SignalFx. Use this dimension to group together MongoDB nodes that share the same cluster.

Database name will appear as the dimension called **db** in SignalFx. Use this dimension to distinguish between DBs in a node.
