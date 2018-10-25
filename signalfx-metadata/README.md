# SignalFx plugin for collectd

Metadata associated with the SignalFx plugin for collectd can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/signalfx-metadata">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd-signalfx/">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This SignalFx plugin for collectd configures collectd to aggregate metrics and send them to SignalFx. This plugin also handles the association to a specific SignalFx org to the data that is being sent through the org's API token.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd  |  4.9+  |
| Python plugin for collectd | (included with [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:collectd)) |
| Python    |  2.6+ |

### INSTALLATION

1. Download the Python module from the following URL:

        https://github.com/signalfx/signalfx-collectd-plugin

2. Download SignalFx’s <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/signalfx-metadata/10-signalfx.conf">sample configuration file</a>.

3. Modify the configuration file as follows:

    1. Modify the fields “TypesDB and “ModulePath” to point to the location on disk where you downloaded the Python module in step 2.

    2. Provide values that make sense for your environment, as described [below](#configuration).

4. Add the following line to /etc/collectd.conf, replacing the example path with the location of the configuration file you downloaded in step 4:

        include '/path/to/10-signalfx.conf'

5. Restart collectd.

collectd will begin emitting metrics to SignalFx.

### CONFIGURATION

You will need to add your API Token to allow the metric data to be sent to the SignalFx service.

Directions for finding your token:
1. Open your SignalFx profile page at https://app.signalfx.com/#/myprofile.
2. Locate the words "API Token" on the page.
3. Click the link next to "API Token" that says "show". Your API token appears.
4. Copy the value of the token to the "Token" field in this config.

| configuration option | definition | default value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | "/opt/signalfx-collectd-plugin" |
| URL | URL for where metrics are sent from collectd. If you are looking to limit the number of connections from your infrastructure to the SignalFx service you can optioally configure the use of the <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/metricproxy">SignalFx metricproxy</a> | "https://ingest.signalfx.com/v1/collectd" |
| Token | API token for your SignalFx org | none |
| LogTraces | Enable log traces | true |
| Notifications | Enable notification on this plugin | true |
| NotifyLevel | Set the notification level | "OKAY" |
| PerCoreCPUUtil | Enable cpu utilization per core metrics.  This requires the [filtering.conf](../collectd-match\_regex/filtering.conf) file| false |


### USAGE

This plugin provides additional aggregated system metrics to SignalFx.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
