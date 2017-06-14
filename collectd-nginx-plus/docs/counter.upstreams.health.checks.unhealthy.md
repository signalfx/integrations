---
title: Upstream Peer Health Check Unhealthy
brief: Total number of times an upstream server became unhealthy
metric_type: cumulative_counter
---
### Upstream Peer Health Check Fails
The total number of times an upstream server entered the `unhealthy` state due to failed health checks.
This metric is reported with dimensions `upstream.name` and `upstream.peer.name` to indicate the upstream group name
and the individual server name.
