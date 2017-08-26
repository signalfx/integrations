title | brief | metric_type
------|-------|------------
Number of Critical Nodes | Number of nodes for which health checks are reporting Critical state | gauge

### Number of Critical nodes
Number of nodes for which health checks are reporting Critical state. This metric is reported by leader only. This metric is reported with the dimension `datacenter`, `consul_node` name and `consul_mode`.