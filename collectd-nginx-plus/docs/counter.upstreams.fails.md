---
title: Upstream Peer Failed Connections
brief: Total failed attempts to communicate with an upstream server
metric_type: cumulative_counter
---
### Upstream Peer Failed Connections
The total number of unsuccessful attempts to communicate with a single upstream server. This metric is reported with
dimensions `upstream.name` and `upstream.peer.name` to indicate the upstream group name and the individual server name.
