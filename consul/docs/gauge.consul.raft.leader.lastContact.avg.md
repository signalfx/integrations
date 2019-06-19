---
title: Average Leader Last Contact
brief: Mean of the time since the leader was last able to contact follower nodes
metric_type: gauge
---
### Average Leader Last Contact
This measures the time since the leader was last able to contact the follower nodes when checking its leader lease. It can be used as a measure for how stable the Raft timing is and how close the leader is to timing out its lease. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.