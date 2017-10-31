# ![](./img/integrations_couchdb.png) CouchDB

Metadata associated with the couchdb plugin for collectd can be found [here](https://github.com/signalfx/integrations/tree/release/collectd-couchdb). The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd-couchdb).

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This is the SignalFx couchdb plugin. Follow these instructions to install the couchdb plugin for collectd.

The [couchdb-collectd](https://github.com/signalfx/collectd-couchdb) plugin collects metrics from couchdb instances by calling the api endpoint: [stats](http://docs.couchdb.org/en/2.1.0/api/server/common.html#stats)

#### FEATURES

#### Built-in dashboards

- **COUCHDB CLUSTER**: Provides a high-level overview of metrics for a single couchdb cluster.

  [<img src='./img/couchdb-cluster-dashboard-top.png' width=200px>](./img/couchdb-cluster-dashboard-top.png)

  [<img src='./img/couchdb-cluster-dashboard-bottom.png' width=200px>](./img/couchdb-cluster-dashboard-bottom.png)  

- **COUCHDB NODE**: Provides metrics from a single couchdb node.

  [<img src='./img/couchdb-node-dashboard.png' width=200px>](./img/couchdb-node-dashboard-top.png)

- **COUCHDB NODES**: Provides metrics from couchdb nodes on a particular host.

  [<img src='./img/couchdb-nodes-dashboard.png' width=200px>](./img/couchdb-nodes-dashboard.png)


### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| python | 2.6 or later |
| couchdb | 2.0.0 or later |
| Python plugin for collectd | (included with [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd)) |

### INSTALLATION

1. Download [collectd-couchdb](https://github.com/signalfx/collectd-couchdb). Place the `couchdb_plugin.py` file in `/usr/share/collectd/collectd-couchdb`

2. Modify the [sample configuration file](https://github.com/signalfx/integrations/tree/release/collectd-couchdb/10-couchdb.conf) for this plugin to `/etc/collectd/managed_config`

3. Modify the sample configuration file as described in [Configuration](#configuration), below

4. Install the Python requirements with sudo ```pip install -r requirements.txt```

5. Restart collectd


### CONFIGURATION

Using the example configuration file [10-couchdb.conf](https://github.com/signalfx/integrations/tree/release/collectd-couchdb/10-couchdb.conf) as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the couchdb members

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | "/usr/share/collectd/collectd-couchdb/" |
| Host | Host name of the couchdb member | "localhost" |
| Port | Port at which the member can be reached | "5984" |
| Node | Name of the couchdb node in the cluster | "couchdb@test\_node" |
| EnhancedMetrics | Boolean to indicate if the uncommented enhanced metrics in couchdb_metrics.py are needed. | "false" |
| Username | Username required for authentication of couchdb | "admin" |
| Password | Password required for authentication of couhcdb | "admin" |
| Dimension | Space separated key-value pair for a user-defined dimension | dimension\_name dimension\_value |
| Interval | Number of seconds between calls to couchdb API. | 10 |
| ssl\_keyfile | Path to the keyfile | "path/to/file" |
| ssl\_certificate | Path to the certificate | "path/to/file" |
| ssl\_ca\_certs | Path to the ca file | "path/to/file" |

Example configuration:

```apache
LoadPlugin python
<Plugin python>
  ModulePath "/usr/share/collectd/collectd-couchdb/"

  Import couchdb_plugin
  <Module couchdb_plugin>
    Host "localhost"
    Port "5984"
    Node "couchdb@test_node"
    Interval 10
    Username "admin"
    Password "admin"
    Cluster "dev"
    EnhancedMetrics False
    Dimension "version" "2.0.0"
    ssl_keyfile "/Users/ec2/couchdb/couchdb-ca/couchdb-ca/private/couchdb-client.key"
    ssl_certificate "/Users/ec2/couchdb/couchdb-ca/couchdb-ca/certs/couchdb-client.crt"
    ssl_ca_certs "/Users/ec2/couchdb/couchdb-ca/couchdb-ca/certs/ca.crt"
  </Module>
</Plugin>
```

The plugin can be configured to collect metrics from multiple instances in the following manner.

```apache
LoadPlugin python

<Plugin python>
  ModulePath "/usr/share/collectd/collectd-couchdb/"
  Import couchdb_plugin
  <Module couchdb_plugin>
    Host "localhost"
    Port "15984"
    Interval 10
    Node "couchdb@test_node1"
    Username "admin"
    Password "admin"
    Cluster "dev"
  </Module>
  <Module couchdb_plugin>
    Host "localhost"
    Port "25984"
    Interval 10
    Node "couchdb@test_node2"
    Username "admin"
    Password "admin"
    Cluster "dev"
  </Module>
  <Module couchdb_plugin>
    Host "localhost"
    Port "35984"
    Interval 10
    Node "couchdb@test_node3"
    Username "admin"
    Password "admin"
    Cluster "dev"
  </Module>
</Plugin>
```

### USAGE

#### Interpreting Built-in dashboards

- **COUCHDB CLUSTER**:

  - **Number of Nodes**: Shows the toal number of active nodes in the cluster.

    [<img src='./img/chart-couchdb-cluster-active-nodes.png' width=200px>](./img/chart-couchdb-cluster-active-nodes.png)

  - **Number of Requests**: Shows the total number of requests handled per second by all the nodes in the cluster.

    [<img src='./img/chart-couchdb-cluster-total-requests.png' width=200px>](./img/chart-couchdb-cluster-total-requests.png)

  - **Request Processing Time**: Show the average request processing time of all the nodes in the cluster.

    [<img src='./img/chart-couchdb-cluster-request-time.png' width=200px>](./img/chart-couchdb-cluster-request-time.png)

  - **Database Reads and Writes**: The total number of database reads and writes performed by all the nodes in the cluster.

    [<img src='./img/chart-couchdb-cluster-db-reads-writes.png' width=200px>](./img/chart-couchdb-cluster-db-reads-writes.png)

  - **Active Data Usage**: Shows the active data usage percentage. As the couchdb does only soft deletes, all the deleted records are still present in the database. This chart will indicate the percentage of active data in the database. It is advisable to compact database when the value is below 50%

    [<img src='./img/chart-couchdb-cluster-active-data-usage.png' width=200px>](./img/chart-couchdb-cluster-active-data-usage.png)

  - **Active Docs vs Deleted Docs**: Shows the total number of active and deleted docs present in the cluster.

    [<img src='./img/chart-couchdb-cluster-active-del-docs.png' width=200px>](./img/chart-couchdb-cluster-active-del-docs.png)


- **COUCHDB NODE**:

  - **Number of Requests**: Shows the total number of requests handled by the node per second.

    [<img src='./img/chart-couchdb-node-requests.png' width=200px>](./img/chart-couchdb-node-requests.png)

  - **Request Processing Time**: Show the average request processing time of the node.

    [<img src='./img/chart-couchdb-node-request-time.png' width=200px>](./img/chart-couchdb-node-request-time.png)

  - **Database Reads and Writes**: The total number of database reads and writes performed by the node.

    [<img src='./img/chart-couchdb-node-db-reads-writes.png' width=200px>](./img/chart-couchdb-node-db-reads-writes.png)  

  - **Auth Cache Hits vs Misses**: Shows the stack chart of auth cache hits and misses.
    
    [<img src='./img/chart-couchdb-node-auth-hits-misses.png' width=200px>](./img/chart-couchdb-node-auth-hits-misses.png)

  - **Shard Cache Hits vs Misses**: Shows the stack chart of shard cache hits and misses.
    
    [<img src='./img/chart-couchdb-node-shard-hits-misses.png' width=200px>](./img/chart-couchdb-node-shard-hits-misses.png)

- **COUCHDB NODES**: Provides metrics from nodes on a particular host.

  - **Number of Nodes**: The total number of couchdb nodes running on the host.

    [<img src='./img/chart-couchdb-nodes-active-nodes.png' width=200px>](./img/chart-couchdb-nodes-active-nodes.png)

  - **Top Requests**: List of top nodes handling highest requests per second on the host.

    [<img src='./img/chart-couchdb-nodes-top-requests.png' width=200px>](./img/chart-couchdb-nodes-top-requests.png)

  - **Top Request Processing Time**: List of nodes having highest request processing time on the host.

    [<img src='./img/chart-couchdb-nodes-top-request-time.png' width=200px>](./img/chart-couchdb-nodes-top-request-time.png)

  - **Database Reads**: Percentile distribution of database reads of all the nodes present in the host.

    [<img src='./img/chart-couchdb-nodes-db-reads.png' width=200px>](./img/chart-couchdb-nodes-db-reads.png)

  - **Database Writes**: Percentile distribution of database writes of all the nodes present in the host.

    [<img src='./img/chart-couchdb-nodes-db-writes.png' width=200px>](./img/chart-couchdb-nodes-db-writes.png)


All metrics reported by the couchdb collectd plugin will contain the following dimensions by default:

* `node`, name of the node as in the cluster
* `cluster`, human readable cluster name


A few other details:

* `plugin` is always set to `couchdb`
* `plugin_instance` will contain the IP address and the port of the member given in the configuration
* To add enhanced metrics, use the configuration options mentioned in [configuration](#configuration).


### METRICS
By default, basic metrics are provided. For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs). See [usage](#usage) for details.



### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.