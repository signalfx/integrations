---
title: Throttling time
brief: Throttling time in nano seconds
metric_type: cumulative_counter
---
### Throttling time

(Optional metric) The amount of time (in nanoseconds) that a container is throttled. A container is throttled when it tries to use more than it's quota within a period. Docker reports 0 if there is no quota constraint on the container.
