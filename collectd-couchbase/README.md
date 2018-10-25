# ![](https://github.com/signalfx/integrations/blob/master/collectd-couchbase/img/integrations_couchbase.png) Couchbase

Metadata associated with SignalFx's Couchbase integration can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-couchbase">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd-couchbase">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

`collectd-couchbase` is a <a target="_blank" href="http://www.collectd.org/">collectd</a> plugin that collects statistics from Couchbase.

#### FEATURES

##### Built-in dashboards

- **Couchbase Clusters**: Overview of data from all Couchbase clusters reporting.

  [<img src='./img/dashboard_couchbase_clusters.png' width=200px>](./img/dashboard_couchbase_clusters.png)

- **Couchbase Nodes**: Overview of all data from Couchbase nodes.

  [<img src='./img/dashboard_couchbase_nodes.png' width=200px>](./img/dashboard_couchbase_nodes.png)

- **Couchbase Node**: Focus on a single Couchbase node.

  [<img src='./img/dashboard_couchbase_node.png' width=200px>](./img/dashboard_couchbase_node.png)

- **Couchbase Buckets**: Performance and activity of Couchbase buckets.

  [<img src='./img/dashboard_couchbase_buckets.png' width=200px>](./img/dashboard_couchbase_buckets.png)

- **Couchbase Bucket**: Focus on a single Couchbase bucket.

  [<img src='./img/dashboard_couchbase_bucket.png' width=200px>](./img/dashboard_couchbase_bucket.png)

### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| python | 2.7 or later |
| couchbase | 3.0 or later |
| Python plugin for collectd | (included with [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd)) |


### INSTALLATION

1. Download the <a target="_blank" href="https://github.com/signalfx/collectd-couchbase">collectd-couchbase Python module</a>.

2. Download SignalFx's <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/collectd-couchbase/10-couchbase.conf">sample configuration file</a> for this plugin to `/etc/collectd/managed_config`.

