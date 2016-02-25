---
title: Number of underreplicated partitions
brief: Number of underreplicated partitions across all topics on the broker
metric_type: gauge
---
### Number of Underreplicated Partitions

> Number of partitions that are under replicated, for which this broker is the leader.

Each topic has a configured number of brokers that its partitions should be replicated to. A non-zero value for this metric means that a broker is having trouble talking to other broker(s) for partition replication. This increases the risk of losing data that has been acknowledged as committed. 
