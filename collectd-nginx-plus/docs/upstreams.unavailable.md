---
title: Upstream Peer Unavailable
brief: Number of times an upstream peer server became unavailable for client connections
metric_type: cumulative_counter
---
### Upstream Peer Unavailable
The total number of times the server became unavailable for client connections due to the number of unsuccessful
attempts reaching the `max_fails` threshold. This metric is reported with dimensions
`upstream.name` and `upstream.peer.name` to indicate the upstream group name and the individual server name.
