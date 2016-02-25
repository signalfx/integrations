---
title: Number of Watches
brief: Number of watches placed on Z-Nodes on a ZooKeeper server
metric_type: gauge
---

### Number of Watches

> The number of watches on z-nodes on a ZooKeeper server.

Use this metric to keep track of the number of z-node watches on a ZooKeeper server.

Any unexpected changes may be caused by:
* A client creating or deleting new watches. Check that clients are not acting unexpectedly.
* A client disconnecting. This will remove that client's watches. Confirm this by checking the gauge.zk_num_alive_connections metric for this server.
