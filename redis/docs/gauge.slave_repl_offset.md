---
title: Slave replication offset
brief: Slave replication offset
metric_type: gauge
---

### Slave Replication Offset

> slave_repl_offset: How much has the slave replicated

Use this metric to and compare with master_repl_ofset on masters to figure out how replication is doing.

If this metric is significantly different than master:

* There could be a replications problem
