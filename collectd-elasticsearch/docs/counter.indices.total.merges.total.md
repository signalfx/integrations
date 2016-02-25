---
title: Number of Merges
brief: Total number of merges per cluster
metric_type: counter
---
### Number of Merges

> The number of merges that happened on this cluster.

Merges happen every time the index is refreshed due to changes made to it. Elasticsearch's segments are immutable, and merges group together smaller segments into bigger ones. This metric tracks the number of merges across the cluster. It can be examined per index using the `index` dimension.
