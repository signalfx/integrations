# ![](https://github.com/signalfx/integrations/blob/master/collectd-redis/img/integrations_redis.png) Redis

_This is a directory that consolidates all the metadata associated with the Redis collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/redis-collectd-plugin)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

A [Redis](http://redis.io) plugin for [collectd](http://collectd.org) using the Python plugin for collectd.

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
| Python plugin for collectd | (included with [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd)) |
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
| Instance | Nodename | The Module block identifies a Redis instance running in an specified host and port. The name for node is a canonical identifier which is used as plugin instance. It is limited to 64 characters in length.|
| Host | Hostname |The Host option is the hostname or IP-address where the Redis instance is running.|
|Port |Port| The Port option is the TCP port on which the Redis instance accepts connections. Either a service name of a port number may be given. Please note that numerical port numbers must be given as a string, too.|
| Auth | Password | Optionally specify a password to use for AUTH. |

#### Note: Monitoring multiple Redis instances on one host

You can configure this plugin to monitor multiple Redis instances on the same machine by repeating the <Module> section, as in the following example:

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

#### Note: value of plugin_instance

In the example above, 3 redis instances on the same host listen on different ports and `Instance` is used to supply a static value for the dimension `plugin_instance`. If `Instance` was not specified, the value of `plugin_instance` reported by collectd would contain the combination of `Host` and `Port` as follows:

```
"plugin_instance" => "127.0.0.1:9100",
"plugin_instance" => "127.0.0.1:9101",
"plugin_instance" => "127.0.0.1:9102",
```
### USAGE

Sample of pre-built dashboard in SignalFx:

![](././img/dashboard_redis.png)

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
