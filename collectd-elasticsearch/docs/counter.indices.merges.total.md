---
title: Total Merges
brief: Total number of merges since node startup
metric_type: counter
---
### Total Merges

> The number of merges that happened on this node since it started.

Node merges happen every time the index is refreshed due to changes made to it. Elasticsearch's segments are immutable, and merges group together smaller segments into bigger ones. This metric tracks merges across all indexes that exist on the node.
