---
title: Committed Heap
brief: Total heap committed by the process (bytes)
metric_type: gauge
---
### Committed Heap

> The size of the heap that has been committed and is actually allocated to the process.

This tracks the maximum size that can be used before the JVM tries to allocate more memory for the process (unless it reaches the maximum configured).
