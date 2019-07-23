# ![](https://github.com/signalfx/integrations/blob/master/elasticsearch/img/integrations_elasticsearch.png) Elasticsearch

Metadata associated with the Elasticsearch monitor can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/elasticsearch">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/signalfx-agent/tree/master/internal/monitors/elasticsearch">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This is the SignalFx Elasticsearch integration. This will send data about Elasticsearch to SignalFx, enabling built-in Elasticsearch monitoring dashboards.

Use this monitor to monitor the following types of information from an Elasticsearch node:

  * node statistics (cpu, os, jvm, indexing, search, thread pools, etc..)
  * per-index statistics
  * cluster statistics

Original Elasticsearch Documentation <a target="_blank" href="https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html">https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html</a>

#### FEATURES

##### Built-in dashboards

- **Elasticsearch**: Overview of all data from Elasticsearch hosts.

  [<img src='./img/dashboard_elasticsearch.png' width=200px>](./img/dashboard_elasticsearch.png)

- **Elasticsearch Cluster**: Focus on a single Elasticsearch cluster.

  [<img src='./img/dashboard_elasticsearch_cluster.png' width=200px>](./img/dashboard_elasticsearch_cluster.png)

- **Elasticsearch Node**: Focus further on a single Elasticsearch node.

  [<img src='./img/dashboard_elasticsearch_node.png' width=200px>](./img/dashboard_elasticsearch_node.png)

- **Elasticsearch Indexes**: Overview of all Elasticsearch indexes.

  [<img src='./img/dashboard_elasticsearch_indexes.png' width=200px>](./img/dashboard_elasticsearch_indexes.png)

- **Elasticsearch Index**: Focus on a single Elasticsearch index.

  [<img src='./img/dashboard_elasticsearch_index.png' width=200px>](./img/dashboard_elasticsearch_index.png)

### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software          | Version        |
|-------------------|----------------|
| Elasticsearch     | 1.0.0 or later |
| Smart Agent       | 4.4.0 or later to use the new `elasticsearch` monitor that replaced the deprecated `collectd/elasticsearch` monitor |

### CONFIGURATION

This integration is part of the <a
href="https://docs.signalfx.com/en/latest/integrations/agent/index.html"
target="_blank">SignalFx Smart Agent</a>, see the docs for <a
href="https://docs.signalfx.com/en/latest/integrations/agent/monitors/elasticsearch.html"
target="_blank">the elasticsearch monitor</a> for details on how to configure
the Smart Agent.

### USAGE

Sample of built-in dashboard in SignalFx:

![](././img/dashboard_elasticsearch.png)

### METRICS

For documentation of the metrics and dimensions emitted by this monitor, [click here](./docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
