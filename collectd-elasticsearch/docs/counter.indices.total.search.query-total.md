---
title: Total Search Requests
brief: The total number of search requests per cluster
metric_type: counter
---
### Total Search Requests

> How many search requests have been serviced by the cluster.

This includes queries to both primary and replica shards across the entire cluster. Queries that run against an Elasticsearch cluster are executed on all the shards across all nodes in the cluster. Therefore, this metric doesn't map 1:1 to the number of queries issued by the client.
