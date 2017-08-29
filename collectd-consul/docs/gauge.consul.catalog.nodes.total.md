---
title: Number of Nodes
brief: Number of nodes in the Consul datacenter
metric_type: gauge
---
### Number of Nodes
The total number of nodes in the Consul datacenter. This metric is common to the cluster and, therefore, reported by leader only. This metric is reported with the dimension `datacenter`, `consul_node` name and `consul_mode` to indicate which mode - server or client - is the reporting consul agent.
