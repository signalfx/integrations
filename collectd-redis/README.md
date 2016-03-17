---
title: Redis collectd Plugin
brief: Redis plugin for collectd.
---

# ![](https://github.com/signalfx/integrations/blob/master/collectd-redis/img/integrations_redis.png) Redis collectd Plugin

_This is a directory consolidate all the metadata associated with the Redis collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/redis.c)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Redis):

> The Redis plugin connects to one or more instances of Redis, a key-value store, and collects usage information using the `credis` library.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd   |  5.0+  |
| credis (C library implementing the redis protocol)| 0.2.3+ |
| redis | 2.8+ |

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Redis):

> The credis library is lagging support for current redis, and requires at least the following patch:

> ```
--- ../credis_2/credis-0.2.3/credis.c   2010-08-27 01:57:25.000000000 -0700
+++ ../credis-0.2.3/credis.c    2014-01-28 22:39:42.000000000 -0800
@@ -754,7 +754,7 @@
    * first 1.1.0 release(?), e.g. stable releases 1.02 and 1.2.6 */
   if (cr_sendfandreceive(rhnd, CR_BULK, "INFO\r\n") == 0) {
     int items = sscanf(rhnd->reply.bulk,
-                       "redis_version:%d.%d.%d\r\n",
+                       "# Server\r\nredis_version:%d.%d.%d\r\n",
                        &(rhnd->version.major),
                        &(rhnd->version.minor),
                        &(rhnd->version.patch));
```

> * see brief notes on [configuring this under ubuntu 14.04](https://github.com/collectd/collectd/issues/755#issuecomment-57948623)

> * the following tips are useful when testing and troubleshooting
* use redis-cli ping to ensure you can connect to redis itself.
* use credis-test to see if your compiled credis is able to talk to redis itself. If this fails, the collectd plugin will also not work.
* use redis-cli monitor & to see what redis is receiving and sending itself.
* use sudo ngrep -texd lo port 6379 to see raw traffic goin to/from redis on the loopback adapter. You may need to use eth0 or similar depending on your setup. This may show up more information on why certain credis commands do not get through to redis itself.
* Finally, users comfortable with compiling their own versions from scratch may want to follow the hiredis alternative mentioned in [current issues](https://github.com/collectd/collectd/issues?q=hiredis+)

### INSTALLATION

This plugin is included with [SignalFx collectd](https://github.com/signalfx/integrations/tree/master/collectd).

### CONFIGURATION

From the [collectd wiki](https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_redis):

> The Redis plugin connects to one or more Redis servers and gathers information about each server's state. For each server there is a Node block which configures the connection parameters for this node.
> ```
  <Plugin redis>
    <Node "example">
        Host "localhost"
        Port "6379"
        Timeout 2000
        <Query "LLEN myqueue">
          Type "queue_length"
          Instance "myqueue"
        <Query>
    </Node>
  </Plugin>
```

> The information shown in the synopsis above is the _default configuration_ which is used by the plugin if no configuration is present.

| Configuration Option | Type | Definition |
|----------------------|------|------------|
| Node | Nodename | The Node block identifies a new Redis node, that is a new Redis instance running in an specified host and port. The name for node is a canonical identifier which is used as plugin instance. It is limited to 64 characters in length.|
| Host | Hostname |The Host option is the hostname or IP-address where the Redis instance is running on.|
|Port |Port| The Port option is the TCP port on which the Redis instance accepts connections. Either a service name of a port number may be given. Please note that numerical port numbers must be given as a string, too.|
|Password |Password|Use Password to authenticate when connecting to Redis.|
|Timeout |Milliseconds|The Timeout option set the socket timeout for node response. Since the Redis read function is blocking, you should keep this value as low as possible. Keep in mind that the sum of all Timeout values for all Nodes should be lower than Interval defined globally.|
|Query |Querystring|The Query block identifies a query to execute against the redis server. There may be an arbitrary number of queries to execute.|
|Type |Collectd type|Within a query definition, a valid collectd type to use as when submitting the result of the query. When not supplied, will default to gauge.|
|Instance |Type instance|Within a query definition, an optional type instance to use when submitting the result of the query. When not supplied will default to the escaped command, up to 64 chars.|

### USAGE

>This section contains information about how best to monitor the software in question, using the data from this plugin. In this section, the plugin author shares experience and expertise with the software to be monitored, for the benefit of users of the plugin. This section includes:
>
>- Important conditions to watch out for in the software
>- Common failure modes, and the values of metrics that will allow the user to spot them
>- Chart images demonstrating each important condition or failure mode

This plugin is an example that emits values on its own, and does not connect to software. It emits a repeating sine wave in the metric gauge.sine. The metric should look like this:

![Example chart showing gauge.sine](http://fixme)

The following conditions may be cause for concern:

*You see a straight line instead of a curve.*

This may indicate a period of missing data points. In the example chart shown above, some data points are missing between 16:40 and 16:41, and SignalFx is interpolating a straight line through the gap.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

License for this plugin can be found [in the header of the plugin](https://github.com/signalfx/collectd/blob/master/src/redis.c)
