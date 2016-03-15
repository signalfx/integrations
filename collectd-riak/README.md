---
title: Riak Plugin
brief: Riak KV metrics using collectd.
---

# ![](https://github.com/signalfx/Integrations/blob/master/collectd-riak/img/integrations_riak.png) Riak KV Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From [Basho site](http://basho.com/products/riak-kv/):

Riak KV is a distributed NoSQL database with a key/value design and advanced local and multi-cluster replication that guarantees reads and writes even in the event of hardware failures or network partitions.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd | 4.9+  |
| cURL-JSON plugin | (match with collectd version) |
|  Riak KV  | 1.4.0+ |

### INSTALLATION


This plugin is included with [SignalFx's collectd package](https://support.signalfx.com/hc/en-us/articles/208080123).

### CONFIGURATION

| Setting	| Value |
|----------|----------|
| Hostname	| ubuntu-12 |
| Base directory for collectd |	/var/lib/collectd |
| collectd .pid file	| /var/run/collectd.pid |
| collectd plugin directory	| /usr/local/lib/collectd |
| collectd types.db file	| /usr/local/share/collectd/types.db |
| Riak stats URL	| http://localhost:8098/stats |
| Riak node/instance name	| riak1@127.0.0.1 |

### USAGE


### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

Since this is not an actual _plugin_ but rather a configuration of the `collectd-curl-json plugin` there is no need for a separate license.
