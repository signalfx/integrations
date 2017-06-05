---
title: Stream Upstream Peer Health Check Unhealthy
brief: Total number of times a stream upstream server became unhealthy
metric_type: cumulative_counter
---
### Stream Upstream Peer Health Check Fails
The total number of times a stream upstream server entered the `unhealthy` state due to failed health checks.
This metric is reported with dimensions `stream.upstream.name` and `stream.upstream.peer.name` to indicate the name
of the upstream group and name of the individual server, respectively.
