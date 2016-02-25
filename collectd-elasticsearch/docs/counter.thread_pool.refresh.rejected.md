---
title: Rejected Refresh Requests
brief: Number of rejected refresh requests
metric_type: counter
---
### Rejected Refresh Requests

> The number of refresh requests that have been rejected on this node since it started.

If the refresh request queue fills up to its limit, new work units will begin to be rejected, and you will see that reflected in this rejected metric. This is often a sign that your cluster is starting to bottleneck on some resources, since a full queue means your node/cluster is processing at maximum speed but unable to keep up with the influx of work.
