# HAProxy

This directory consolidates all the metadata associated with the HAProxy collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd-haproxy).

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use the [collectd-haproxy](https://github.com/signalfx/collectd-haproxy) collectd plugin to collect metrics about HaProxy.

### REQUIREMENTS AND DEPENDENCIES

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| haproxy  | 1.5 or later |

### INSTALLATION

1. Download the [collectd-haproxy-plugin](https://github.com/signalfx/collectd-haproxy) git repo to `/usr/share/collectd/collectd-haproxy`
2. Download SignalFx's [sample configuration file](https://github.com/signalfx/integrations/tree/master/collectd-haproxy/10-haproxy.conf) for this plugin to `/etc/collectd/managed_config`.
3. Modify the sample configuration file as described in [Configuration](#configuration), below.
4. `SELINUX ONLY` Create a SELinux policy package using the supplied type enforcement file.  Enter the commands below to create and install the policy package.
    ```      
    $ cd /usr/share/collectd/collectd-haproxy/selinux
    $ checkmodule -M -m -o collectd-haproxy.mod collectd-haproxy.te
    checkmodule:  loading policy configuration from collectd-haproxy.te
    checkmodule:  policy configuration loaded
    checkmodule:  writing binary representation (version 17) to collectd-haproxy.mod
    $ semodule_package -o collectd-haproxy.pp -m collectd-haproxy.mod
    $ sudo semodule -i collectd-haproxy.pp
    $ sudo reboot
    ```

5. Restart collectd.


### CONFIGURATION

Using the example configuration file [10-haproxy.conf](https://github.com/signalfx/integrations/tree/master/collectd-haproxy/10-haproxy.conf) as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the HAProxy instance to be monitored.

| Configuration Option | Definition | Example Value |
| ---------------------|------------|---------------|
| Socket | Location of the HAProxy socket file. The default socket is `/var/run/haproxy.sock` | Socket "/var/run/haproxy.sock" |
| ProxyMonitor | A list of all the pxname(s) or svname(s) that you want to monitor | <ui><li>ProxyMonitor "http-in"</li><li>ProxyMonitor "server1"</li><li>ProxyMonitor "backend"</li></ui> |
| Interval | Interval between collectd to get HAProxy metrics. | 10 |
| EnhancedMetrics | Enable sending all metrics, not just the default metrics. Defaults to false| EnhancedMetrics 'True' |
| ExcludeMetric | Do not send a specific metric. Metric names can be found in the docs repo | ExcludeMetric 'response_1xx' |

The location of the HAProxy socket file is defined in the HAProxy config file, as in the following example:

```
global
    daemon
    stats socket /var/run/haproxy.sock
    stats timeout 2m
```

Note: it is possible to use a tcp socket for stats in HAProxy. Users will first need to define in their collectd-haproxy plugin config file the tcp address for the socket, for example `localhost:9000`, and then in the haproxy.cfg file change the stats socket to listen on the same address
```
global
    daemon
    stats socket localhost:9000
    stats timeout 2m
```

For a more restricted tcp socket, a backend server can be defined to listen to stats on localhost. A frontend proxy can use the backend server on a different port, with ACLs to restrict access. See below for example.

```
global
    daemon
    stats socket localhost:9000
    stats timeout 2m

backend stats-backend
    mode tcp
    server stats-localhost localhost:9000

frontend stats-frontend
    bind *:9001
    default_backend stats-backend
    acl ...
    acl ...
```


### METRICS
#### Default metrics
- **HAProxy Overview**
    - Connection Rate
    - Requests per Second
    - Idle Percent
    - Current Sessions
    - Sessions Rate
    - Top Servers Selected
    - Highest Bytes Out
    - Average Session Time
- **HAProxy Frontend**
    - Request Rate
    - Session Rate
    - Response 2xx, 4xx, 5xx
    - Request Errors
    - Denied Requests
    - Bytes Out
    - Bytes In
- **HAProxy Backend**
    - Current Queue Size
    - Average Response Time
    - Average Queue Time
    - Top Servers Selected
    - Response Errors
    - Server Retries and Redispatches
    - Connection Errors
    - Denied Responses

#### Enhanced Metrics

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs). Non-default metrics can be enabled in the plugin configuration file, by setting EnhancedMetrics to "True". Any metric can be excluded from being sent by adding ExcludeMetric "metric_name" in the plugin configuration file. Metric names are found in the [docs](./docs).


### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
