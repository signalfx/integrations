---
title: Stream Upstream Peer Max Connections
brief: Maximum number of simultaneous connections to a stream upstream server
metric_type: cumulative_counter
---
### Stream Upstream Max Connections
The maximum number of simultaneous connections to a single stream upstream server. This metric is reported
with dimensions `stream.upstream.name` and `stream.upstream.peer.name` to indicate the name of the upstream group
and name of the individual server, respectively.
