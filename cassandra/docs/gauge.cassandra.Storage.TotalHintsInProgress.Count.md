
---
title: gauge.cassandra.Storage.TotalHintsInProgress.Count
brief: Total pending hints
metric_type: gauge
custom: false
---
### gauge.cassandra.Storage.TotalHintsInProgress.Count

Total pending hints. Indicates that write operations cannot be
delivered to a node, usually because a node is down. If this value is
increasing and all nodes are up then there may be some connectivity
issue between nodes in the cluster.

