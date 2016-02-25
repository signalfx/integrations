---
title: Request queue size
brief: Number of requests in the request queue across all partitions on the broker
metric_type: gauge
---
### Request Queue Size

> Number of requests in the request queue across all partitions on the broker.

If this number is consistently high or growing in size, then the broker is unable to keep up with incoming requests. 

* The broker may be overloaded. Check the CPU and memory usage on the broker to see if it does not have enough resources.
* Check the metric gauge.kafka-log-flush-time-ms-p95 to find out if log flush time has increased, causing requests to take longer to process. 
