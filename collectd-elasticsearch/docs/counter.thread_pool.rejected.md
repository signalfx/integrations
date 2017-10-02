---
title: Rejected Thread Pool Requests
brief: Number of rejected thread pool requests
metric_type: counter
---
### Rejected Requests

> The number of requests that have been rejected per thread pool on this node since it started.


If the get request queue fills up to its limit, new work units will begin to be
rejected, and you will see that reflected in this rejected metric. This is
often a sign that your cluster is starting to bottleneck on some resources,
since a full queue means your node/cluster is processing at maximum speed but
unable to keep up with the influx of work.

Number of rejected requests for a given thread pool.  The represented thread pool is indicated by the dimension "thread_pool".


The following thread pools may be configured:

|Thread Pool|Description|Configured By Default|
|-----------|-----------|---------------------|
|bulk|The number of bulk requests that have been rejected on this node since it started.|False|
|force\_merge|The number of force merges that have been rejected on this node since it started|False|
|fetch\_shard\_started|The number of fetch\_shard\_started requests that have been rejected on this node since it started|False|
|fetch\_shard\_store|The number of fetch\_shard\_store requests that have been rejected on this node since it started|False|
|flush|The number of flush requests that have been rejected on this node since it started.|False|
|generic|The number of generic requests that have been rejected on this node since it started.|False|
|get|The number of get requests that have been rejected on this node since it started.|False|
|index|The number of index requests that have been rejected on this node since it started.|True|
|listener|The number of listener requests that have been rejected on this node since it started|False|
|management|The number of management requests that have been rejected on this node since it started|False|
|merge|The number of merge requests that have been rejected on this node since it started.|False|
|optimize|The number of optimize requests that have been rejected on this node since it started.|False|
|percolate|The number of percolate requests that have been rejected on this node since it started.|False|
|refresh|The number of refresh requests that have been rejected on this node since it started.|False|
|search|The number of search requests that have been rejected on this node since it started.|True|
|snapshot|The number of snapshot requests that have been rejected on this node since it started.|False|
|suggest|The number of suggest requests that have been rejected on this node since it started|False|
|warmer|The number of warmer requests that have been rejected on this node since it started|False|
