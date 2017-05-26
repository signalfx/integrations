---
title: Stream Upstream Peer Connections
brief: Total number of connections forwarded to a stream upstream server
metric_type: cumulative_counter
---
### Stream Upstream Connections
The total number of client connections forwarded to a single stream upstream server. This metric is reported
with dimensions `stream.upstream.name` and `stream.upstream.peer.name` to indicate the name of the upstream group
and name of the individual server, respectively.
