---
title: Networking metrics
brief: Networking metrics, primarily about TCP.
---
### Networking metrics

This is set of metrics collected by the `protocols` plugin for collectd. The following metrics are included in SignalFx's default configuration for this plugin:


| Metric                          | Protocol | PluginInstance | Meaning        |
|---------------------------------|----------|----------------|----------------|
| protocol_counter.InDestUnreachs | ICMP     | Icmp           | The number of ICMP Destination Unreachable messages received |
| protocol_counter.CurrEstab      | TCP      | Tcp            | The number of TCP connections for which the current state is either ESTABLISHED or CLOSE- WAIT |
| protocol_counter.RetransSegs    | TCP      | Tcp            | The total number of segments retransmitted |
| protocol_counter.OutSegs        | TCP      | Tcp            | The total number of segments sent, excluding those containing only retransmitted octets |
| protocol_counter.ActiveOpens    | TCP      | Tcp            | The number of times TCP connections have made a direct transition to the SYN-SENT state from the CLOSED state |
| protocol_counter.PassiveOpens   | TCP      | Tcp            | The number of times TCP connections have made a direct transition to the SYN-RCVD state from the LISTEN state |
| protocol_counter.DelayedACKs    | TCP      | TcpExt         | The total number of acknowledgements which were pending because of waiting for other package, but were sent after timeout occurred |


### Configuration
SignalFx's default configuration for collectd includes the metrics listed above. You can configure this plugin to collect additional metrics by modifying the `<Plugin "protocols">` section of collectd.conf. Available additional metrics include the output of the following commands:

`cat /proc/net/snmp`
`cat /proc/net/netstat`

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.7 or later  |

### Useful links

* [collectd protocols plugin](https://collectd.org/wiki/index.php/Plugin:Protocols)
* For TCP metrics not defined here, refer to [Description of TCP metrics as collected by Diamond](https://github.com/BrightcoveOS/Diamond/wiki/collectors-TCPCollector)
