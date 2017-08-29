---
title: Raft Candidate State
brief: Tracks the number of times given node enters the candidate state
metric_type: gauge
---
### Raft Candidate State
Tracks the number of times given node enters the candidate state, i.e., the number of times the Consul server starts a leader election. If this increments without a leadership change occurring it could indicate that a single server is overloaded or is experiencing network connectivity issues. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.