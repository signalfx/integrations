---
title: Size of Data
brief: Size of data in bytes that a ZooKeeper server has in its data tree
metric_type: gauge
---

### Size of Data

> The size in bytes of the data tree for a ZooKeeper server

Use this metric to keep track of the size of the data tree on a ZooKeeper server.

Any unexpected changes maybe caused by:
* A client writing or deleting data.
* A client disconnecting and ephemeral nodes being deleted as a result. Check to see if the gauge.zk_num_alive_connections metric for this server is also changing unexpected.
