---
title: Error request
brief: Corresponds to HAProxy's `ereq` metric -  Request errors.
metric_type: cumulative counter
---
### Error request

Corresponds to HAProxy's `ereq` metric -  Request errors. Some of the possible causes are:
     - early termination from the client, before the request has been sent.
     - read error from the client
     - client timeout
     - client closed connection
     - various bad requests from the client.
     - request was tarpitted.
