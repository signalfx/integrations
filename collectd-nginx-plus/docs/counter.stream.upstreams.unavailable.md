---
title: Stream Upstream Peer Unavailable
brief: Number of times a stream upstream server server became unavailable for client connections
metric_type: cumulative_counter
---
### Stream Upstream Peer Unavailable
The total number of times the server became unavailable for client connections due to the number of unsuccessful
attempts reaching the `max_fails` threshold. This metric is reported with dimensions
`stream.upstream.name` and `stream.upstream.peer.name` to indicate the name of the upstream group and name of the
individual server, respectively.
