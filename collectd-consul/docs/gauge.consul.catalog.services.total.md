---
title: Number of Registered Services
brief: Total number of services registered with Consul in the given datacenter
metric_type: gauge
---
### Number of Registered Services
The total number of services registered with Consul in the given datacenter. This metric is common to the cluster and, therefore, reported by leader only. This metric is reported with the dimension `datacenter`, `consul_node` name and `consul_mode` to indicate which mode - server or client - is the reporting consul agent.