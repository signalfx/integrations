---
title: ZooKeeper Packets Sent
brief: Count of the number of ZooKeeper packets sent from a server
metric_type: cumulative counter
---
### ZooKeeper Packets Sent

> How many ZooKeeper packets have been sent from a ZooKeeper server.

Use this metric to see how many packets are being sent from a ZooKeeper server.

If this metric is significantly different than other servers:
* There might be a connection imbalance. Check the gauge.zk_num_alive_connections metric for this server to see if it also differs significantly from other servers.
* There might be an unbalanced number of requests being sent to this server. Check the gauge.zk_packets_received metric for this server to see if it also differs significantly from other servers.
