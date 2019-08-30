---
title: ZooKeeper Packets Received
brief: Count of the number of ZooKeeper packets received by a server
metric_type: cumulative counter
---
### ZooKeeper Packets Received

> How many ZooKeeper packets have been received by a ZooKeeper server.

Use this metric to see how many packets are being received by a ZooKeeper server.

If the value of this metric on one server differs significantly from other servers:
* There might be a connection imbalance. Check the gauge.zk_num_alive_connections metric for this server to see if it also differs significantly from other servers.
* There might be an unbalanced number of requests being sent to this server. This can happen if clients are not sending the expected number of requests.
