---
title: Number of Z-Nodes
brief: Number of z-nodes that a ZooKeeper server has in its data tree
metric_type: gauge
---

### Number of Z-Nodes

> The number of unique z-nodes on a ZooKeeper server has in it's data tree

Use this metric to keep track of the number of z-nodes on a ZooKeeper server.

Any unexpected changes may be caused by:
* A client deleting or creating new nodes. Check that clients are not acting unexpectedly.
* A client disconnecting and ephemeral nodes being deleted. Check to see if the gauge.zk_ephemerals_count for this server has decreased unexpectedly.
