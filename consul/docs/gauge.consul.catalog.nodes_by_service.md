---
title: Number of Nodes by Service
brief: Number of nodes providing a given service
metric_type: gauge
---
### Number of Services by Node
Number of nodes providing a given service. This metric is reported by the leader only. The dimension `consul_service` indicates which service the metric corresponds too. Additionally, the metric also has the `datacenter` and `consul_mode` dimension.