---
title: Number of Active Clients
brief: Number of active clients connected to a ZooKeeper server
metric_type: gauge
---

### Number of Active Clients

> The number of active clients connected to a ZooKeeper server.

An active client is one that is sending in regular heartbeat messages.

Use this metric to keep track of the number of clients on a ZooKeeper server.
For example, this metric will show you if one server in a ZooKeeper cluster has more clients than the others.

Any unexpected changes may be caused by:
* Networking issues such as dropped packets or large network latency.
* Clients disconnecting or reconnecting.
