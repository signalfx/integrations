# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_collectd.png) Memory

Metadata associated with the Memory collectd plugin can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-memory">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/memory.c">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:Memory">collectd wiki</a>:

> The Memory plugin collects physical memory utilization.
The values are reported by their use by the operating system. Under Linux, the categories are:

> * Used
> * Buffered
> * Cached
> * Free

> Free memory is memory you paid for, that's using power and that doesn't do anything useful. It is normal that the operating system puts that memory to use, for example by caching files it has accessed (reported as Cached under Linux).

> Virtual memory statistics can be collected with the [vmem plugin](https://github.com/signalfx/integrations/tree/master/collectd-vmem)[](sfx_link:collectd-vmem) under Linux.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd |  1.0+ |

### INSTALLATION

**If you are using the new Smart Agent, see the docs for [the collectd/memory
monitor](https://github.com/signalfx/signalfx-agent/tree/master/docs/monitors/collectd-memory.md)
for more information.  The configuration documentation below may be helpful as
well, but consult the Smart Agent repo's docs for the exact schema.**


Installation and initial configuration options are available as part of the <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd">SignalFx collectd agent</a>.


### CONFIGURATION

No configuration is required for this plugin.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

License for this plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/memory.c">in the header of the plugin</a>
