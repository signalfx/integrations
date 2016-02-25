---
title: Cluster Status
brief: The health status of the cluster
metric_type: gauge
---
### Cluster Status

> Whether the cluster is green, yellow or red.

This gauge can have three different values:
 * 0, meaning green: all primary and replica shards are allocated. Your cluster is 100% operational.
 * 1, meaning yellow: all primary shards are allocated, but at least one replica is missing. No data is missing, so search results will still be complete. However, your high availability is compromised to some degree. If more shards disappear, you might lose data. Think of yellow as a warning that should prompt investigation.
 * 2, meaning red: at least one primary shard (and all of its replicas) are missing. This means that you are missing data: searches will return partial results, and indexing into that shard will return an exception.
