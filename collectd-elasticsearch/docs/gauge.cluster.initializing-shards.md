---
title: Number of Initializing Shards
brief: The number of currently initializing shards
metric_type: gauge
---
### Number of Initializing Shards

> How many shards are currently being initialized.

This is a count of shards that are being freshly created. For example, when you first create an index, the shards will all briefly reside in initializing state. This is typically a transient event, and shards shouldn’t linger in this state too long. You may also see initializing shards when a node is first restarted: as shards are loaded from disk, they start as initializing.
