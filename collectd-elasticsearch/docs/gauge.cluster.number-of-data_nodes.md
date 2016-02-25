---
title: Number of Data Nodes
brief: The current number of data nodes in the cluster
metric_type: gauge
---
### Number of Data Nodes

> How many data nodes the cluster currently have.

This metric indicates the number of data nodes that are currently participating in the cluster. Each Elasticsearch node can either be allowed to store data locally or not. Storing data locally means that shards of different indexes can be allocated to that node. By default, each node is considered to be a data node. This can be turned off by setting `node.data` to false. 
