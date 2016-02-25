---
title: Elasticsearch Metrics
brief: Metrics collected from Elasticsearch nodes
---
### Elasticsearch Metrics

Use the [elasticsearch-plugin](https://github.com/signalfuse/collectd-elasticsearch) collectd plugin to collect metrics for Elasticsearch.

Use this plugin to monitor the following types of information from an Elasticsearch node:
  * node statistics (cpu, os, jvm, indexing, search, thread pools, etc..)
  * per-index statistics
  * cluster statistics
  
Original Elasticsearch Documentation https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html

### Version information

| Software          | Version        |
|-------------------|----------------|
| collectd          | 4.9 or later   |
| Elasticsearch     | 1.0.0 or later |

### Configuration
 * set the cluster name. It is preferrable to have a unique cluster name to be able to easily distinguish between clusters. This is usually the same as the cluster name in the Elasticsearch configuration file. This defaults to "elasticsearch".
 * per-index and cluster statistics can be disabled. They are enabled by default.

Example config located at https://raw.githubusercontent.com/signalfx/signalfx-collectd-configs/master/managed_config/20-elasticsearch.conf

### References
 * node statistics: https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-nodes-stats.html
 * per-index statistics: https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-stats.html
 * cluster statistics: https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-stats.html
 * monitoring Elasticsearch: https://www.elastic.co/guide/en/elasticsearch/guide/current/cluster-admin.html
