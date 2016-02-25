---
title: Number of Open File Descriptors
brief: Number of file descriptors that a ZooKeeper server has open
metric_type: gauge
---

### Number of Open File Descriptors

> The number of file descriptors a ZooKeeper server has open.

Use this metric to keep track of open file descriptors in a ZooKeeper process.

If this number is too high then ZooKeeper will stop accepting connections from clients.
Compare this metric to gauge.zk_max_file_descriptor_count to figure out how close you are to file descriptor capacity.

File descriptor counts grow with:
* The number of clients connected
* The number of data files on disk
