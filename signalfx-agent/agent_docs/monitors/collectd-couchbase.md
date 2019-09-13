
<!--- Generated by to-integrations-repo script in Smart Agent repo, DO NOT MODIFY HERE --->
<!--- GENERATED BY gomplate from scripts/docs/monitor-page.md.tmpl --->

# collectd/couchbase

Monitor Type: `collectd/couchbase` ([Source](https://github.com/signalfx/signalfx-agent/tree/master/internal/monitors/collectd/couchbase))

**Accepts Endpoints**: **Yes**

**Multiple Instances Allowed**: Yes

## Overview

This is a Smart Agent monitor for [Couchbase](https://www.couchbase.com/)
that uses the [couchbase collectd Python
plugin](https://github.com/signalfx/collectd-couchbase) to collect metrics
from Couchbase server instances.

For general reference on how to monitor Couchbase, see <a target="_blank"
href="http://blog.couchbase.com/monitoring-couchbase-cluster">Couchbase
Monitoring</a> and <a target="_blank"
href="http://developer.couchbase.com/documentation/server/4.0/monitoring/monitoring-rest.html">Monitor
using the REST API</a>.

<!--- METRICS --->
## Note on bucket metrics

This plugin emits some metrics about the bucket's performance across the
cluster, and some metrics about the bucket's performance per node.

Metrics beginning with `gauge.bucket.basic.*` and
`gauge.bucket.quota.*` are reported once per cluster. All other
bucket metrics (`gauge.bucket.*`) are reported by every node that hosts
that bucket. In order to analyze bucket performance for the entire bucket,
apply functions like Sum or Mean to group node-level metrics together by
bucket.

<!--- SETUP --->
## Example Config

Sample YAML configuration with custom query:

```yaml
monitors:
- type: collectd/couchbase
  host: 127.0.0.1
  port: 8091
  collectTarget: "NODE"
  clusterName: "my-cluster"
  username: "user"
  password: "password"
```


## Configuration

To activate this monitor in the Smart Agent, add the following to your
agent config:

```
monitors:  # All monitor config goes under this key
 - type: collectd/couchbase
   ...  # Additional config
```

**For a list of monitor options that are common to all monitors, see [Common
Configuration](../monitor-config.html#common-configuration).**


| Config option | Required | Type | Description |
| --- | --- | --- | --- |
| `pythonBinary` | no | `string` | Path to a python binary that should be used to execute the Python code. If not set, a built-in runtime will be used.  Can include arguments to the binary as well. |
| `host` | **yes** | `string` |  |
| `port` | **yes** | `integer` |  |
| `collectTarget` | **yes** | `string` | Define what this Module block will monitor: "NODE", for a Couchbase node, or "BUCKET" for a Couchbase bucket. |
| `collectBucket` | no | `string` | If CollectTarget is "BUCKET", CollectBucket specifies the name of the bucket that this will monitor. |
| `clusterName` | no | `string` | Name of this Couchbase cluster. (**default**:"default") |
| `collectMode` | no | `string` | Change to "detailed" to collect all available metrics from Couchbase stats API. Defaults to "default", collecting a curated set that works well with SignalFx. |
| `username` | no | `string` | Username to authenticate with |
| `password` | no | `string` | Password to authenticate with |


## Metrics

These are the metrics available for this monitor.
Metrics that are categorized as
[container/host](https://docs.signalfx.com/en/latest/admin-guide/usage.html#about-custom-bundled-and-high-resolution-metrics)
(*default*) are ***in bold and italics*** in the list below.


#### Group bucket
All of the following metrics are part of the `bucket` metric group. All of
the non-default metrics below can be turned on by adding `bucket` to the
monitor config option `extraGroups`:
 - `gauge.bucket.basic.dataUsed` (*gauge*)<br>    Size of user data within buckets of the specified state that are resident in RAM (%)
 - `gauge.bucket.basic.diskFetches` (*gauge*)<br>    Number of disk fetches
 - ***`gauge.bucket.basic.diskUsed`*** (*gauge*)<br>    Amount of disk used (bytes)
 - ***`gauge.bucket.basic.itemCount`*** (*gauge*)<br>    Number of items associated with the bucket
 - `gauge.bucket.basic.memUsed` (*gauge*)<br>    Amount of memory used by the bucket (bytes)
 - ***`gauge.bucket.basic.opsPerSec`*** (*gauge*)<br>    Number of operations per second
 - ***`gauge.bucket.basic.quotaPercentUsed`*** (*gauge*)<br>    Percentage of RAM used (for active objects) against the configure bucket size (%)
 - ***`gauge.bucket.op.cmd_get`*** (*gauge*)<br>    requested objects
 - ***`gauge.bucket.op.couch_docs_fragmentation`*** (*gauge*)<br>    Percent fragmentation of documents in this bucket.
 - ***`gauge.bucket.op.couch_views_ops`*** (*gauge*)<br>    view operations per second
 - ***`gauge.bucket.op.curr_connections`*** (*gauge*)<br>    open connection per bucket
 - `gauge.bucket.op.curr_items` (*gauge*)<br>    total number of stored items per bucket
 - `gauge.bucket.op.disk_write_queue` (*gauge*)<br>    number of items waiting to be written to disk
 - ***`gauge.bucket.op.ep_bg_fetched`*** (*gauge*)<br>    number of items fetched from disk
 - ***`gauge.bucket.op.ep_cache_miss_rate`*** (*gauge*)<br>    ratio of requested objects found in cache vs retrieved from disk
 - ***`gauge.bucket.op.ep_diskqueue_drain`*** (*gauge*)<br>    items removed from disk queue
 - ***`gauge.bucket.op.ep_diskqueue_fill`*** (*gauge*)<br>    enqueued items on disk queue
 - ***`gauge.bucket.op.ep_mem_high_wat`*** (*gauge*)<br>    memory high water mark - point at which active objects begin to be ejected from bucket
 - `gauge.bucket.op.ep_mem_low_wat` (*gauge*)<br>    memory low water mark
 - ***`gauge.bucket.op.ep_num_value_ejects`*** (*gauge*)<br>    number of objects ejected out of the bucket
 - ***`gauge.bucket.op.ep_oom_errors`*** (*gauge*)<br>    request rejected - bucket is at quota, panic
 - ***`gauge.bucket.op.ep_queue_size`*** (*gauge*)<br>    number of items queued for storage
 - ***`gauge.bucket.op.ep_tmp_oom_errors`*** (*gauge*)<br>    request rejected - couchbase is making room by ejecting objects, try again later
 - ***`gauge.bucket.op.mem_used`*** (*gauge*)<br>    memory used
 - `gauge.bucket.op.ops` (*gauge*)<br>    total of gets, sets, increment and decrement
 - ***`gauge.bucket.op.vb_active_resident_items_ratio`*** (*gauge*)<br>    ratio of items kept in memory vs stored on disk
 - `gauge.bucket.quota.ram` (*gauge*)<br>    Amount of RAM used by the bucket (bytes).
 - `gauge.bucket.quota.rawRAM` (*gauge*)<br>    Amount of raw RAM used by the bucket (bytes).

#### Group nodes
All of the following metrics are part of the `nodes` metric group. All of
the non-default metrics below can be turned on by adding `nodes` to the
monitor config option `extraGroups`:
 - ***`gauge.nodes.cmd_get`*** (*gauge*)<br>    Number of get commands
 - ***`gauge.nodes.couch_docs_actual_disk_size`*** (*gauge*)<br>    Amount of disk space used by Couch docs.(bytes)
 - ***`gauge.nodes.couch_docs_data_size`*** (*gauge*)<br>    Data size of couch documents associated with a node (bytes)
 - `gauge.nodes.couch_spatial_data_size` (*gauge*)<br>    Size of object data for spatial views (bytes)
 - `gauge.nodes.couch_spatial_disk_size` (*gauge*)<br>    Amount of disk space occupied by spatial views, in bytes.
 - `gauge.nodes.couch_views_actual_disk_size` (*gauge*)<br>    Amount of disk space occupied by Couch views (bytes).
 - `gauge.nodes.couch_views_data_size` (*gauge*)<br>    Size of object data for Couch views (bytes).
 - `gauge.nodes.curr_items` (*gauge*)<br>    Number of current items
 - ***`gauge.nodes.curr_items_tot`*** (*gauge*)<br>    Total number of items associated with node
 - ***`gauge.nodes.ep_bg_fetched`*** (*gauge*)<br>    Number of disk fetches performed since server was started
 - `gauge.nodes.get_hits` (*gauge*)<br>    Number of get hits
 - `gauge.nodes.mcdMemoryAllocated` (*gauge*)<br>    Amount of memcached memory allocated (bytes).
 - `gauge.nodes.mcdMemoryReserved` (*gauge*)<br>    Amount of memcached memory reserved (bytes).
 - ***`gauge.nodes.mem_used`*** (*gauge*)<br>    Memory used by the node (bytes)
 - `gauge.nodes.memoryFree` (*gauge*)<br>    Amount of memory free for the node (bytes).
 - `gauge.nodes.memoryTotal` (*gauge*)<br>    Total memory available to the node (bytes).
 - ***`gauge.nodes.ops`*** (*gauge*)<br>    Number of operations performed on Couchbase
 - ***`gauge.nodes.system.cpu_utilization_rate`*** (*gauge*)<br>    The CPU utilization rate (%)
 - ***`gauge.nodes.system.mem_free`*** (*gauge*)<br>    Free memory available to the node (bytes)
 - ***`gauge.nodes.system.mem_total`*** (*gauge*)<br>    Total memory available to the node (bytes)
 - ***`gauge.nodes.system.swap_total`*** (*gauge*)<br>    Total swap size allocated (bytes)
 - ***`gauge.nodes.system.swap_used`*** (*gauge*)<br>    Amount of swap space used (bytes)
 - `gauge.nodes.vb_replica_curr_items` (*gauge*)<br>    Number of items/documents that are replicas

#### Group storage
All of the following metrics are part of the `storage` metric group. All of
the non-default metrics below can be turned on by adding `storage` to the
monitor config option `extraGroups`:
 - `gauge.storage.hdd.free` (*gauge*)<br>    Free harddrive space in the cluster (bytes)
 - `gauge.storage.hdd.quotaTotal` (*gauge*)<br>    Harddrive quota total for the cluster (bytes)
 - `gauge.storage.hdd.total` (*gauge*)<br>    Total harddrive space available to cluster (bytes)
 - `gauge.storage.hdd.used` (*gauge*)<br>    Harddrive space used by the cluster (bytes)
 - `gauge.storage.hdd.usedByData` (*gauge*)<br>    Harddrive use by the data in the cluster(bytes)
 - `gauge.storage.ram.quotaTotal` (*gauge*)<br>    Ram quota total for the cluster (bytes)
 - `gauge.storage.ram.quotaTotalPerNode` (*gauge*)<br>    Ram quota total per node (bytes)
 - `gauge.storage.ram.quotaUsed` (*gauge*)<br>    Ram quota used by the cluster (bytes)
 - `gauge.storage.ram.quotaUsedPerNode` (*gauge*)<br>    Ram quota used per node (bytes)
 - `gauge.storage.ram.total` (*gauge*)<br>    Total ram available to cluster (bytes)
 - `gauge.storage.ram.used` (*gauge*)<br>    Ram used by the cluster (bytes)
 - `gauge.storage.ram.usedByData` (*gauge*)<br>    Ram used by the data in the cluster (bytes)

### Non-default metrics (version 4.7.0+)

**The following information applies to the agent version 4.7.0+ that has
`enableBuiltInFiltering: true` set on the top level of the agent config.**

To emit metrics that are not _default_, you can add those metrics in the
generic monitor-level `extraMetrics` config option.  Metrics that are derived
from specific configuration options that do not appear in the above list of
metrics do not need to be added to `extraMetrics`.

To see a list of metrics that will be emitted you can run `agent-status
monitors` after configuring this monitor in a running agent instance.

### Legacy non-default metrics (version < 4.7.0)

**The following information only applies to agent version older than 4.7.0. If
you have a newer agent and have set `enableBuiltInFiltering: true` at the top
level of your agent config, see the section above. See upgrade instructions in
[Old-style whitelist filtering](../legacy-filtering.html#old-style-whitelist-filtering).**

If you have a reference to the `whitelist.json` in your agent's top-level
`metricsToExclude` config option, and you want to emit metrics that are not in
that whitelist, then you need to add an item to the top-level
`metricsToInclude` config option to override that whitelist (see [Inclusion
filtering](../legacy-filtering.html#inclusion-filtering).  Or you can just
copy the whitelist.json, modify it, and reference that in `metricsToExclude`.


