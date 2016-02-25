---
title: Memory Metrics
brief: Metrics collected about memory usage
---
### Memory Metrics

Use the `memory` plugin to monitor the following data:

* Free memory
* Used memory
* Buffered and cached memory
* Reclaimable and unreclaimable slab memory

Plugin reports memory usage in bytes.

| Metric name        |  Description                                                                   |
|--------------------|--------------------------------------------------------------------------------|
| memory.used        | Total amount of memory used                                                    |
| memory.free        | Total amount of unused memory                                                  |
| memory.buffered    | Amount of memory used for buffering, mostly for I/O operations                 |
| memory.cached      | Memory used for caching disk data for reads, memory-mapped files or tmpfs data |
| memory.slab_recl   | Amount of reclaimable memory used for slab kernel allocations                  |
| memory.slab_unrecl | Amount of unreclaimable memory used for slab kernel allocations                |

Total amount of memory should be calculated as used + free memory. All other metrics are included in either free
or used memory.

### Version information

| Software        | Version        |
|-----------------|----------------|
| collectd        |  1.0 or later  |
| memory plugin   |  1.0 or later  |
