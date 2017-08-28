---
title: Number of Suspect Messages
brief: Number of suspect messages received per interval
metric_type: gauge
---
### Number of Suspect Messages
This increments when an agent suspects another as failed when executing random probes as part of the gossip protocol. These can be an indicator of overloaded agents, network problems, or configuration errors where agents can not connect to each other on the required ports. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.