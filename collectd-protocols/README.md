---
title: Protocols collectd Plugin
brief: Protocols plugin for collectd.
---

#![](https://github.com/signalfx/Integrations/blob/master/collectd/img/integrations_collectd.png) Protocols collectd Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Protocols):

The Protocols plugin collects information about the network protocols supported by the system, for example Internet Protocol (IP) and Transmission Control Protocol (TCP). Currently the plugin is only available under Linux and reads its information from the following two files in the /proc file-system:

* `/proc/net/snmp`
* `/proc/net/netstat`

Because the available information is usually far too much to be useful, the interesting values can be selected using the configuration file.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

- collectd 4.7+

### INSTALLATION

This plugin is included with [SignalFx collectd](https://github.com/signalfx/Integrations/tree/master/collectd).

### CONFIGURATION

Configuration for this plugin is kept in the main [collectd.conf](https://github.com/signalfx/Integrations/blob/master/collectd/collectd.conf) file.

From [collectd wiki](https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_protocols):

| Configuration Option | Type | Definition |
|----------------------|------|------------|
|`Value`| _Selector_ | Selects whether or not to select a specific value. <ul><li>The string being matched is of the form `Protocol:ValueName` where `Protocol` will be used as the plugin instance and `ValueName` will be used as type instance. </li><li> An example of the string being used would be `Tcp:RetransSegs` </li><li> You can use regular expressions to match a large number of values with just one configuration option. </li><li> To select all "extended" TCP values, you could use the following statement: `Value "/^TcpExt:/"` </li><li> Whether only matched values are selected or all matched values are ignored depends on the **`IgnoreSelected`**. By default, only matched values are selected. If no value is configured at all, all values will be selected.</li></ui>|
|`IgnoreSelected`| _true/false_ | If set to true, inverts the selection made by `Value`, i. e. all matching values will be ignored.|


### USAGE

>This section contains information about how best to monitor the software in question, using the data from this plugin. In this section, the plugin author shares experience and expertise with the software to be monitored, for the benefit of users of the plugin. This section includes:
>
>- Important conditions to watch out for in the software
>- Common failure modes, and the values of metrics that will allow the user to spot them
>- Chart images demonstrating each important condition or failure mode

This plugin is an example that emits values on its own, and does not connect to software. It emits a repeating sine wave in the metric gauge.sine. The metric should look like this:

![Example chart showing gauge.sine](http://fixme)

The following conditions may be cause for concern:

*You see a straight line instead of a curve.*

This may indicate a period of missing data points. In the example chart shown above, some data points are missing between 16:40 and 16:41, and SignalFx is interpolating a straight line through the gap.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

License for this plugin can be found [in the header of the plugin](https://github.com/collectd/collectd/blob/master/src/protocols.c)
