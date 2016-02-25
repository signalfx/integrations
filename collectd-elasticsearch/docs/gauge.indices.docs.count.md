---
title: Number of Documents
brief: Number of documents on this node
metric_type: gauge
---
### Number of Documents

> How many documents are currently on this node.

This metric tracks the number of documents that are currently stored on this node. This includes primary and replica shards. This also includes documents that may actually be deleted but have not been cleaned up yet (through a merge).
