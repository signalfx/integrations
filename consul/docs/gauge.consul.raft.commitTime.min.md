---
title: Min Raft Commit Time
brief: Minimum of the time it takes to commit an entry on the leader
metric_type: gauge
---
### Min Raft commit time
This measures the minimum time it takes to commit a new entry to the Raft log on the leader. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.