title | brief | metric_type
------|-------|------------
Number of Warning Nodes | Number of nodes for which health checks are reporting Warning state | gauge

### Number of Warning nodes
Number of nodes which health checks are reporting to be in Warning state. This metric is reported by leader only. This metric is reported with the dimension `datacenter`, `consul_node` name and `consul_mode`.