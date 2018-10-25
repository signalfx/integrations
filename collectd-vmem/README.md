# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_collectd.png) vmem

Metadata associated with the vmem collectd plugin can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-vmem">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/vmem.c">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:vmem">collectd wiki</a>:

> The vmem plugin collects information about the virtual memory subsystem of the kernel. Per default, information such as page-faults, page-in and page-out to and from memory and swap, and the total number of pages are collected. When verbose statistics are enabled, all page actions (allocations, refills, steals, …) are collected per zone (DMA, DMA32, …).

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
|  collectd   |  4.4+  |

### INSTALLATION

**If you are using the new Smart Agent, see the docs for [the collectd/vmem
monitor](https://github.com/signalfx/signalfx-agent/tree/master/docs/monitors/collectd-vmem.md)
for more information.  The configuration documentation below may be helpful as
well, but consult the Smart Agent repo's docs for the exact schema.**


Installation and initial configuration options are available as part of the <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd">SignalFx collectd agent</a>.


### CONFIGURATION

Configuration for this plugin is kept in the main <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/collectd/collectd.conf">collectd.conf</a> file.

From the <a target="_blank" href="https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_vmem">collectd wiki</a>:

> The vmem plugin collects information about the usage of virtual memory. Since the statistics provided by the Linux kernel are very detailed, they are collected very detailed. However, to get all the details, you have to switch them on manually. Most people just want an overview over, such as the number of pages read from swap space.

| Configuration Option | Type | Definition |
|----------------------|------|------------|
|Verbose| true/false|Enables verbose collection of information. This will start collecting page "actions", e. g. page allocations, (de)activations, steals and so on. Part of these statistics are collected on a "per zone" basis.|

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

License for this plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/vmem.c">in the header of the plugin</a>
