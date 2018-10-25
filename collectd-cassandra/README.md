# ![](./img/integrations_cassandra.png) Cassandra

 Metadata associated with SignalFx's Cassandra integration with collectd can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-cassandra">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/java.c">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Monitor Cassandra using SignalFx's configuration of the Java plugin for collectd.

Use this integration to monitor the following types of information from Cassandra nodes:

* read/write/range-slice requests
* read/write/range-slice errors (timeouts and unavailable)
* read/write/range-slice latency (median, 99th percentile, maximum)
* compaction activity
* hint activity

#### FEATURES

##### Built-in dashboards

- **Cassandra Nodes**: Overview of data from all Cassandra nodes.

  [<img src='./img/dashboard_cassandra_nodes.png' width=200px>](./img/dashboard_cassandra_nodes.png)

- **Cassandra Node**: Focus on a single Cassandra node.

  [<img src='./img/dashboard_cassandra_node.png' width=200px>](./img/dashboard_cassandra_node.png)

### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9+  |
| [Java plugin for collectd](https://github.com/signalfx/integrations/tree/master/collectd-java)[](sfx_link:collectd-java) | (match with collectd version) |
| Cassandra | 2.0.10+ |


### INSTALLATION

**If you are using the new Smart Agent, see the docs for [the collectd/cassandra
monitor](https://github.com/signalfx/signalfx-agent/tree/master/docs/monitors/collectd-cassandra.md)
for more information.  The configuration documentation below may be helpful as
well, but consult the Smart Agent repo's docs for the exact schema.**


#### System modifications

Open the JMX port on your Cassandra app. Cassandra will listen for connections on port 8080 (port 7199 starting in 0.8.0-beta1). More information can be found at the <a target="_blank" href="http://wiki.apache.org/cassandra/JmxInterface">Cassandra Project site</a>. There is also a page covering a few <a target="_blank" href="http://wiki.apache.org/cassandra/JmxGotchas">common issues</a>.

#### Install Cassandra integration

1. RHEL/CentOS and Amazon Linux users: Install the Java plugin for collectd](https://github.com/signalfx/integrations/tree/master/collectd-java)[](sfx_link:collectd-java) if it is not already installed.

2. Download SignalFx's example Cassandra configuration file to `/etc/collectd/managed_config`:  <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/collectd-cassandra/20-cassandra.conf">20-cassandra.conf</a>

3. Modify `20-cassandra.conf` to provide values that make sense for your environment, as described in [Configuration](#configuration), below.

4. Restart collectd.

### CONFIGURATION

Using the example configuration file <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd-cassandra/20-cassandra.conf">20-cassandra.conf</a> as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the Cassandra instance to be monitored.

| Configuration Option | Description | Default |
|-------|-------------|------------|
| ServiceURL | URL of your JMX application. | `service:jmx:rmi:///jndi/rmi://localhost:7199/jmxrmi` |
| Host | The name of your host. Appears as dimension `host` in SignalFx.  </p> Note: (Please leave the identifier `[hostHasService=cassandra]`) in the host name. | `testcassandraserver[hostHasService=cassandra]` |

### USAGE

Sample of built-in dashboard in SignalFx:

![](././img/dashboard_cassandra.png)

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
