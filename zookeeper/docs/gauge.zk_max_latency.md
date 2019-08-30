---
title: Maximum Request Latency
brief: Maximum time in milliseconds for a request to be processed
metric_type: gauge
---

### Maximum Request Latency

> The maximum time it took this ZooKeeper server to process a request in milliseconds. This is measured
since the last restart of the ZooKeeper server.

If this metric is rising then one of the following may be true:
* There may be too many requests being sent to this server for its CPU capacity. Make sure there is enough CPU capacity for the ZooKeeper server on the server.
* This server may be unable to connect to other ZooKeeper servers. Look at logs on the server to see if they contain exceptions.
