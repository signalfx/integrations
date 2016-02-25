---
title: Outstanding requests
brief: Number of currently executing requests
metric_type: gauge
---

### Outstanding Requests

> The instantaneous number of requests on a ZooKeeper server that have started but have not finished yet.

If this metric is climbing:
* There may be too many requests being sent to this server for its CPU capacity. Check CPU capacity on your ZooKeeper cluster and make sure that this server is not receiving a disproportionate number of requests relative to other servers.
* This server may be unable to connect to other ZooKeeper servers. Look at logs on the server to see if they contain exceptions.
