---
title: Log flush time ms 95
brief: 95th percentile of log flush time in milliseconds
metric_type: gauge
---
### Log Flush Time ms 95th

> 95th percentile of log flush time in milliseconds across all partitions on the broker.

Each Kafka partition has a log associated with it. Use this metric to find out how much time a log flush takes in 95% of cases.

If the value of this metric on one broker is higher than the others

* Check if this broker is getting more traffic (messages or bytes) than other brokers.
* If this broker is receiving a balanced amount of traffic, then the disks on that machine might have degraded. Check disk performance metrics on the broker and consider replacing it.
