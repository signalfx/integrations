---
title: Number of Stale DNS Queries 
brief: Number of times an agent serves a DNS query with stale information
metric_type: gauge
---
### Number of Stale DNS Queries
Number of times an agent serves a DNS query based on information from a server that is more than 5 seconds out of date. This metric has the dimensions `datacenter`, `consul_node` and `consul_mode`.