---
title: Messages in
brief: Number of messages received per second across all topics
metric_type: cumulative counter
---
### Messages In

> Number of messages received per second across all topics.

Use this metric to find out how many messages each Kafka broker is receiving.

If the value of this metric on one broker differs significantly from other brokers:

* This broker may have a disproportionately high number of Kafka topic partitions. Check gauge.kafka-log-flush-time-ms-p95 to see if log latency is particularly high on the brokers getting more messages.
* Some topics or partitions might be receiving more traffic than others. Consider rebalancing the partitions across brokers so that all brokers have similar levels of log flush latency and CPU utilization.
