# ![](./img/integrations_cassandra.png) Cassandra

 Metadata associated with SignalFx's Cassandra integration with collectd can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/cassandra">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

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
| SignalFx Smart Agent  |  2.0+  |
| Cassandra | 2.0.10+ |


### CONFIGURATION

This integration is part of the <a
href="https://docs.signalfx.com/en/latest/integrations/agent/index.html"
target="_blank">SignalFx Smart Agent</a> -- see the docs for <a
href="https://docs.signalfx.com/en/latest/integrations/agent/monitors/collectd-cassandra.html"
target="_blank">the collectd/cassandra monitor</a> for details on how to
configure the Smart Agent to work with this integration.


### USAGE

Sample of built-in dashboard in SignalFx:

![](././img/dashboard_cassandra.png)

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
