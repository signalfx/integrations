# ![](./img/integrations_etcd.png) etcd

_This directory consolidates all the metadata associated with the etcd plugin for collectd. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd-etcd)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This is the SignalFx etcd plugin. Follow these instructions to install the etcd plugin for collectd.

The [`etcd-collectd`](https://github.com/signalfx/collectd-etcd) plugin collects metrics from etcd instances hitting these endpoints: [statistics](https://coreos.com/etcd/docs/latest/v2/api.html#statistics) (default metrics)  and [metrics](https://coreos.com/etcd/docs/latest/v2/metrics.html) (optional metrics).

#### FEATURES

#### Built-in dashboards

- **ETCD CLUSTER**: Provides a high-level overview of metrics for a single etcd cluster.

  [<img src='./img/etcd_member.png' width=200px>](./img/etcd_cluster.png)

- **ETCD INSTANCE**: Provides metrics from a single etcd instance.

  [<img src='./img/etcd_leader.png' width=200px>](./img/etcd_instance.png)  

- **ETCD INSTANCES**: Provides metrics from hosts on a particular host.

  [<img src='./img/etcd_store.png' width=200px>](./img/etcd_instacnes.png)


### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| python | 2.6 or later |
| etcd | 2.0.8 or later |
| Python plugin for collectd | (included with [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd)) |

### INSTALLATION

1. Download [collectd-etcd](https://github.com/signalfx/collectd-etcd). Place the `etcd_plugin.py` file in `/usr/share/collectd/collectd-etcd`.

2. Modify the [sample configuration file](./10-etcd.conf) for this plugin to `/etc/collectd/managed_config`.

3. Modify the sample configuration file as described in [Configuration](#configuration), below.

4. Restart collectd.


### CONFIGURATION

Using the example configuration file [10-etcd.conf](./10-etcd.conf) as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the etcd members

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | "/usr/share/collectd/collectd-etcd/" |
| Host | Define the host name of the etcd member | "localhost" |
| Port | Define the port at which the member can be reached | "2379" |
| Cluster | Name of this etcd cluster. | "1" |
| EnhancedMetrics | Takes a boolean indicated whether stats from ```/metrics``` are needed | "false" |
| IncludeMetric | Takes a metric name from the ```/metric``` endpoint that has to included | metric_name_from_metrics_endpoint |
| ExcludeMetric | Takes a metric name from the ```/metric``` endpoint that has to excluded | metric_name_from_metrics_endpoint |
| Dimension | Takes space separated key-value pair for a user-defined dimension | dimension_name dimension_value |
| Interval | Number of seconds between calls to etcd API. | 10 |
| ssl_keyfile | Path to the keyfile | path to file |
| ssl_certificate | Path to the certificate | path to file |
| ssl_ca_certs | Path to the ca file | path to file |
| ssl_cert_validation | Takes a boolean to enable cert validation | "false" |

Example configuration:

```apache
LoadPlugin python
<Plugin python>
  ModulePath "/usr/share/collectd/collectd-etcd/"

  Import etcd_plugin
  <Module etcd_plugin>
    Host "localhost"
    Port "2379"
    Interval 10
    Cluster "1"
    Dimension dimension_name dimension_value
    EnhancedMetrics False
    IncludeMetric metric_name_from_metrics_endpoint
    ssl_keyfile "/Users/as001/work/play/etcd/etcd-ca/etcd-ca/private/etcd-client.key"
    ssl_certificate "/Users/as001/work/play/etcd/etcd-ca/etcd-ca/certs/etcd-client.crt"
    ssl_ca_certs "/Users/as001/work/play/etcd/etcd-ca/etcd-ca/certs/ca.crt"
    ssl_cert_validation True
  </Module>
</Plugin>
```

The plugin can be configured to collect metrics from multiple instances in the following manner.

```apache
LoadPlugin python

<Plugin python>
  ModulePath "/usr/share/collectd/collectd-etcd/"
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

### USAGE

#### Built-in dashboards

- **ETCD CLUSTER**: Below is a brief description for each of the charts on this dashboard.

  - **Number of Followers**: Shows the number of followers in the cluster. A cluster that is expected to have 2n + 1 members, can tolerate failure of n members. By virtue of raft consensus algorithm, a cluster should have at least 3 members

  - **Number of Watchers**: Shows the total number of watchers on all the members of the cluster put together. Gives an overview of memory consumption by the watchers on the cluster as a whole

  - **Top Watchers**: Get an overview of the members that are being requested for watching. Watching is consumes memory

  - **Top Current Latency**: Gives an overview of the followers with max current latency with the leader. Since raft relies on log replication throughout all the members, this is helps in flushing out followers that logo_large

  - **Total RPC Requests (successful/failed)**: A stacked chart that shows successful (in green) and failed (in red) RPC requests per second across all the followers. Leader sends RPC requests and followers receive

  - **Per Member Failed RPCs**: A stacked chart showing failed RPC requests per second on a per follower basis. On comparing this chart with one above, followers that cause more failures can be flushed out

  - **Top RPC Requests**: Followers with top RPC requests, both successful and failed

  - **Store operations (successful/failed)**: This includes the next 6 charts: Creates, Sets, Updates, Deletes, Compare-and-Swaps and Compare-and-Deletes. These charts are stacked charts that show successful operations (in green) and failed operations (in red) per second. This gives an idea of the ratio between success and failure

  - **Receive Packet Rate**: Stacked chart of the packets received per second for each follower. At given point in time, followers receive packets from the leader (leader sends information as part of log replication)

  - **Receive Append Requests**: Stacked chart of the append requests received per second for each follower. At given point in time, followers receive append requests from the leader (leader sends information as part of log replication)

  - **Send Packet Rate**: Chart for the packets sent per second for the leader. At given point in time, only leader sends packets. In the ideal world, every packet sent by the leader should be received by one of the followers. Comparing this chart with **Receive Packet Rate** would explain if packets are not received by followers (or an individual follower). Latency can also be observed through these charts

  - **Send Append Requests**: Chart for the append requests sent per second for the leader. At given point in time, only leader sends append requests. In the ideal world, all append requests sent by the leader should be received by one of the followers. Comparing this chart with **Receive Append Requests** would explain if append requests are not received by followers (or an individual follower). Latency can also be observed through these charts

- **ETCD INSTANCE**: Provides metrics from a single etcd instance.

- **ETCD INSTANCES**: Provides metrics from hosts on a particular host.


All metrics reported by the etcd collectd plugin will contain the following dimensions by default:

* `state`, whether the member is a follower or a leader
* `cluster`, human readable cluster name used to group by members by cluster
* `follower`, metrics from the leader endpoint will have this dimension to group by follower

A few other details:

* `plugin` is always set to `etcd`
* `plugin_instance` will contain the IP address and the port of the member given in the configuration
* To add metrics from the ```/metrics``` endpoint, use the configuration options mentioned in [configuration](#configuration). If metrics are being included individually, make sure to give names that are valid. For example, ```etcd_debugging_mvcc_slow_watcher_total``` or ```etcd_network_peer_sent_bytes_total```


### METRICS
By default, metrics about a member, leader and store are provided. Click [here](./docs) for details. Metrics from ```/metrics``` endpoint can be activated through the configuration file. Note, that SignalFx does not support `histogram` and `summary` metric types (hence, metrics of these will be skipped if provided in the configuration). See [usage](#usage) for details.


#### Metric naming
`<metric type>.etcd.<endpoint name>.<name of metric>`. This is the format of default metric names reported by the plugin. Optional metrics are named as available from the `/metrics` endpoint with `_` replaced by `.`.


### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
