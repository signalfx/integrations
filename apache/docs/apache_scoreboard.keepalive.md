
---
title: apache_scoreboard.keepalive
brief: |
  The number of worker threads that are maintaining keep-alive connections: keeping the connection "alive" after serving a response, in the expectation that another HTTP request will come on the same connection
metric_type: gauge
custom: true
---
### apache_scoreboard.keepalive

The number of worker threads that are maintaining keep-alive connections: keeping the connection "alive" after serving a response, in the expectation that another HTTP request will come on the same connection. At the end of the keep-alive interval, the connection is closed.

