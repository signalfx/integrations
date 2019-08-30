---
title: Buffer hits
brief: Number of buffer hits
metric_type: gauge
---

### Buffer Hits

This metric shows how many read operations were served from the buffer in memory, so that a disk read was not necessary. This only includes hits in the PostgreSQL buffer cache, not the operating system's file system cache.
