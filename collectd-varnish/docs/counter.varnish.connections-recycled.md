---
title: Backend connection recycles
brief: Count of backend connection recycles
metric_type: cumulative counter
---
### Backend Connection Recycles

> Count of backend connection recycles

This counter is increased whenever we have a keep-alive
connection that is put back into the pool of connections.
It has not yet been used, but it might be, unless the backend
closes it.
