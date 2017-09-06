---
title: Throttling time
brief: Throttling time in nano seconds
metric_type: cumulative_counter
---
### Throttling time

(Optional metric) Tracks the amount of time (in nanoseconds) a container is throttled for. A container is throttled when it tries to use more than it's quota in a period. Docker reports 0 if there is no quota constraint on the container.
