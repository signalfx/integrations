title | brief | metric_type
------|-------|------------
Avg Time for Forward DNS Query | Average time to complete a forward DNS query | gauge

### Avg Time for Forward DNS Query 
This tracks how long it takes to service forward DNS lookups on the given Consul agent. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.