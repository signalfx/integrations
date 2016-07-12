---
title: Redis collectd Plugin
brief: Redis plugin for collectd.
---

# ![](https://github.com/signalfx/integrations/blob/master/collectd-redis/img/integrations_redis.png) Redis collectd Plugin

_This is a directory that consolidates all the metadata associated with the Redis collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/redis-collectd-plugin)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

A [Redis](http://redis.io) plugin for [collectd](http://collectd.org) using collectd's [Python plugin](http://collectd.org/documentation/manpages/collectd-python.5.shtml).

You can capture any kind of Redis metrics like:

 * Memory used
 * Commands processed per second
 * Number of connected clients and slaves
 * Number of blocked clients
 * Number of keys stored (per database)
 * Uptime
 * Changes since last save
 * Replication delay (per slave)

#### FEATURES

##### Built-in dashboards

- **Redis Instances**: Overview of data from all Redis instances.

 [<img src='./img/dashboard_redis_instances.png' width=200px>](./img/dashboard_redis_instances.png)

- **Redis Instance**: Focus on a single Redis instance.

 [<img src='./img/dashboard_redis_instance.png' width=200px>](./img/dashboard_redis_instance.png)  

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd   |  4.9+  |
| Python plugin for collectd | (included with SignalFx collectd) |
| Python    |  2.6+ |
| redis | 2.8+ |


### INSTALLATION

1. Download the Python module from the following URL:

 https://github.com/signalfx/redis-collectd-plugin

1. Download SignalFx's sample configuration files for a [Redis master](././10-redis_master.conf) or [Redis slave](././10-redis_slave.conf) to `/etc/collectd/managed_config`. 

1. Modify the sample configuration file as described in  [Configuration](#configuration), below.

1. Restart collectd.

### CONFIGURATION

Using the example configuration files [`10-redis_master.conf`](././10-redis_master.conf) or [`10-redis_slave.conf`](././10-redis_slave.conf) as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the Redis instance to be monitored.

| Configuration Option | Type | Definition |
|----------------------|------|------------|
| Instance | Nodename | The Node block identifies a new Redis node, that is a new Redis instance running in an specified host and port. The name for node is a canonical identifier which is used as plugin instance. It is limited to 64 characters in length.|
| Host | Hostname |The Host option is the hostname or IP-address where the Redis instance is running on.|
|Port |Port| The Port option is the TCP port on which the Redis instance accepts connections. Either a service name of a port number may be given. Please note that numerical port numbers must be given as a string, too.|
|Instance |Type instance|Within a query definition, an optional type instance to use when submitting the result of the query. When not supplied will default to the escaped command, up to 64 chars.|

### Multiple Redis instances

You can configure to monitor multiple redis instances by the same machine by repeating the <Module> section, such as:

```
<Plugin python>
  ModulePath "/opt/collectd_plugins"
  Import "redis_info"

  <Module redis_info>
    Host "127.0.0.1"
    Port 9100
    Verbose true
    Instance "instance_9100"
    Redis_uptime_in_seconds "gauge"
    Redis_used_memory "bytes"
    Redis_used_memory_peak "bytes"
  </Module>

  <Module redis_info>
    Host "127.0.0.1"
    Port 9101
    Verbose true
    Instance "instance_9101"
    Redis_uptime_in_seconds "gauge"
    Redis_used_memory "bytes"
    Redis_used_memory_peak "bytes"
    Redis_master_repl_offset "gauge"
  </Module>

  <Module redis_info>
    Host "127.0.0.1"
    Port 9102
    Verbose true
    Instance "instance_9102"
    Redis_uptime_in_seconds "gauge"
    Redis_used_memory "bytes"
    Redis_used_memory_peak "bytes"
    Redis_slave_repl_offset "gauge"
  </Module>
</Plugin>
```

These 3 redis instances listen on different ports, they have different plugin_instance combined by Host and Port:

```
"plugin_instance" => "127.0.0.1:9100",
"plugin_instance" => "127.0.0.1:9101",
"plugin_instance" => "127.0.0.1:9102",
```

These values will be part of the metric name emitted by collectd, e.g. `collectd.redis_info.127.0.0.1:9100.bytes.used_memory`

If you want to set a static value for the plugin instance, use the ```Instance``` configuration option:

```
...
  <Module redis_info>
    Host "127.0.0.1"
    Port 9102
    Instance "redis-prod"
  </Module>
...
```

This will result in metric names like: `collectd.redis_info.redis-prod.bytes.used_memory`

`Instance` can be empty, in this case the name of the metric will not contain any reference to the host/port. If it is omitted, the host:port value is added to the metric name.

### Multiple Data source types
You can send multiple data source types from same key by specifying it in the Module:

```
...
  <Module redis_info>
    Host "localhost"
    Port 6379

    Redis_total_net_input_bytes "bytes"
    Redis_total_net_output_bytes "bytes"
    Redis_total_net_input_bytes "derive"
    Redis_total_net_output_bytes "derive"
  </Module>
...
```

### USAGE

Sample of pre-built dashboard in SignalFx:

![](././img/dashboard_redis.png)

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
