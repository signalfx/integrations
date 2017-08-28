---
title: Min Time to Append Entries
brief: Min time taken to complete the AppendEntries RPC
metric_type: gauge
---
### Min Time to Append Entries
This measures the minimum time it takes to replicate log entries to followers. This is a general indicator of the load pressure on the Consul servers, as well as the performance of the communication between the servers. This metric is sent by the leader for each follower. The metric has the followers ip or hostname added to the metric name. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.