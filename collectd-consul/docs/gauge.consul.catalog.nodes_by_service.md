title | brief | metric_type
------|-------|------------
Number of Nodes by Service | Number of nodes providing a given service | gauge

### Number of Services by Node
Number of nodes providing a given service. This metric is reported by the leader only. The dimension `consul_service` indicates which service the metric corresponds too. Additionally, the metric also has the `datacenter` and `consul_mode` dimension.