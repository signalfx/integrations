---
title: Number of Ephemeral Z-Nodes
brief: Number of ephemeral nodes that a ZooKeeper server has in its data tree
metric_type: gauge
---

### Number of Ephemeral Z-Nodes

> The number of unique ephemeral z-nodes on a ZooKeeper server.

Use this metric to keep track of the number of ephemeral z-nodes on a ZooKeeper server.

Any unexpected changes may be caused by:
* A client deleting or creating new ephemeral nodes.
* A client disconnecting and ephemeral nodes being deleted as a result. Check to see if the gauge.zk_num_alive_connections.md metric for this server is decreasing unexpectedly.
