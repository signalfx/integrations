---
title: Apache Scoreboard Keep-Alive
brief: Number of keep-alive connections
metric_type: gauge
---
### Apache Scoreboard Keep-Alive

The number of worker threads that are maintaining keep-alive connections: keeping the connection "alive" after serving a response, in the expectation that another HTTP request will come on the same connection. At the end of the keep-alive interval, the connection is closed.
