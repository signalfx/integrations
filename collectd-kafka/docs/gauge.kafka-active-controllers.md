---
title: Active controllers
brief: Specifies if the broker an active controller
metric_type: gauge
---
### Active Controllers

> Set to 1 if the broker is an active controller, 0 otherwise.

For each independent Kafka cluster there should be a single broker which is the active controller at any time.
The sum of this metric across all brokers in any given cluster should be one.
