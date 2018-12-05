# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_collectd.png) cURL-JSON Plugin

Metadata associated with the cURL-JSON collectd plugin can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-curl-json">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/curl_json.c">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

### DESCRIPTION

From <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:cURL-JSON">collectd wiki</a>:

The cURL-JSON plugin queries JavaScript Object Notation (JSON) data using the cURL library and parses it according to the user's configuration using Yet Another JSON Library (YAJL). This can be used to query statistics information from a CouchDB instance, for example.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software  | Version        |
|-----------|----------------|
| collectd  | 4.8+ |

### INSTALLATION

Installation and initial configuration options are available as part of the <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd">SignalFx collectd agent</a>.


### CONFIGURATION

From <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:cURL-JSON">collectd wiki</a>:

This plugin is a generic plugin, i.e. it cannot work without configuration, because there is no reasonable default behavior. Please read the [Plugin curl\_json section](https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_curl_json) of the collectd.conf manual page for an in-depth description of the plugin's configuration.

### USAGE

There are many potential uses for the cURL-JSON plugin. One example is for gathering metrics from [Riak KV from Basho](http://basho.com/products/riak-kv/). You can find more details on this use case and a Riak KV configuration [here](https://github.com/signalfx/integrations/tree/master/collectd-riak)[](sfx_link:collectd-riak).

### LICENSE

License for this plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/curl_json.c">in the header of the plugin</a>.
