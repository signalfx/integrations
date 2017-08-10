#![](https://github.com/signalfx/integrations/blob/master/collectd-etcd/img/integrations_etcd.png) etcd

_This directory consolidates all the metadata associated with the etcd plugin for collectd. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd-etcd)_

- [Description](#description)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This is the SignalFx etcd plugin. Follow these instructions to install the etcd plugin for collectd.

The [`etcd-collectd`](https://github.com/signalfx/collectd-etcd) plugin collects metrics from etcd members from the three [statistics](https://coreos.com/etcd/docs/latest/v2/api.html#statistics) endpoints and the [metric](https://coreos.com/etcd/docs/latest/v2/metrics.html).

#### FEATURES

##### Built-in dashboards

- **etcd Member**: Provides a high-level overview of metrics for a single etcd member.

  [<img src='./img/etcd_member.png' width=200px>](./img/etcd_member.png)

- **etcd Leader**: Provides metrics from the current leader of the cluster.

  [<img src='./img/etcd_leader.png' width=200px>](./img/etcd_leader.png)  

- **etcd Store**: Provides metrics that are specific to a single cluster.

  [<img src='./img/etcd_store.png' width=200px>](./img/etcd_store.png)

### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| python | 2.7 or later |
| etcd | 2.0.8 or later |
| Python plugin for collectd | (included with [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd)) |


### INSTALLATION

1. Download the [collectd-etcd Python module](https://github.com/signalfx/collectd-etcd).

1. Download SignalFx's [sample configuration file](https://github.com/signalfx/integrations/blob/master/collectd-etcd/10-etcd.conf) for this plugin to `/etc/collectd/managed_config`.

1. Modify the sample configuration file as described in [Configuration](#configuration), below.

1. Restart collectd.

### CONFIGURATION

Using the example configuration file [10-etcd.conf](https://github.com/signalfx/integrations/tree/master/collectd-etcd/10-etcd.conf) as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the etcd members

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | "/opt/collectd-etcd" |
| Host | Define the host name of the etcd member | "localhost" |
| Port | Define the port at which the member can be reached | "2379" |
| Cluster | Name of this etcd cluster. | "prod" |
| EnhancedMetrics | Takes a boolean indicated whether stats from ```/metrics``` are needed | "false" |
| IncludeMetric | Takes a metric name from the ```/metric``` endpoint that has to included |  |
| ExcludeMetric | Takes a metric name from the ```/metric``` endpoint that has to excluded |  |
| Dimension | Takes space separated key-value pair for a user-defined dimension | "dimension_name dimension_value" |
| Interval | Number of seconds between calls to etcd API. | 10 |

Example configuration:

```apache
LoadPlugin python

<Plugin python>
  ModulePath "/usr/share/collectd/collectd-etcd/plugin"
  Import etcd_plugin
  <Module etcd_plugin>
    Host "localhost"
    Port "2379"
    Interval 10
    Cluster "prod"
  </Module>
  <Module etcd_plugin>
    Host "localhost"
    Port "22379"
    Interval 10
    Cluster "prod"
    IncludeMetric "etcd_debugging_mvcc_slow_watcher_total"
    IncludeMetric "etcd_debugging_store_reads_total"
    IncludeMetric "etcd_server_has_leader"
    IncludeMetric "etcd_network_peer_sent_bytes_total"
  </Module>
  <Module etcd_plugin>
    Host "localhost"
    Port "32379"
    Interval 10
    Cluster "test"
  </Module>
</Plugin>
```

### METRICS
By default, metrics about a member, leader and store are provided. Click [here](./docs) for details. Metrics from ```/metrics``` endpoint can be activated through the configuration file. See [usage](#usage) for details.

#### Metric naming
`<metric type>.etcd.<endpoint name>.<name of metric>`. This is the format of default metric names reported by the plugin. The optional metrics are named the as available from the `/metrics` endpoint with `_` replaced by `.`.

### USAGE
All metrics reported by the etcd collectd plugin will contain the following dimensions by default:

* `state`, whether the member is a follower or a leader
* `cluster`, human readable cluster name used to group by members by cluster
* `follower`, metrics from the leader endpoint will have this dimension to group by follower

A few other details:

* `plugin` is always set to `etcd`
* `plugin_instance` will contain the IP address and the port of the member given in the configuration
* To add metrics from the ```/metrics``` endpoint, use the configuration options mentioned in [configuration](#configuration). If metrics are being included individually, make sure to give names that are valid. For example, ```etcd_debugging_mvcc_slow_watcher_total``` or ```etcd_network_peer_sent_bytes_total```



### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
