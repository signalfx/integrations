---
title: Garbage Collector Time
brief: Total garbage collection time (milliseconds)
metric_type: counter
---
### Garbage Collector Time

> Total time in milliseconds spent in garbage collection since the node has started.

This counter will increase after garbage collections. If its rate spikes, it may indicate memory pressure on the system since the JVM is trying to free up memory by running bigger and more frequent garbage collections.