3. Modify the sample configuration file as described in [Configuration](#configuration), below.

4. Restart collectd.

### CONFIGURATION

Using the example configuration file <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd-couchbase/10-couchbase.conf">10-couchbase.conf</a> as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the Couchbase nodes and buckets to be monitored.

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | "/opt/collectd-couchbase" |
| CollectTarget | Define what this Module block will monitor: "NODE", for a Couchbase node, or "BUCKET" for a Couchbase bucket. | "BUCKET" |
| CollectBucket | If CollectTarget is "BUCKET", the name of the bucket that this Module block will monitor. | "custom_bucket" |
| Host | Hostname or IP address of the Couchbase server. | "localhost" |
| Port | Port at which the Couchbase server can be reached. | "8091" |
| ClusterName | Name of this Couchbase cluster. | "default" |
| CollectMode | Change to "detailed" to collect all available metrics from Couchbase stats API. Defaults to "default", collecting a curated set that works well with SignalFx. See <a target="_blank" href="https://github.com/signalfx/collectd-couchbase/blob/master/metric_info.py">metric_info.py</a> for more information. | "default" |
| Interval | Number of seconds between calls to Couchbase API. | 10 |
| Username | If CollectTarget is "BUCKET" and this bucket requires authentication, username to authenticate to this bucket. If this bucket does not require authentication, do not include this option in the Module block. | "USERNAME" |
| Password | If CollectTarget is "BUCKET" and this bucket requires authentication, password to authenticate to this bucket. If this bucket does not require authentication, do not include this option in the Module block. | "PASSWORD" |
| FieldLength | The number of characters used to encode dimension data. **CAUTION**: Modify this value only if you specifically compiled collectd with a non-default value for `DATA_MAX_NAME_LEN` in `plugin.h`. |  "1024" |

### USAGE

Below are screen captures of dashboards created for this plugin by SignalFx, illustrating the metrics emitted by this plugin.

For general reference on how to monitor Couchbase, see <a target="_blank" href="http://blog.couchbase.com/monitoring-couchbase-cluster">Couchbase Monitoring</a> and <a target="_blank" href="http://developer.couchbase.com/documentation/server/4.0/monitoring/monitoring-rest.html">Monitor using the REST API</a>.

**Note on bucket metrics**

This plugin emits some metrics about the bucket's performance across the cluster, and some metrics about the bucket's performance per node.

Metrics beginning with `gauge.bucket.basic.​*` and `gauge.bucket.quota.*`​ are reported once per cluster. All other bucket metrics (`gauge.bucket.*`) are reported by every node that hosts that bucket. In order to analyze bucket performance for the entire bucket, apply functions like Sum or Mean to group node-level metrics together by bucket.

**Monitoring a Couchbase cluster**

On the Couchbase Nodes overview dashboard, you can see at a glance the status the nodes and buckets in a given cluster. Nodes in the cluster should be seeing balanced activity. Buckets in the cluster should each have adequate memory remaining.

![Couchbase - Nodes and buckets in a cluster](././img/nodes_and_buckets_snapshot.png)

*This cluster's three nodes have roughly the same number of gets per second, and its two buckets have plenty of headroom.*

This dashboard also includes a percentile distribution of CPU utilization per node, allowing quick identification of unusually hot nodes. This chart shows minimum, 10th percentile, median (50th percentile), 90th percentile, and maximum CPU utilization for each node in the cluster.

![Nodes CPU distribution](././img/nodes_cpu.png)

*This cluster's CPU utilization distribution shows only a small amount of variation in utilization, suggesting that each of the nodes is using about the same amount.*

**Monitoring a Couchbase node**

Zooming in to an individual node shows that node's activity, cache performance, and compute resource usage.

![Node overview](././img/node.png)

*This node is lightly loaded. To compare its activity to other nodes in this cluster, we'd use the Couchbase Nodes dashboard above.*

We can check the node's cache performance using a graph that shows the number of gets per second in yellow, overlaid on the number of cache hits in blue. The ratio between gets and cache hits is computed as "hit ratio" and is shown as a dotted line. When every get request results in a cache hit, the graph is green and the dotted line remains high. When there are fewer cache hits than gets, the graph shows yellow areas and the dotted line drops.

![Gets and hits](././img/node_gets_and_hits.png)

*This lightly-loaded node has a 100% cache hit ratio: it can serve every get request that it receives from memory.*

**Monitoring Couchbase buckets**

The Couchbase Buckets overview shows activity for all buckets being monitored.

![Buckets overview](././img/buckets_activity.png)

*The buckets in this cluster happen to have about the same number of items and are serving about the same number of operations per second.*

**Monitoring a single Couchbase bucket**

Selecting a particular bucket to show on the Couchbase Bucket dashboard lets us go deep on that bucket's performance.

Resident items ratio and cache miss rate are inversely related: as the ratio of items in this bucket that are resident in memory drops, the number of get requests that require a fetch from disk will increase.

![Bucket cache performance](././img/bucket_cache_miss_rate.png)

*This bucket has a 100% resident items ratio: all of the items that it contains can be served from memory, instead of disk.*

The performance of Couchbase buckets is bound by memory. When memory is exhausted, new items can be stored only by ejecting old items. An attempt to store a new item in a bucket with insufficient memory headroom produces an out-of-memory error: either a "temp" error (an old item will be ejected, try again) or a "non-temp" error (this item cannot be stored at all). Any out-of-memory error is cause for concern.

![Bucket memory usage](././img/bucket_memory.png)

*This bucket has available memory, and shows no out-of-memory errors.*

Couchbase persists in-memory items to disk. This graph shows the number of items that have been added to the disk write queue in yellow, and the number of items that have been successfully written in blue. When Couchbase is able to keep up with disk writes, these metrics are equal and the graph is green. When the disk queue is filling faster than it can be drained, this graph shows yellow areas.  

![Bucket write queue](././img/bucket_write_queue.png)

*This bucket is keeping up with disk writes: the number of items added to the queue is about equal to the number of items successfully written to disk.*

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
