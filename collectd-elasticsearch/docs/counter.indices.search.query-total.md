---
title: Total Search Requests
brief: The total number of search requests since node startup
metric_type: counter
---
### Total Search Requests

> How many search requests have been servied by this node since it started.

This includes queries to both primary and replica shards. Queries run against an Elasticsearch cluster are executed on all the shards across all nodes in the cluster. This means that this metric doesn't map 1:1 to the number of queries issued by the client.
