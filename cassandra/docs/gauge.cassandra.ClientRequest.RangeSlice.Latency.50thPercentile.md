
---
title: gauge.cassandra.ClientRequest.RangeSlice.Latency.50thPercentile
brief: 50th percentile (median) of Cassandra range slice latency
metric_type: gauge
custom: true
---
### gauge.cassandra.ClientRequest.RangeSlice.Latency.50thPercentile

50th percentile (median) of Cassandra range slice latency. This value
should be similar across all nodes in the cluster. If some nodes have higher
values than the rest of the cluster then they may have more connected clients
or may be experiencing heavier than usual compaction load.

