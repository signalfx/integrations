# ![](https://github.com/signalfx/integrations/blob/master/collectd-nginx-plus/img/integrations_nginxplus.png) NGINX Plus

_This directory consolidates all the metadata associated with the NGINX Plus plugin for collectd. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd-nginx-plus)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This is the SignalFx NGINX Plus plugin. Follow these instructions to install the NGINX Plus plugin for collectd.

The [`niginx-plus-collectd`](https://github.com/signalfx/collectd-nginx-plus) plugin collects metrics about a single NGINX Plus instance,
using the `/status` endpoints exposed with the [ngx_http_status_module](http://nginx.org/en/docs/http/ngx_http_status_module.html).

#### FEATURES

##### Built-in dashboards

**Coming Soon**

### Installation

1. Download the [`niginx-plus-collectd`](https://github.com/signalfx/collectd-nginx-plus) project.

1. Run the following command to install the module’s dependencies using `pip`, replacing the example path with the download location of the `niginx-plus-collectd` project:

  ```
  sudo pip install -r install_requirements.txt
  ```

1. Download SignalFx’s [sample configuration file](https://github.com/signalfx/integrations/blob/master/collectd-nginx-plus/10-nginx-plus.conf) for this plugin to `/etc/collectd/managed_config`.

1. Modify the configuration file to provide values that make sense for your environment, as described in [Configuration](#configuration) below.

1. Restart collectd.

### Configuration

Using the example configuration file [10-nginx-plus.conf](https://github.com/signalfx/integrations/tree/master/collectd-nginx-plus/10-nginx-plus.conf) as a guide, provide values for the configuration options listed below that make sense for your environment.

| Configuration Option | Definition | Default Value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | ``/usr/share/collectd/niginx-plus-collectd/plugin` |
| StatusHost | IP address or DNS of the NGINX+ instance to retrieve status information from | `localhost` |
| StatusPort | Port the NGINX+ status endpoint can be reached at. | `8080` |
| DebugLogLevel | `true` to enable logging at DEBUG level. | `false` |
| Username | Username to use for username/password authentication. | None |
| Password | Password to use for username/password authentication. | None |
| Dimension | A single additional dimension decorating to each metric. There are two values, the first for the name,
the second for the value. | None |

Example addition to the collectd configuration:

```apache
LoadPlugin python

<Plugin python>
  ModulePath "/usr/share/collectd/collectd-nginx-plus/plugin"
  Import nginx_plus_collectd

  <Module nginx_plus_collectd>
    StatusHost "localhost"
    StatusPort "8080"
    DebugLogLevel true
    Username "user_1"
    Password "my_password"
    Dimension "extra_dimension_name_1" "extra_dimension_value_1"
    Dimension "extra_dimension_name_2" "extra_dimension_value_2"
  </Module>
</Plugin>
```

By default only a small subset of the available metrics are published by default. The remaining metrics can be enabled by opting-in to additional metric groups. See [Metrics](#metrics) for more details on each metric group
and how to enable them.

### USAGE

All metrics reported by the NGINX Plus collectd plugin will contain the following dimensions:

* `nginx.version` will contain the version number of the NGINX Plus instance being monitored
* `plugin` is always set to `nginx-plus`
* `plugin_instance` will contain the IP address of the NGINX Plus instance as given in the `/status/address` response.


### METRICS
By default only a subset (26) of the available metrics (87) are published by default. The remaining metrics can be enabled by opting-in to additional metric groups.

#### Default Metrics
The default metrics report the values necessary to power the default dashboards. This includes high-level connection
information, cache, server zone and upstreams metrics.

##### Metrics
* connections.accepted
* connections.dropped
* connections.idle
* connections.active
* ssl.handshakes.successful
* ssl.handshakes.failed
* ssl.handshakes.reuses
* requests.total
* requests.current
* server.zone.requests
* server.zone.responses.4xx
* server.zone.responses.5xx
* server.zone.responses.total
* server.zone.responses.received
* server.zone.bytes.received
* server.zone.bytes.sent
* caches.size
* caches.size.max
* upstreams.requests
* upstreams.responses.4xx
* upstreams.responses.5xx
* upstreams.responses.total
* upstreams.downtime
* upstreams.response.time
* upstreams.bytes.received
* upstreams.bytes.sent

#### Server Zone Metrics
Server Zone metrics are emitted for each server in each [status zone](http://nginx.org/en/docs/http/ngx_http_status_module.html#status_zone).
To include these metrics, add `ServerZone true` to the plugin configuration, e.g.
```apache
  <Module nginx_plus_collectd>
    StatusHost "localhost"
    StatusPort "8080"
    ServerZone true
  </Module>
```
##### Metrics
* server.zone.processing
* server.zone.discarded
* server.zone.responses.1xx
* server.zone.responses.2xx
* server.zone.responses.3xx

#### Memory Zone Metrics
Memory Zone metrics are emitted for each shared memory zone that uses a slab allocator.
To include these metrics, add `MemoryZone true` to the plugin configuration, e.g.
```apache
  <Module nginx_plus_collectd>
    StatusHost "localhost"
    StatusPort "8080"
    MemoryZone true
  </Module>
```
##### Metrics
* zone.pages.used
* zone.pages.free

#### Upstream Metrics
Upstream metrics are emitted for each server in each http-context [upstream group](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#upstream).
To include these metrics, add `Upstream true` to the plugin configuration, e.g.
```apache
  <Module nginx_plus_collectd>
    StatusHost "localhost"
    StatusPort "8080"
    Upstream true
  </Module>
```
##### Metrics
* upstreams.active
* upstreams.responses.1xx
* upstreams.responses.2xx
* upstreams.responses.3xx
* upstreams.fails
* upstreams.unavailable
* upstreams.health.checks.checks
* upstreams.health.checks.fails
* upstreams.health.checks.unhealthy
* upstreams.header.time
* upstreams.keepalive
* upstreams.zombies

#### Cache Metrics
Cache metrics are emitted for each cache, e.g. [proxy cache](http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_cache_path).
To include these metrics, add `Cache true` to the plugin configuration, e.g.
```apache
  <Module nginx_plus_collectd>
    StatusHost "localhost"
    StatusPort "8080"
    Cache true
  </Module>
```
##### Metrics
* caches.hit.responses
* caches.miss.responses
* caches.stale.responses
* caches.updating.responses
* caches.revalidated.responses
* caches.expired.responses
* caches.bypass.responses
* caches.hit.bytes
* caches.miss.bytes
* caches.stale.bytes
* caches.updating.bytes
* caches.revalidated.bytes
* caches.expired.bytes
* caches.bypass.bytes
* caches.miss.responses.written
* caches.expired.responses.written
* caches.bypass.responses.written
* caches.miss.bytes.written
* caches.expired.bytes.written
* caches.bypass.bytes.written

#### Stream Server Zone Metrics
Stream Server Zone metrics are emitted for each server in each stream-context [status zone](http://nginx.org/en/docs/http/ngx_http_status_module.html#status_zone).
To include these metrics, add `StreamServerZone true` to the plugin configuration, e.g.
```apache
  <Module nginx_plus_collectd>
    StatusHost "localhost"
    StatusPort "8080"
    StreamServerZone true
  </Module>
```
##### Metrics
* stream.server.zone.connections
* stream.server.zone.processing
* stream.server.zone.sessions.2xx
* stream.server.zone.sessions.4xx
* stream.server.zone.sessions.5xx
* stream.server.zone.received
* stream.server.zone.sent
* stream.server.zone.discarded

#### Stream Upstream Metrics
Stream Upstream metrics are emitted for each server in each stream-context [upstream group](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#upstream).
To include these metrics, add `StreamUpstream true` to the plugin configuration, e.g.
```apache
  <Module nginx_plus_collectd>
    StatusHost "localhost"
    StatusPort "8080"
    StreamUpstream true
  </Module>
```
##### Metrics
* stream.upstreams.connections
* stream.upstreams.active
* stream.upstreams.connections.max
* stream.upstreams.bytes.sent
* stream.upstreams.bytes.received
* stream.upstreams.fails
* stream.upstreams.unavailable
* stream.upstreams.health.checks.checks
* stream.upstreams.health.checks.fails
* stream.upstreams.health.checks.unhealthy
* stream.upstreams.response.time
* stream.upstreams.downtime
* stream.upstreams.bytes.received
* stream.upstreams.bytes.sent
* stream.upstreams.zombies

### Processes Metrics
Process metrics only include the default dimensions.
To include these metrics, add `Processes true` to the plugin configuration, e.g.
```apache
  <Module nginx_plus_collectd>
    StatusHost "localhost"
    StatusPort "8080"
    Processes true
  </Module>
```
##### Metrics
* processes.respawned

For full documentation of the metrics and dimensions emitted by this plugin, see the `docs` directory in this repository.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
