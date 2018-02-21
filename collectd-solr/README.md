# ![](./img/integrations_solr.png) solr

Metadata associated with the solr plugin for collectd can be found [here](https://github.com/signalfx/integrations/tree/release/collectd-solr). The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd-solr).

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This is the SignalFx solr plugin. Follow these instructions to install the solr plugin for collectd.

The [solr-collectd](https://github.com/signalfx/collectd-solr) plugin collects metrics from solr instances hitting these endpoints: [statistics](https://lucene.apache.org/solr/guide/6_6/performance-statistics-reference.html) (default metrics)  and [metrics](https://lucene.apache.org/solr/guide/6_6/metrics-reporting.html) (optional metrics).

#### FEATURES

#### Built-in dashboards

- **solr CLUSTER**: Provides a high-level overview of metrics for a single solr cluster.

  [<img src='./img/solr-cluster-dashboard-top.png' width=200px>](./img/solr-cluster-dashboard-top.png)

  [<img src='./img/solr-cluster-dashboard-bottom.png' width=200px>](./img/solr-cluster-dashboard-bottom.png)  

- **SOLR NODE**: Provides metrics from a single solr instance/node.

  [<img src='./img/solr-node-dashboard.png' width=200px>](./img/solr-node-dashboard.png)

- **solr NODES**: Provides metrics from hosts on a particular host.

  [<img src='./img/solr-nodes-dashboard.png' width=200px>](./img/solr-nodes-dashboard.png)


### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| python | 2.6 or later |
| solr | 6.6 or later |
| Python plugin for collectd | (included with [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd)) |

### INSTALLATION

1. Download [collectd-solr](https://github.com/signalfx/collectd-solr). Place the `solr_collectd.py` file in `/usr/share/collectd/collectd-solr`

2. Modify the [sample configuration file](https://github.com/signalfx/integrations/tree/release/collectd-solr/20-solr.conf) for this plugin to `/etc/collectd/managed_config`

3. Modify the sample configuration file as described in [Configuration](#configuration), below

4. Install the Python requirements with sudo ```pip install -r requirements.txt```

5. Restart collectd


### CONFIGURATION

Using the example configuration file [20-solr.conf](https://github.com/signalfx/integrations/tree/release/collectd-solr/20-solr.conf) as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the solr nodes

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | "/usr/share/collectd/collectd-solr/" |
| Host | Host name of the solr node | "localhost" |
| Port | Port at which the node can be reached | "8983" |
| Cluster | Name of this solr cluster. | "demo" |
| EnhancedMetrics | Boolean to indicate whether stats from `/metrics` are needed | "false" |
| IncludeMetric | Metric name from the `/admin/metrics` endpoint to include(valid when EnhancedMetrics is "false") | "" |
| ExcludeMetric | Metric name from the `/admin/metrics` endpoint to exclude(valid when EnhancedMetrics is "true") | "" |
| Dimension | Space separated key-value pair for a user-defined dimension | dimension\_name dimension\_value |
| Interval | Number of seconds between calls to solr API. | 10 |
| ssl\_keyfile | Path to the keyfile | "path/to/file" |
| ssl\_certificate | Path to the certificate | "path/to/file" |
| ssl\_ca\_certs | Path to the ca file | "path/to/file" |

Example configuration:

```apache
LoadPlugin python
<Plugin python>
  ModulePath "/usr/share/collectd/collectd-solr/"

  Import solr_plugin
  <Module solr_plugin>
    Host "localhost"
    Port "8983"
    Interval 10
    Cluster "prod"
    Dimension dimension_name dimension_value
    EnhancedMetrics False
    IncludeMetric metric_name_from_metrics_endpoint
    ssl_keyfile "/Users/as001/work/play/solr/solr-ca/solr-ca/private/solr-client.key"
    ssl_certificate "/Users/as001/work/play/solr/solr-ca/solr-ca/certs/solr-client.crt"
    ssl_ca_certs "/Users/as001/work/play/solr/solr-ca/solr-ca/certs/ca.crt"
  </Module>
</Plugin>
```

The plugin can be configured to collect metrics from multiple nodes in the following manner.

```apache
LoadPlugin python

<Plugin python>
  ModulePath "/usr/share/collectd/collectd-solr/"
  Import solr_plugin
  <Module solr_plugin>
    Host "localhost"
    Port "8983"
    Interval 10
    Cluster "prod"
  </Module>
  <Module solr_plugin>
    Host "localhost"
    Port "7574"
    Interval 10
    Cluster "prod"
    IncludeMetric "metrics.solr.node.ADMIN./admin/zookeeper.serverErrors.meanRate"
    IncludeMetric "metrics.solr.jetty.org.eclipse.jetty.server.handler.DefaultHandler.post-requests.count"
  </Module>
  <Module solr_plugin>
    Host "localhost"
    Port "8984"
    Interval 10
    Cluster "test"
  </Module>
</Plugin>
```

### USAGE

#### Interpreting Built-in dashboards

- **SOLR CLUSTER**:

  - **Number of Collections**: Shows the number of collections in the cluster.

    [<img src='./img/chart-solr-cluster-number-collections.png' width=200px>](./img/chart-solr-cluster-number-collections.png)

  - **Number of Nodes**: Shows the number of nodes in the cluster.

    [<img src='./img/chart-solr-cluster-number-nodes.png' width=200px>](./img/chart-solr-cluster-number-nodes.png)

  - **Number of Nodes**: Shows the total number of cores on all the collections of the cluster put together. Gives an overview of documents distributed over the cores on the cluster as a whole.

    [<img src='./img/chart-solr-cluster-cores-collection.png' width=200px>](./img/chart-solr-cluster-cores-collection.png)

  - **Followers with Max Number of Watchers**: Get an overview of the nodes that are being requested for watching. Watching is memory intensive. The list gives information about the nodes (```host:port``` information) and the corresponding states.

    [<img src='./img/chart-solr-cluster-Max-Watchers.png' width=200px>](./img/chart-solr-cluster-Max-Watchers.png)

  - **Top Current Latency**: Gives an overview of the followers (```host:port```) with max current latency with the leader. Since raft relies on log replication throughout all the nodes, this is helps in flushing out followers that have max latency.

    [<img src='./img/chart-solr-cluster-top-latency.png' width=200px>](./img/chart-solr-cluster-top-latency.png)

  - **Total RPC Requests (successful/failed)**: A stacked chart that shows successful (in green) and failed (in red) RPC requests per second across all the followers. Leader sends RPC requests and followers receive.

    [<img src='./img/chart-solr-cluster-total-rpcs.png' width=200px>](./img/chart-solr-cluster-total-rpcs.png)

  - **Per node Failed RPCs**: A stacked chart showing failed RPC requests per second on a per follower basis. On comparing this chart with one above, followers that cause more failures can be flushed out.

    [<img src='./img/chart-solr-cluster-node-rpc-failure.png' width=200px>](./img/chart-solr-cluster-node-rpc-failure.png)

  - **Top RPC Requests**: Followers with top RPC requests, both successful and failed.

    [<img src='./img/chart-solr-cluster-top-rpcs.png' width=200px>](./img/chart-solr-cluster-top-rpcs.png)

  - **Store operations (successful/failed)**: This includes the following charts: Creates, Sets, Updates, Deletes, Compare-and-Swaps and Compare-and-Deletes. These charts are stacked charts that show successful operations (in green) and failed operations (in red) per second. This gives an idea of the ratio between success and failure for each operation type.

    [<img src='./img/chart-solr-cluster-creates.png' width=200px>](./img/chart-solr-cluster-creates.png)
    [<img src='./img/chart-solr-cluster-sets.png' width=200px>](./img/chart-solr-cluster-sets.png)
    [<img src='./img/chart-solr-cluster-updates.png' width=200px>](./img/chart-solr-cluster-updates.png)
    [<img src='./img/chart-solr-cluster-deletes.png' width=200px>](./img/chart-solr-cluster-deletes.png)
    [<img src='./img/chart-solr-cluster-cas.png' width=200px>](./img/chart-solr-cluster-cas.png)
    [<img src='./img/chart-solr-cluster-cad.png' width=200px>](./img/chart-solr-cluster-cad.png)

  - **Receive Packet Rate**: Stacked chart of the packets received per second for each follower. At given point in time, followers receive packets from the leader (leader sends information as part of log replication).

    [<img src='./img/chart-solr-cluster-packet-recv.png' width=200px>](./img/chart-solr-cluster-packet-recv.png)

  - **Receive Append Requests**: Stacked chart of the append requests received per second for each follower. At given point in time, followers receive append requests from the leader (leader sends information as part of log replication).

    [<img src='./img/chart-solr-cluster-append-recv.png' width=200px>](./img/chart-solr-cluster-append-recv.png)

  - **Send Packet Rate**: Chart for the packets sent per second for the leader. At given point in time, only leader sends packets. In the ideal world, every packet sent by the leader should be received by one of the followers. Comparing this chart with **Receive Packet Rate** would explain if packets are not received by followers (or an individual follower). Latency can also be observed through these charts.

    [<img src='./img/chart-solr-cluster-packet-sent.png' width=200px>](./img/chart-solr-cluster-packet-sent.png)

  - **Send Append Requests**: Chart for the append requests sent per second for the leader. At given point in time, only leader sends append requests. In the ideal world, all append requests sent by the leader should be received by one of the followers. Comparing this chart with **Receive Append Requests** would explain if append requests are not received by followers (or an individual follower). Latency can also be observed through these charts.

    [<img src='./img/chart-solr-cluster-append-sent.png' width=200px>](./img/chart-solr-cluster-append-sent.png)

- **solr INSTANCE**:

  - **Number of Watchers**: Shows the number of watchers on this particular instance. Watching is memory intensive and might explain high memory utilization.

    [<img src='./img/chart-solr-instance-number-watchers.png' width=200px>](./img/chart-solr-instance-number-watchers.png)

  - **Expire Rate**: The number of keys and directories that expire per second. This is common to the distributed key-value store. However, when a node leaves the cluster, this metric becomes instance specific.

    [<img src='./img/chart-solr-instance-expire-rate.png' width=200px>](./img/chart-solr-instance-expire-rate.png)

  - **Gets (successful/failed)**: A stacked chart that shows successful gets (in green) and failed gets (in red) per second. This gives insight to the ratio between successful and failed get requests per second for the instance. It is possible that a high fail count for gets is because of a high expire rate.

    [<img src='./img/chart-solr-instance-gets.png' width=200px>](./img/chart-solr-instance-gets.png)

  - **Receive / Send Bandwidth Rate** A line graph showing both, sent (in blue) and received (in green) bandwidth rate for the instance. Followers receive and Leader sends.

    [<img src='./img/chart-solr-instance-bandwidth.png' width=200px>](./img/chart-solr-instance-bandwidth.png)

  - **Receive / Send Append Requests** A line graph showing both, sent (in blue) and received (in green) append requests per second for the instance. Followers receive and Leader sends.

    [<img src='./img/chart-solr-instance-appends.png' width=200px>](./img/chart-solr-instance-appends.png)

- **solr INSTANCES**: Provides metrics from hosts on a particular host.

  - **Number of instances**: The total number of solr isntances running on the host, group by type (follower/leader).

    [<img src='./img/chart-solr-instances-number-instances.png' width=200px>](./img/chart-solr-instances-number-instances.png)

  - **Instances by Number of Watchers**: A line graph that shows number of watchers on each of the instances on the host. Instances with more number of watchers consume more memory.

    [<img src='./img/chart-solr-instances-number-watchers.png' width=200px>](./img/chart-solr-instances-number-watchers.png)

  - **Instances with Most Number of Wacthers**: Shows the instances with most number of watchers. Watching is memory intensive.

    [<img src='./img/chart-solr-instances-most-watchers.png' width=200px>](./img/chart-solr-instances-most-watchers.png)

  - **Packets Exchange Trend**: A stacked chart showing packets sent (in blue) and received (in green) across all instances on the host. Gives an idea of bandwidth usage.

    [<img src='./img/chart-solr-instances-packets.png' width=200px>](./img/chart-solr-instances-packets.png)

  - **Bandwidth Trend Rate**: A stacked chart showing send bandwidth (in blue) and receive bandwidth (in green) rates across all instances on the host. Gives an idea of bandwidth usage and should shows similar trends as the above chart.

    [<img src='./img/chart-solr-instances-bandwidth.png' width=200px>](./img/chart-solr-instances-bandwidth.png)

  - **Top Bandwidth Rate**: Gives a list of the instances that consume max bandwidth, both for sending and receiving put together.

    [<img src='./img/chart-solr-instances-top-bandwidth.png' width=200px>](./img/chart-solr-instances-top-bandwidth.png)

  - **Gets Successful Trend**: A stacked chart showing the number of successful get operations per second for each of the instances running on the host.

    [<img src='./img/chart-solr-instances-gets-success.png' width=200px>](./img/chart-solr-instances-gets-success.png)

  - **Gets Failed Trend**: A stack chart showing the number of failed get operations per second for each of the instances running on the host. Compare with above chart to analyze the success ratio.

    [<img src='./img/chart-solr-instances-gets-fail.png' width=200px>](./img/chart-solr-instances-gets-fail.png)

  - **Top Gets per second** A list of the instances on the host that perform the max number of gets per second, both successful and failed gets put together.

    [<img src='./img/chart-solr-instances-gets-top.png' width=200px>](./img/chart-solr-instances-gets-top.png)

  - **Expire Rate Trend**: A line chart showing the rate of expiry of keys/directories for all the instances on host.

  [<img src='./img/chart-solr-instances-expire-trend.png' width=200px>](./img/chart-solr-instances-expire-trend.png)

  - **Top Expire Rate**: A list of instances with top expire rates. Can be used to analyze if gets fail due to a high expiry rate.

    [<img src='./img/chart-solr-instances-top-expire.png' width=200px>](./img/chart-solr-instances-top-expire.png)

All metrics reported by the solr collectd plugin will contain the following dimensions by default:

* `state`, whether the node is a follower or a leader
* `cluster`, human readable cluster name used to group by nodes by cluster
* `follower`, metrics from the leader endpoint will have this dimension to group by follower

A few other details:

* `plugin` is always set to `solr`
* `plugin_instance` will contain the IP address and the port of the node given in the configuration
* To add metrics from the `/metrics` endpoint, use the configuration options mentioned in [configuration](#configuration). If metrics are being included individually, make sure to give names that are valid. For example, `solr_debugging_mvcc_slow_watcher_total` or `solr_network_peer_sent_bytes_total`


### METRICS
By default, metrics about a node, leader and store are provided. For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs). Metrics from `/metrics` endpoint can be activated through the configuration file. Note, that SignalFx does not support `histogram` and `summary` metric types (hence, metrics of these will be skipped if provided in the configuration). See [usage](#usage) for details.


#### Metric naming
`<metric type>.solr.<endpoint name>.<name of metric>`. This is the format of default metric names reported by the plugin. Optional metrics are named as available from the `/metrics` endpoint with `_` replaced by `.`.


### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
