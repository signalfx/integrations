# ![](./img/integrations_azurerediscaches.png) Microsoft Azure Redis Cache

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Azure Redis Cache via [Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

#### FEATURES

##### Built-in dashboards

- **Azure Redis Cache**: Shows metrics of a Redis cahce.

  [<img src='./img/redis.1.png' width=200px>](./img/redis.1.png)

  [<img src='./img/redis.2.png' width=200px>](./img/redis.2.png)

- **Azure Redis Caches**: Shows metrics of all Redis cahces being monitored.

  [<img src='./img/redis.all.png' width=200px>](./img/redis.1.png)

### INSTALLATION

To access this integration, [connect to Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

### USAGE

#### Interpreting Built-in dashboards

**Azure Redis Cache**

- **Cache Hit Rate Percent** - Cache hit rate percent for each of the shards in the cache.

  [<img src='./img/cache.hit.rate.png' width=200px>](./img/cache.hit.rate.png)

- **Cache Hit Rate Trend** - Cache hit rate trend for each of the shards in the cache.

  [<img src='./img/cache.hit.rate.trend.png' width=200px>](./img/cache.hit.rate.trend.png)

- **Server Load** - Server load percent for each of the shards in the cache.

  [<img src='./img/cache.server.load.png' width=200px>](./img/cache.server.load.png)

- **CPU percent** - Percentage of CPU used by each of the shards in the cache.

  [<img src='./img/cache.cpu.percent.png' width=200px>](./img/cache.cpu.percent.png)

- **Number of Connections** - Number of connections to each of the shards in the cache.

  [<img src='./img/cache.connections.png' width=200px>](./img/cache.connections.png)

- **Memory Fragmentation Ratio** - Memory fragmentation ratio of the cache. Ideally this value should be around 1.

  [<img src='./img/cache.mem.ratio.png' width=200px>](./img/cache.mem.ratio.png)

- **Used RSS Memory** - RSS memory used by each shard.

  [<img src='./img/cache.used.rss.memory.png' width=200px>](./img/cache.used.rss.memory.png)

- **Used Memory** - Memory used by each shard.

  [<img src='./img/cache.used.memory.png' width=200px>](./img/cache.used.memory.png)

- **Total Keys** - Total number of keys on each of the shards.

  [<img src='./img/cache.total.keys.png' width=200px>](./img/cache.total.keys.png)

- **Evicted Keys** - Number of keys evicted due to lack of space from each of the shards.

  [<img src='./img/cache.evicted.keys.png' width=200px>](./img/cache.evicted.keys.png)

- **Expired Keys** - Number of keys expired from each of the shards.

  [<img src='./img/cache.expired.keys.png' width=200px>](./img/cache.expired.keys.png)

- **Total Commands Processed** - Number of commands processed by each of the shards.

  [<img src='./img/cache.total.commands.png' width=200px>](./img/cache.total.commands.png)

- **Get Commands** - Number of get commands processed by each of the shards.

  [<img src='./img/cache.get.commands.png' width=200px>](./img/cache.get.commands.png)

- **Set Commands** - Number of set commands processed by each of the shards.

  [<img src='./img/cache.set.commands.png' width=200px>](./img/cache.set.commands.png)

- **Cache Reads** - Number of cache reads by each of the shards.

  [<img src='./img/cache.reads.png' width=200px>](./img/cache.reads.png)

- **Cache Writes** - Number of cache writes by each of the shards.

  [<img src='./img/cache.writes.png' width=200px>](./img/cache.writes.png)

**Azure Redis Caches**

- **Number of Caches** - Total number of caches being monitored.

  [<img src='./img/caches.count.png' width=200px>](./img/caches.count.png)

- **Lowest Cache Hit Rates** - Caches with the lowest hit rates.

  [<img src='./img/caches.lowest.hit.rate.png' width=200px>](./img/caches.lowest.hit.rate.png)

- **Number of Connections** - Number of connections stacked per cache.

  [<img src='./img/caches.connections.png' width=200px>](./img/caches.connections.png)

- **Used Memory per Cache** - Memory used stacked by cache.

  [<img src='./img/caches.used.memory.png' width=200px>](./img/caches.used.memory.png)

- **Total Keys per Cache** - Number of keys, stacked by cache.

  [<img src='./img/caches.total.keys.png' width=200px>](./img/caches.total.keys.png)

- **Total Keys** - Total number of keys stored across all caches.

  [<img src='./img/caches.keys.png' width=200px>](./img/caches.keys.png)




### METRICS

For more information about the metrics emitted by Azure Redis Cache, visit <a target="_blank" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-supported-metrics#microsoftcacheredis">here</a>.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
