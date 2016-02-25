---
title: Number of Unassigned Shards
brief: The number of shards that are currently unassigned
metric_type: gauge
---
### Number of Unassigned Shards

> How many shards are currently unassigned.

These are shards that exist in the cluster state, but cannot be found in the cluster itself. A common source of unassigned shards is unassigned replicas. For example, an index with five shards and one replica will have five unassigned replicas in a single-node cluster. Unassigned shards will also be present if your cluster is red (since primaries are missing).
