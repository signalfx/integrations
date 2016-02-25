---
title: Number of Relocating Shards
brief: The number of shards that are currently being relocated
metric_type: gauge
---
### Number of Relocating Shards

> How many shards are currently being relocated.

This shows the number of shards that are currently moving from one node to another node. This number is often zero, but can increase when Elasticsearch decides a cluster is not properly balanced, a new node is added, or a node is taken down.
