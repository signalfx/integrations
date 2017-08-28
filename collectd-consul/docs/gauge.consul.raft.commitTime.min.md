title | brief | metric_type
------|-------|------------
Min Raft Commit Time | Minimum of the time it takes to commit an entry on the leader | gauge

### Min Raft commit time
This measures the minimum time it takes to commit a new entry to the Raft log on the leader. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.