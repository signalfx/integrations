---
title: Master replication offset
brief: Master replication offset
metric_type: gauge
---

### Master Replication Offset

> master_repl_offset: target offset of master dataset

Use this metric to and compare with slave_repl_offset on slaves to figure out how replication is doing.  if slave_repl_offset on slave host is behind its  master's master_repl_offset, you know you have a replication problem.
