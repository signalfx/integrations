# ![](https://github.com/signalfx/integrations/blob/master/mongodb/img/integrations_mongodb.png) MongoDB

#### FEATURES

##### Built-in dashboards

- **MongoDB Hosts**: Overview of data from all MongoDB hosts.

  [<img src='./img/dashboard_mongodb_hosts.png' width=200px>](./img/dashboard_mongodb_hosts.png)

- **MongoDB Host**: Focus on a single MongoDB host.

  [<img src='./img/dashboard_mongodb_host.png' width=200px>](./img/dashboard_mongodb_host.png)

- **MongoDB Cluster**: Overview of a MongoDB cluster.

### USAGE

Below are screen captures of dashboards created for this plugin by SignalFx, illustrating the metrics emitted by this plugin.

For general reference on how to monitor MongoDB performance, see <a target="_blank" href="https://docs.mongodb.org/manual/administration/analyzing-mongodb-performance/">Analyzing MongoDB Performance</a>.

**Monitoring MongoDB clusters**

Writes to MongoDB require the use of the global lock. If lock utilization is high, operations can begin to slow down. This can be a symptom of database issues such as poorly configured or absent indexes, or a schema design that needs improvement. It can also indicate the failure of a disk. Monitor the number of readers and writers waiting for the lock in [gauge.globalLock.currentQueue.total](./docs/gauge.globalLock.currentQueue.total.md).

![lock queue](././img/lock_queue.png)

*This lock has little utilization and few queued readers and writers.*

MongoDB flushes data changes from memory to disk on a timed interval, by default every 60 seconds. If background flushes begin taking longer than usual, it can indicate that the disk doesn't have enough I/O capacity to handle the load (read more below). It could also reflect a large number of writes occurring at once -- check [counter.opcounters.insert](./docs/counter.opcounters.insert.md) and [counter.opcounters.update](./docs/counter.opcounters.update.md).

Monitor average background flush time and the most recent background flush time in [gauge.backgroundFlushing.average\_ms](./docs/gauge.backgroundFlushing.average_ms.md) and [gauge.backgroundFlushing.last\_ms](./docs/gauge.backgroundFlushing.last_ms.md) respectively.

![background flush time](././img/background_flushes.png)

*Average background flush time on this cluster is around 40ms, well within healthy parameters.*

When analyzing the performance of a MongoDB cluster, it's also important to verify that the load is balanced across each instance. The cluster dashboard included in this repository contains many list charts of individual MongoDB instances ordered by important metrics like requests per second ([counter.network.numRequests](./docs/counter.network.numRequests.md)) and number of connections to MongoDB ([gauge.connections.current](./docs/gauge.connections.current.md)). This can help you compare load between instances. Load imbalance can arise in a sharded cluster if MongoDB is unable to balance chunks equally between the shards, for example if lock utilization is high.

![top hosts by requests and connections](././img/top_hosts_by_requests.png)

*All the listed instances show about the same requests per second and number of connections. Their load is balanced.*

**Monitoring MongoDB hosts**

On an individual instance level, it's important to monitor system statistics like memory usage, page faults, and disk I/O utilization.

MongoDB uses memory-mapped files to store data, so it is important to compare the amount of memory that MongoDB has allocated to the amount of system memory. This plugin reports resident memory usage in [gauge.mem.resident](./docs/gauge.mem.resident.md) and mapped memory usage in [gauge.mem.mapped](./docs/gauge.mem.mapped.md). If either of these quantities exceed the amount of system memory (reported by the <a target="_blank" href="https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.memory.html">memory</a> plugin for collectd), the system may be at or over capacity.

![Memory statistics from MongoDB](././img/mongodb_memory.png)

*This MongoDB instance is not using a large amount of resident memory, and has non-mapped memory available to the process (calculated as [gauge.mem.virtual](./docs/gauge.mem.virtual.md) - [gauge.mem.mapped](./docs/gauge.mem.mapped.md).)*

This plugin reports page faults in [counter.extra\_info.page\_faults](./docs/counter.extra_info.page_faults.md). Page faults indicate that reads or writes are occurring to data files that are not currently in memory. This is different from an OS page fault. Sudden increases in MongoDB page faults can indicate that a large read operation is taking place. Steadily high numbers of page faults indicate that MongoDB is reading more often from disk than is optimal.

![Page fault statistics from MongoDB](././img/mongodb_page_faults.png)

*This MongoDB instance has a low rate of page faults. This means that most of the data MongoDB needs to access is in memory, and doesn't need to be fetched from disk.*

You can monitor disk I/O utilization for your MongoDB host using the <a target="_blank" href="https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.disk.html#derive-disk-ops-write">disk_ops.write</a> and <a target="_blank" href="https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.disk.html#derive-disk-ops-read">disk_ops.read</a> metrics emitted by the `disk` plugin for collectd, which is included and enabled by default in most packages of collectd. <a target ="_blank" href="https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.disk.html">Click here to learn more about the collectd-disk</a> plugin.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
