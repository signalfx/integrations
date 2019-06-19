---
title: Leadership Transitions
brief: Tracks the number of leadership transitions per interval
metric_type: gauge
---
### Leadership Transitions
This metric increments whenever a Consul server becomes a leader. If there are frequent leadership changes this may be indication that the servers are overloaded and aren't meeting the soft real-time requirements for Raft, or that there are networking problems between the servers. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.