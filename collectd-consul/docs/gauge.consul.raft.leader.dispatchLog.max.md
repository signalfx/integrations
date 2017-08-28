title | brief | metric_type
------|-------|------------
Max Disk Commit Time | Maximum of the time it takes for the leader to write log entries to disk | gauge

### Min Disk Commit Time
This measures the maximum time it takes for the leader to write log entries to disk. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.