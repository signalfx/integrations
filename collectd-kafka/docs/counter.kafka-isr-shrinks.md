---
title: kafka-isr-shrinks
brief: Decrease in ISR of partitions
metric_type: counter
---
### kafka-isr-shrinks

When a broker goes down, ISR (in-sync-replicas) for some of partitions will shrink. When that broker is up again, ISR will be expanded once the replicas are fully caught up. Other than that, the expected value for both ISR shrink rate and expansion rate is 0.
