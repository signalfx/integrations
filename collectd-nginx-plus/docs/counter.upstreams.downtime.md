---
title: Upstream Peer Downtime
brief: Total time the server was in the `unavail`, `checking`, and `unhealthy` states
metric_type: cumulative_counter
---
### Upstream Peer Downtime
The total time the server was in the `unavail`, `checking`, and `unhealthy` states. This metric is reported with
dimensions `upstream.name` and `upstream.peer.name` to indicate the upstream group name and the individual server name.
