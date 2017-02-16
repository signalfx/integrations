# ![](https://github.com/signalfx/integrations/blob/master/telegraf/img/integration_signalfx.png) SignalFx Telegraf Agent

_This is a directory that consolidates all the metadata associated with the SignalFx Telegraf Agent. The code repository for this project can be found [here](https://github.com/signalfx/telegraf/)._

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

### DESCRIPTION

[Telegraf](https://github.com/influxdata/telegraf) is an open source daemon that collects statistics from a system and publishes them to a destination of your choice. You can use Telegraf to monitor infrastructure metrics, and enable Telegraf plugins that monitor a wide range of software. 

#### FEATURES

Sending data using Telegraf allows you to take advantage of the following features:

- The [SignalFx Infrastructure page](http://docs.signalfx.com/en/latest/built-in-content/host-nav.html) visualizes hosts that are monitored using the SignalFx Telegraf Agent.

  [<img src='./img/telegrafhostspage.png' width=200px>](./img/telegrafhostspage.png)

  [<img src='./img/hostspagesinglehost.png' width=200px>](./img/hostspagesinglehost.png)

- SignalFx provides [recommended detectors](http://docs.signalfx.com/en/latest/built-in-content/recommended-detectors.html) for hosts instrumented with the SignalFx Telegraf Agent. These built-in templates allow you to instantly create intelligent detectors based on SignalFx’s powerful analytics.

- The SignalFx metadata plugin for Telegraf is a plugin that enriches your data by sending metadata about your hosts to SignalFx. This plugin is included by default in SignalFx’s Telegraf Agent.

### REQUIREMENTS AND DEPENDENCIES

The SignalFx Telegraf Agent is supported on the following operating systems:

| Operating System  | Version        |
|-----------|----------------|
| Amazon Linux | 2014.09, 2015.03, 2015.09, & 2016.03 |
| Debian  | 7 & 8 |
| RHEL/Centos | 6.x & 7.x |
| Ubuntu  | 12.04, 14.04, 15.04 & 16.04 |

### INSTALLATION

#### Install on a host

1.  Download the latest release of the [SignalFx Telegraf Agent](https://github.com/signalfx/telegraf/releases) for your platform.
1.  Unzip the downloaded zip file.
```bash
unzip Linux-x86_64.zip
```
1. Copy the binary `telegraf` to the location of your choosing.
1. This agent must be configured before it is run. To generate a configuration file for the agent, execute the `telegraf` binary with the option `config` and redirect it to a file named `telegraf.conf`:
```bash
./telegraf config > telegraf.conf
```
1. Modify the resulting configuration file to provide values that make sense for your environment, as described [below](#configuration). 
1. Start the SignalFx Telegraf Agent, specifying the configuration file you generated in step 4.
```
./telegraf --config <path to the telegraf config file>
```
Note: This command only starts an executable. To ensure that the SignalFx Telegraf Agent starts as a background process at boot time, take additional steps as appropriate for your platform.

### CONFIGURATION

Edit the configuration file `telegraf.conf` as shown below to configure the agent for use with SignalFx. 

#### Enable required plugins

By default, the following plugin sections are listed in the configuration file but commented out. Uncomment the following configuration sections to enable necessary plugins:
*  `[[inputs.net]]`
*  `[[inputs.signalfx-metadata]]`
*  `[[outputs.signalfx]]`
*  `[[aggregators.signalfx_util]]`

If you are not using InfluxDB, comment out the InfluxDB plugin configuration section `[[outputs.influxdb]]`.

#### Set configuration values 

In `telegraf.conf`, provide values for the configuration options listed below that make sense for your environment.

| plugin block | configuration option | definition | example |
| ------ | ------------------ | ------- | -------- |
| [[outputs.signalfx]] | APIToken | Your SignalFx API token. | 'YOUR_SIGNALFX_API_TOKEN' |
| [[outputs.signalfx]] | DatapointIngestURL | The datapoint ingest endpoint you wish to send to. | `https://ingest.signalfx.com/v2/datapoint` |
| [[outputs.signalfx]] | EventIngestURL | The event ingest endpoint you wish to send to. | `https://ingest.signalfx.com/v2/event` |
| [[outputs.signalfx]] | Exclude | An array of metric names represented as strings that should not be sent to SignalFx | `["system.uptime_format", "cpu.idle"]` |
| [agent] | logfile | Name of the desired logfile. Leave empty to log to `stderr`.  | 'logfile.log' |


### USAGE

To use the data transmitted by the SignalFx Telegraf Agent, check out the Infrastructure tab in SignalFx. On this page you'll find a visualization of all transmitting hosts, built-in dashboards to show the health of your infrastructure, and recommended detectors to send intelligent alerts.

#### Adding dimensions to all datapoints

You can add a dimension to every datapoint that Telegraf sends to SignalFx by including key='value' pairs in the `[global_tags]` block of the Telegraf configuration file. The following example adds dimensions `serverType=API` and `tier=middleware` to every datapoint:
```bash
[global_tags]
  serverType='API'
  tier='middleware'
```

### METRICS

For full documentation of the metrics and dimensions emitted by Telegraf, see the `docs` directory in this repository.

### LICENSE

This integration is released under the MIT license. See [LICENSE](./LICENSE) for more details.
