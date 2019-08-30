---
title: VMem Metrics
brief: Metrics collected about virtual memory
---
# VMem Metrics

Use the [vmem](https://collectd.org/wiki/index.php/Plugin:vmem) collectd plugin to collect metrics about virtual memory usage.

The vmem plugin collects information about the virtual memory subsystem of the kernel. By default, it collects information such as page-faults, page-in and page-out to and from memory and swap, and the total number of pages. When verbose statistics are enabled, all page actions (allocations, refills, steals, …) are collected per zone (DMA, DMA32, …).

The data source for the Vmem plugin is /proc/vmstat. You may want to analyze this in order to understand what metrics you are interested in.

This plugin can collect very detailed data, as the statistics provided by the Linux kernel are very detailed. However, this must be enabled manually. In most cases, the default overview provides sufficient metrics, such as the number of pages read from swap space.

# Version information

| Software           | Version               |
|--------------------|-----------------------|
| collectd           |  4.4 or later         |


# Configuration
No configuration recommended.

This plugin provides only one configuration option, "Verbose", which defaults to false.

Setting "Verbose to true enables verbose collection of information. This includes page "actions", e. g. page allocations, (de)activations, steals and so on. Part of these statistics are collected on a "per zone" basis.

However, in our sample configuration we also filter out some less-used metrics. In order to see them you'll need to remove that filtering.

Filtering options can be found in `/etc/collectd.d/filtering_config/filtering-vmem.conf`. This file contains several rules related to filtering out metrics produced by the vmem plugin. The default behavior for all metrics is to drop  out from further processing. Some metrics have been whitelisted. To add more metrics than those that are already whitelisted, use vmem_filtering_accept_whitelisted_* rules as a reference. If you want to collect the entire set of available metrics, change the default filtering chain target to 'return'. The default target is the last target of the chain. 

Please note that even if you turn off filtering, you may still want to turn on verbose mode in collectd.conf file.

Brief filtering-vmem listing:

```
<Chain "VmemFilters">
  # more rules here
  <Rule "vmem_filtering_accept_whitelisted_vmpage_number_free_pages"> #rule to include free pages number metric
    <Match "regex">
      Type 'vmpage_number'
      TypeInstance 'free_pages'
    </Match>
  Target "return" #continue processing
  </Rule>
  # more rules here
  Target "stop" #default rule. Change it to return if you want to have all metrics to be collected
</Chain>

```


# Useful links:
* [Vmem plugin](https://collectd.org/wiki/index.php/Plugin:vmem)
* [Collectd filter chains explained](http://manpages.ubuntu.com/manpages/precise/en/man5/collectd.conf.5.html#contenttoc6)
