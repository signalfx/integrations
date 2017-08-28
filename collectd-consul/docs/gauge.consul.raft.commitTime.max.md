title | brief | metric_type
------|-------|------------
Max Raft Commit Time | Max of the time it takes to commit an entry on the leader | gauge

### Max Raft commit time
This measures the max time it takes to commit a new entry to the Raft log on the leader. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.