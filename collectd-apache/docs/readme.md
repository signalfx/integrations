---
title: Apache Web Server Metrics
brief: Metrics collected from Apache Web Server.
---
### Apache Web Server Metrics

Use the [Apache collectd plugin](https://collectd.org/wiki/index.php/Plugin:Apache) to collect metrics about Apache Web Server.  This plugin collects metrics from the module `mod_status`. 

Apache worker threads can be in one of the following states: 

| State        | Remark                                  |
|--------------|-----------------------------------------|
| Open         | Open (unused) slot - no process         |
| Waiting      | Idle and waiting for request            |
| Sending      | Serving response                        |
| KeepAlive    | Kept alive for possible next request    |
| Idle_cleanup | Idle and marked for cleanup             |
| Closing      | Closing connection                      |
| Logging      | Writing to log file                     |
| Reading      | Reading request                         |
| Finishing    | Finishing as part of graceful shutdown  |
| Starting     | Starting up to serve                    |

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  3.9 or later  |
