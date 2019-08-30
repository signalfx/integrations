---
title: Dead rows
brief: Number of dead rows in the database
metric_type: gauge
---

### Dead Rows

This metric shows how many dead rows in the database. Rows that are deleted or obsoleted by an update are not physically removed from their table; they remain present as dead rows until a VACUUM is done.
