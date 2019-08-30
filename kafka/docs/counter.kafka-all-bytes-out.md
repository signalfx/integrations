---
title: Bytes out
brief: Number of bytes transmitted per second across all topics
metric_type: cumulative counter
---
### Bytes Oout

> Number of bytes transmitted per second across all topics.

Use this metric to find out how many bytes each Kafka broker is transmitting.
Bytes are transmitted to both consumers and to replicas.

This metric usually increases when:
* New Kafka instances have come online and partitions are being synced to them.
* New consumers have come online and are requesting more data.
