---
title: Disk Operations Metrics
brief: Metrics collected about disk operations.
---
### Disk Operation Metrics

This document describes disk operations metrics as reported by the [disk plugin for collectd](https://collectd.org/wiki/index.php/Plugin:Disk).

The metrics are reported per physical disk, and where supported, per partition.  The metrics measure the number of bytes, the number of operations, the number of merges, and the average time to execute.  In each case, they are measured separately for read and write operations.  On FreeBSD, the number of bytes read or written is the only metric available.

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  1.5 or later  |
