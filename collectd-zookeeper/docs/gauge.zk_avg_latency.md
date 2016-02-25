---
title: Average Request Latency
brief: Average time in milliseconds for requests to be processed
metric_type: gauge
---

### Average Request Latency

> How long on average it takes for this ZooKeeper server to process a request in milliseconds. This is
measured since the last restart of the ZooKeeper server.

If this metric is continuously rising then one of the following may be true:
* There may be too many requests being sent to this server for its CPU capacity. Make sure there is enough CPU capacity for the ZooKeeper Server on the server.
* This server may be having an issue connecting to other ZooKeeper servers. Look at logs on the server to see if they contain exceptions.
