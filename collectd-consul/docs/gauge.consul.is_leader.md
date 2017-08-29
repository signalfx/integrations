---
title: Server State
brief: Metric to map consul server's in leader or follower state
metric_type: gauge
---
### Server State
Metric to map consul server's in leader or follower state. A follower instance returns value of 0 and leader returns a value of 1. Used by a Heat Map in the dashboard which makes recognizing the leader from followers visually easy. This metric comes with the dimension - `consul_server_state` which can be either leader or follower. Also has the dimensions `datacenter`, `consul_node` and `consul_mode`.