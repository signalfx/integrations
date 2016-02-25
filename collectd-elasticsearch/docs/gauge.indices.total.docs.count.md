---
title: Number of Documents
brief: Number of documents in the cluster
metric_type: gauge
---
### Number of Documents

> How many documents are currently in this cluster.

This metric tracks the number of documents that are currently stored in the cluster. This includes primary and replica shards. This also includes documents that may actually be deleted but have not been cleaned up yet (through a merge). This metric is also available per index.
