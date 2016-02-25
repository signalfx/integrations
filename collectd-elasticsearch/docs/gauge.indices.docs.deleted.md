---
title: Number of Deleted Documents
brief: Number of deleted documents on this node
metric_type: gauge
---
### Number of Deleted Documents

> How many documents are currently deleted on this node.

Deleted documents are not cleaned up until merge happens. Elasticsearch merge policy may not favour the cleaning up of deleted documents. A high ratio of deleted documents may impact search performance and cache sizes.
