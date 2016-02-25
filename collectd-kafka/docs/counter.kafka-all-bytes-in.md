---
title: Bytes in
brief: Number of bytes received per second across all topics
metric_type: cumulative counter
---
### Bytes In

> Number of bytes received per second across all topics.

Use this metric to find out how many bytes each Kafka broker is receiving.
The more bytes a broker receives, the more work it has to do to flush them to its logs.

If the value of this metric on one server differs significantly from other servers:

* Kafka partitions are not balanced properly across brokers. Check gauge.kafka-log-flush-time-ms-p95 to see if log latency is particularly high on the brokers processing more bytes.
* If the partitions are balanced across messages, some of the topics might have bigger messages than the others.
