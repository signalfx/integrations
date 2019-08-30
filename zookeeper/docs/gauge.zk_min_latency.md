---
title: Minimum Request Latency
brief: Minimum time in milliseconds for a request to be processed
metric_type: gauge
---

### Minimum Request Latency

> The minimum time it took this ZooKeeper server to process a request in milliseconds. This is measured since the last restart of this ZooKeeper server.

If this metric is rising then one of the following may be true:
* There may be too many requests being sent to this server for its CPU capacity. Make sure there is enough CPU capacity for the ZooKeeper Server on the server.
* This server may be unable to connect to other ZooKeeper servers. Look at logs on the server to see if they contain exceptions.
