---
title: Minimum Datacenter Latency
brief: Minimum network latency between 2 datacenters
metric_type: gauge
---
### Minimum Datacenter Latency
Minimum datacenter latency between 2 datacenters. This metric has the additional dimension `destination_dc` dimension. The latency is calculated between this destination datacenter and the agent's datacenter given by the `datacenter` dimension. Only the leader in the source datacenter calculates this metric. The metric also has the dimensions `consul_mode` and `consul_node`.