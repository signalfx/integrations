title | brief | metric_type
------|-------|------------
Average Raft Commit Time | Average of the time it takes to commit an entry on the leader | gauge

### Average Raft commit time
This measures the mean time it takes to commit a new entry to the Raft log on the leader. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.