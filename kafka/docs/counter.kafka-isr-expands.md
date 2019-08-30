---
title: kafka-isr-expands
brief: Increase in ISR of partitions
metric_type: counter
---
### kafka-isr-expands

When a broker is brought up after a failure, it starts catching up by reading from the leader. Once it is caught up, it gets added back to the ISR (in-sync-replicas).
