title | brief | metric_type
------|-------|------------
Min Disk Commit Time | Minimum of the time it takes for the leader to write log entries to disk | gauge

### Min Disk Commit Time
This measures the minimum time it takes for the leader to write log entries to disk. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.