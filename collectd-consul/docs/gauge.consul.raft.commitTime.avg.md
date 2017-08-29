---
title: Average Raft Commit Time
brief: Average of the time it takes to commit an entry on the leader
metric_type: gauge
---
### Average Raft commit time
This measures the mean time it takes to commit a new entry to the Raft log on the leader. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.