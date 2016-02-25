---
title: Number of Open File Descriptors
brief: Number of currently open file descriptors
metric_type: gauge
---
### Number of Open File Descriptors

> The number of file descriptors used by the Elasticsearch process.

File descriptors are used for files as well as for network connections. Usually this metric is correlated with the number of segments that Elasticsearh is managing (`gauge.indices.segments.count`).
