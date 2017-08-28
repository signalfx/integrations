title | brief | metric_type
------|-------|------------
Maximum Node Network Latency | Minimum network latency between given node and other nodes in the datacenter | gauge

### Minimum Node Network Latency
Minimum network latency between given node and other nodes in the datacenter. The dimension `consul_node` corresponds to the source node. The metric also has the dimensions `datacenter` and `consul_mode`.