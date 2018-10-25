# ![](https://github.com/signalfx/integrations/blob/master/collectd-haproxy/img/integrations_haproxy.png) HAProxy

Metadata associated with the HAProxy collectd plugin can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-haproxy">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd-haproxy">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use the <a target="_blank" href="https://github.com/signalfx/collectd-haproxy">collectd-haproxy</a> collectd plugin to collect metrics about HaProxy.

### REQUIREMENTS AND DEPENDENCIES

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| haproxy  | 1.5 or later |

### INSTALLATION

**If you are using the new Smart Agent, see the docs for <a target="_blank" href="https://github.com/signalfx/signalfx-agent/tree/master/docs/monitors/collectd-haproxy.md">the collectd/haproxy monitor</a>
for more information.  The configuration documentation below may be helpful as
well, but consult the Smart Agent repo's docs for the exact schema.**


1. Download the <a target="_blank" href="https://github.com/signalfx/collectd-haproxy">collectd-haproxy-plugin</a> git repo to `/usr/share/collectd/collectd-haproxy`
2. Download SignalFx's <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd-haproxy/10-haproxy.conf">sample configuration file</a> for this plugin to `/etc/collectd/managed_config`.
3. Modify the sample configuration file as described in [Configuration](#configuration), below.
4. `SELINUX ONLY` Create a SELinux policy package using the supplied type enforcement file.  Enter the commands below to create and install the policy package.

        $ cd /usr/share/collectd/collectd-haproxy/selinux
        $ checkmodule -M -m -o collectd-haproxy.mod collectd-haproxy.te
        checkmodule:  loading policy configuration from collectd-haproxy.te
        checkmodule:  policy configuration loaded
        checkmodule:  writing binary representation (version 17) to collectd-haproxy.mod
        $ semodule_package -o collectd-haproxy.pp -m collectd-haproxy.mod
        $ sudo semodule -i collectd-haproxy.pp
        $ sudo reboot

5. Restart collectd.


### CONFIGURATION

Using the example configuration file <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd-haproxy/10-haproxy.conf">10-haproxy.conf</a> as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the HAProxy instance to be monitored.

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

### USAGE
#### Default metrics
- **HAProxy Overview**
    - Connection Rate - Total number of connections per second being made.
    - Requests per Second - Number of incoming requests per second.
    - Idle Percent - HAProxy runs on an event loop and waits for new events using poll(). Idle_pct is the ratio of polling time versus total time. Near 100% means load is low, near 0% means the load is very high.
    - Current Sessions - Current number of active sessions in the system. A session is an end-to-end connection.
    - Sessions Rate - Chart showing the rate at which sessions are being created.
    - Top Servers Selected - List of which servers are being selected the most by the load balancer algorithm.
    - Highest Bytes Out - List of which servers are outputting the most data.
    - Average Session Time - List of the average session time over the last 1024 requests
- **HAProxy Frontend**
    - Request Rate - The rate of requests being made to the frontend, useful to monitor spikes in traffic.
    - Session Rate - Number of sessions per second being created, also useful to monitor spikes in traffic.
    - Response 2xx, 4xx, 5xx - The ratio between 2xx and 4xx/5xx responses is ideally very low. Watch for spikes in 4xx or 5xx as they may show a misconfiguration or other potential errors.
    - Request Errors - Rate of error requests being made in the system. These may stem from early client termination, read errors from the client, client timeouts, or other various bad requests from the client.
    - Denied Requests - Rate of requests denied because of security concerns. This could be denied requests because they do not satisfy an ACL configuration, or some other deny.
    - Bytes Out - Number of bytes sent out.
    - Bytes In - Number of bytes sent in.
- **HAProxy Backend**
    - Current Queue Size - Number of items in the queued requests. If HAProxy hits the configured max number of connections, HAProxy will queue new incoming requests until a server becomes available.
    - Average Response Time - Lists average response time in seconds over the past 1024 requests. Backend must be using mode http, otherwise the metric will report 0.
    - Average Queue Time - The average time a request spends in the queue. This value should be low to keep the system latency low.
    - Top Servers Selected - List of which servers are being selected the most by the load balancer algorithm.
    - Response Errors - The backend error response rate. This metric can be correlated with denied responses and frontend requests to gain insight on potential errors.
    - Server Retries and Redispatches - Server retries occur when a server is not reached the first time. The request will be redispatched to another server if the retry limit is hit.
    - Connection Errors - The rate of connection errors includes both failed backend requests and general backend errors. Correlate with response errors and response codes to track down an issue.
    - Denied Responses - The rate of denied responses by the backend. Most denied responses will come from an ACL and can be correlated with 5xx responses.


### METRICS
#### Enhanced Metrics

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs). Non-default metrics can be enabled in the plugin configuration file, by setting EnhancedMetrics to "True". Any metric can be excluded from being sent by adding ExcludeMetric "metric_name" in the plugin configuration file. Metric names are found in the [docs](./docs).


### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
