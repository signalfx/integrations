# ![](https://github.com/signalfx/integrations/blob/master/collectd-mongodb/img/integrations_mongodb.png) MongoDB

Metadata associated with the MongoDB collectd plugin can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-mongodb">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd-mongodb">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use the <a target="_blank" href="https://github.com/signalfx/collectd-mongodb">mongodb</a> collectd plugin to collect metrics from MongoDB nodes.

This plugin captures the following metrics about MongoDB generally:

* memory
* network input/output bytes count
* heap usage
* db connections
* operations count
* active client connections
* queued operations

The plugin also captures the following DB-specific metrics:

* db size
* db counters

Documentation for MongoDB can be found <a target="_blank" href="http://docs.mongodb.org/manual/">here</a>.

#### FEATURES

##### Built-in dashboards

- **MongoDB Hosts**: Overview of data from all MongoDB hosts.

  [<img src='./img/dashboard_mongodb_hosts.png' width=200px>](./img/dashboard_mongodb_hosts.png)

- **MongoDB Host**: Focus on a single MongoDB host.

  [<img src='./img/dashboard_mongodb_host.png' width=200px>](./img/dashboard_mongodb_host.png)

- **MongoDB Cluster**: Overview of a MongoDB cluster.

### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| Python    |  2.4 or later  |
| MongoDB   |  2.6 or later  |
| PyMongo   |  3.0 or later  |
| Python plugin for collectd | (included with [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd)) |

### INSTALLATION

**If you are using the new Smart Agent, see the docs for [the collectd/mongodb
monitor](https://github.com/signalfx/signalfx-agent/tree/master/docs/monitors/collectd-mongodb.md)
for more information.  The configuration documentation below may be helpful as
well, but consult the Smart Agent repo's docs for the exact schema.**


1. Install `pip` and `pymongo`.

    * **RHEL/CentOS and Amazon Linux**

            yum install -y epel-release
            yum install -y python-pip
            sudo pip install pymongo==3.0.3

    * **Ubuntu and Debian:**

            apt-get install -y python-pip python-dev build-essential
            sudo pip install pymongo==3.0.3



2. If you want to use SSL/TLS to connect to Mongo, install the PyMongo TLS
   dependencies as well:

        sudo pip install pymongo[tls]

3. Download the <a target="_blank" href="https://github.com/signalfx/collectd-mongodb">collectd-mongodb Python module</a>.  

4. Download SignalFx's <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd-mongodb/10-mongodb.conf">sample configuration file</a> for this plugin to `/etc/collectd/managed_config`.

5. Modify the sample configuration file as described in [Configuration](#configuration), below.

6. Restart collectd.

### CONFIGURATION

Using the example configuration file <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd-mongodb/10-mongodb.conf">10-mongodb.conf</a> as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the MongoDB instance to be monitored.

| configuration option | definition | default value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | "/usr/share/collectd/mongodb-collectd-plugin" |
| Host | Host IP | "127.0.0.1" |
| Port | Port number for IP connection | "27017" |
| User | Valid mongodb user | "" |
| Password | Associated password for valid user | "password" |
| Database | Name(s) of database(s) that you would like metrics from. Note: the first database in this list must be "admin", as it is used to perform a `serverStatus()` command. | "admin" "db-prod" "db-dev" |
| Interval | How frequently to send metrics in seconds | collectd `Interval` setting |
| SendCollectionMetrics | Whether to send collection level metrics or not | false |
| SendCollectionTopMetrics | Whether to send collection level top (timing) metrics or not | false |
| CollectionMetricsIntervalMultiplier | How frequently to send collection level metrics as a multiple of the configured plugin interval (e.g. if the Interval is 15 and the multiplier is 4, collection level metrics will be fetched every minute) | 6 |
| UseTLS | Set this to `true` if you want to connect to Mongo using TLS/x509/SSL. | false |
| CACerts | Path to a CA cert that will be used to verify the certificate that Mongo presents (not needed if not using TLS or if Mongo's cert is signed by a globally trusted issuer already installed in the default location on your OS) | "" |
| TLSClientCert | Path to a client certificate (not needed unless your Mongo instance requires x509 client verification) | "" |
| User | (**same as above `User` field but required for TLS client auth**) The username associated with the client cert (this is the *subject* field of the client cert, formatted according to RFC2253 **and in the same order that was specified when creating the user in the Mongo `$external` database**).  You can get this value by running the following command: `openssl x509 -in <pathToClient PEM> -inform PEM -subject -nameopt RFC2253`. | "" |
| TLSClientKey | Path to a client certificate key (not needed unless your Mongo instance requires x509 client verification, or if your client cert above has the key included) | "" |
| TLSClientKeyPassphrase | Passphrase for the TLSClientKey above (requires Python 2.7.9+) | "" |

#### Note: Monitoring multiple instances

Each MongoDB instance to be monitored is specified in a `<Module>` block within the configuration file. By default, the sample configuration file `10-mongodb.conf` contains only one such block. To monitor an additional instance of MongoDB, add another `<Module>` block immediately below the first, and configure it according to that instance's parameters.

#### Note: Creating a MongoDB user for collectd

If you're monitoring a secured MongoDB deployment, it is a good practice to create a MongoDB user with minimal read-only roles, as follows:

```
db.createUser( {
  user: "collectd",
  pwd: "collectd",
  roles: [ { role: "readAnyDatabase", db: "admin" }, { role: "clusterMonitor", db: "admin" } ]
});
```

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

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
