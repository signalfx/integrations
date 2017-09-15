# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integration_collectd.png) vmem

This is a directory consolidate all the metadata associated with the vmem collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/vmem.c).

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:vmem):

> The vmem plugin collects information about the virtual memory subsystem of the kernel. Per default, information such as page-faults, page-in and page-out to and from memory and swap, and the total number of pages are collected. When verbose statistics are enabled, all page actions (allocations, refills, steals, …) are collected per zone (DMA, DMA32, …).

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
|  collectd   |  4.4+  |

### INSTALLATION

Installation and initial configuration options are available as part of the [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd).


### CONFIGURATION

Configuration for this plugin is kept in the main [collectd.conf](https://github.com/signalfx/integrations/blob/master/collectd/collectd.conf) file.

From the [collectd wiki](https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_vmem):

> The vmem plugin collects information about the usage of virtual memory. Since the statistics provided by the Linux kernel are very detailed, they are collected very detailed. However, to get all the details, you have to switch them on manually. Most people just want an overview over, such as the number of pages read from swap space.

| Configuration Option | Type | Definition |
|----------------------|------|------------|
|Verbose| true/false|Enables verbose collection of information. This will start collecting page "actions", e. g. page allocations, (de)activations, steals and so on. Part of these statistics are collected on a "per zone" basis.|

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

License for this plugin can be found [in the header of the plugin](https://github.com/signalfx/collectd/blob/master/src/vmem.c)
