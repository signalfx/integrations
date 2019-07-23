
---
title: counter.cassandra.ClientRequest.RangeSlice.Unavailables.Count
brief: Count of range slice unavailables since server start
metric_type: cumulative
custom: false
---
### counter.cassandra.ClientRequest.RangeSlice.Unavailables.Count

Count of range slice unavailables since server start. A non-zero value
means that insufficient replicas were available to fulfil a range slice
request at the requested consistency level.

This typically means that one or more nodes are down. To fix this condition,
any down nodes must be restarted, or removed from the cluster.

