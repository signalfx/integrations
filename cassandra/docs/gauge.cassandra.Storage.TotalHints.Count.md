
---
title: gauge.cassandra.Storage.TotalHints.Count
brief: Total hints since node start
metric_type: gauge
custom: true
---
### gauge.cassandra.Storage.TotalHints.Count

Total hints since node start. Indicates that write operations cannot be
delivered to a node, usually because a node is down. If this value is
increasing and all nodes are up then there may be some connectivity
issue between nodes in the cluster.

