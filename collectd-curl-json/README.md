---
title: collectd cURL-JSON Plugin
brief: Use cURL on JSON formatted metrics for collectd.
---

# cURL-JSON Plugin  ![](https://github.com/signalfx/Integrations/blob/master/collectd/img/integrations_collectd.png)

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:cURL-JSON):

The cURL-JSON plugin queries JavaScript Object Notation (JSON) data using the cURL library and parses it according to the user's configuration using Yet Another JSON Library (YAJL). This can be used to query statistics information from a CouchDB instance, for example.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

- collectd 4.8+

### INSTALLATION

This plugin is included with [SignalFx's collectd package](https://support.signalfx.com/hc/en-us/articles/208080123).

### CONFIGURATION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:cURL-JSON):

This plugin is a generic plugin, i.e. it cannot work without configuration, because there is no reasonable default behavior. Please read the [Plugin curl_json section](https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_curl_json) of the collectd.conf manual page for an in-depth description of the plugin's configuration.

### USAGE

There are many potential uses for the cURL-JSON plugin. One example is for gathering metrics from [Riak KV from Basho](http://basho.com/products/riak-kv/). You can find more details on this use case and a Riak KV configuration [here](https://github.com/signalfx/Integrations/tree/master/collectd-riak).

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

License for this plugin can be found [in the header of the plugin](https://github.com/collectd/collectd/blob/master/src/curl_json.c).
