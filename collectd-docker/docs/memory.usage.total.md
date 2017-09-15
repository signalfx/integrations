---
title: Memory usage
brief: Bytes of memory used by the container
metric_type: gauge
---
### Memory usage

This metrics reports the current memory (RAM) usage of the container, in bytes. A memory utilization percentage can be calculated against the `memory.usage.limit` metric:

```
Memory usage % = 100 * memory.usage.total / memory.usage.limit
```
