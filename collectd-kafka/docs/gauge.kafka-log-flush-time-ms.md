---
title: Log flush time ms
brief: Average number of milliseconds to flush a log
metric_type: gauge
---
### Log Flush Time ms

> Average number of milliseconds to flush logs across all partitions on the broker.

Each Kafka partition has a log associated with it. Use this metric to find out the average time a log flush takes.

If the value of this metric on one broker is higher than the others

* Check if this broker is getting more traffic (messages or bytes) than other brokers.
* If this broker is receiving a balanced amount of traffic, then the disks on that machine might have degraded. Check disk performance metrics on the broker and consider replacing it.
