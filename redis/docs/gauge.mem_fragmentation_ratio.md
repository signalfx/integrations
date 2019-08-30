---
title: Memory fragmentation ratio
brief: Ratio between used_memory_rss and used_memory
metric_type: gauge
---

### Memory Fragmentation Ratio

> mem_fragmentation_ratio: Ratio between used_memory_rss and used_memory

Ideally, the used_memory_rss value should be only slightly higher than used_memory. When rss >> used, a large difference means there is memory fragmentation (internal or external), which can be evaluated by checking mem_fragmentation_ratio. When used >> rss, it means part of Redis memory has been swapped off by the operating system: expect some significant latencies.
