title | brief | metric_type
------|-------|------------
Leader Reconcilation Time | Leader time to reconcile the differences between Serf membership and Consul's store. | gauge

### Leader Reconcilation Time
Time it takes the leader to reconcile the differences between Serf membership and Consul's store. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.