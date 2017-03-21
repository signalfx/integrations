---
title: Network total
brief: Total amount of inbound and outbound network traffic on this host, in bytes.
metric_type: cumulative_counter
---
### Network total

This metric shows the total amount of inbound and outbound network traffic on this host, in bytes. 

The SignalFx metadata plugin computes this metric based on the network traffic metrics output by the `interface` plugin for collectd and the `net` plugin for Telegraf as follows, initially summing all metrics by host:

collectd
```
if_octets.rx + if_octets.tx
```

Telegraf
```
net.bytes_recv + net.bytes_sent
```