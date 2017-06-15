---
title: Cache Bypass Bytes
brief: Total bytes read from an origin server due to a `proxy_cache_bypass` directive
metric_type: cumulative_counter
---
### Cache Bypass Bytes
The total number of bytes read from an origin server rather than the cache due to a matching `proxy_cache_bypass` directive.
This metric is reported with the dimension `cache.name` to indicate the name of the cache.
