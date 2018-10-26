# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_collectd.png) Protocols

Metadata associated with the Protocols collectd plugin can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-protocols">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/protocols.c">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:Protocols">collectd wiki</a>:

The Protocols plugin collects information about the network protocols supported by the system, for example Internet Protocol (IP) and Transmission Control Protocol (TCP). Currently the plugin is only available under Linux and reads its information from the following two files in the /proc file-system:

* `/proc/net/snmp`
* `/proc/net/netstat`

Because the available information is usually far too much to be useful, the interesting values can be selected using the configuration file.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd | 4.7+ |

### INSTALLATION

**If you are using the new Smart Agent, see the docs for [the collectd/protocols
monitor](https://github.com/signalfx/signalfx-agent/tree/master/docs/monitors/collectd-protocols.md)
for more information.  The configuration documentation below may be helpful as
well, but consult the Smart Agent repo's docs for the exact schema.**


Installation and initial configuration options are available as part of the <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd">SignalFx collectd agent</a>.


### CONFIGURATION

Configuration for this plugin is kept in the main <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/collectd/collectd.conf">collectd.conf</a> file.

From <a target="_blank" href="https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_protocols">collectd wiki</a>:

| Configuration Option | Type | Definition |
|----------------------|------|------------|
| `Value` | _Selector_ | Selects whether or not to select a specific value. <ul><li>The string being matched is of the form `Protocol:ValueName` where `Protocol` will be used as the plugin instance and `ValueName` will be used as type instance. </li><li> An example of the string being used would be `Tcp:RetransSegs` </li><li> You can use regular expressions to match a large number of values with just one configuration option. </li><li> To select all "extended" TCP values, you could use the following statement: `Value "/^TcpExt:/"` </li><li> Whether only matched values are selected or all matched values are ignored depends on the **IgnoreSelected**. By default, only matched values are selected. If no value is configured at all, all values will be selected.</li></ui> |
| `IgnoreSelected` | _true/false_ | If set to true, inverts the selection made by `Value`, i. e. all matching values will be ignored. |


### USAGE

This is a plugin used to gather data about specific protocols in use by a host or collectd instance. By default the protocols that the SignalFx configuration gather metrics on are:

| `Value` | default | Definition |
|----------------------|------|------------|
| Icmp |`Icmp:InDestUnreachs`| |
|Tcp|`Tcp:CurrEstab`| The number of TCP connections for which the current state is either ESTABLISHED or CLOSE- WAIT. |
|Tcp| `Tcp:OutSegs` | The total number of segments that have been sent, including those on current connections but excluding those containing only retransmitted octets. |
|Tcp | `Tcp:RetransSegs` | The total number of TCP segments that have been transmitted containing one or more previously transmitted octets. |
|TcpExt | `TcpExt:DelayedACKs` | delayed acknowledgements |
|Tcp | `Tcp:.*Opens/`|  To select all TCP values with an extension including the variable `Opens`|
|TcpExt| `/^TcpExt:.*Octets/` |To select all "extended" TCP values with an extension including the variable `Octets` |


### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

License for this plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/protocols.c">in the header of the plugin</a>
