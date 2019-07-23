---
title: Serf Member Flaps
brief: Tracks flapping agents
metric_type: gauge
---
### Member flaps
 This metric increments when an agent is marked dead and then recovers within a short time period. This can be an indicator of overloaded agents, network problems, or configuration errors where agents can not connect to each other on the required ports. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.