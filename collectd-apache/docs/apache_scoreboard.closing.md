---
title: Apache Scoreboard Closing
brief: Number of workers in the process of closing connections
metric_type: gauge
---
### Apache Scoreboard Closing

This metric shows how many worker threads are in the process of closing TCP connections after serving a response. If this number is consistently high, then there might be a network issue or errant client preventing TCP tear-down.
