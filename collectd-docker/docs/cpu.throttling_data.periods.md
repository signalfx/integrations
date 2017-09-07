---
title: Periods
brief: Number of periods
metric_type: cumulative_counter
---
### Periods

(Optional metric) A cumulative count of the total number of periods that have passed. A period is a measurement of time during which containers are allocated their CPU quota. If the period is set to 100,000 microseconds and a docker container is quoted 50,000 microseconds, then the container is allocated 50% of 1 CPU during a period. The default period length is 100,000 microseconds or 100 milliseconds. Docker reports 0 if there is no quota constraint on the container.
