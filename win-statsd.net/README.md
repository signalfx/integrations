# ![](https://github.com/signalfx/integrations/blob/master/win-statsd.net/img/integrations_windows.png) StatsD.NET

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

### DESCRIPTION

statsd.net is a high-performance stats collection service based on etsy's statsd service and written in c#.net. SignalFx's release of statsd.net (included with this plugin package) adds support for dimensions, and includes a plugin to send metrics to SignalFx.

### REQUIREMENTS AND DEPENDENCIES

| Software          | Version        |
|-------------------|----------------|
| .NET Framework    |  4+ |
| Windows   | Windows Server 2003 SP2 or later |  
| Powershell (required to use the one-line installer) | v2+ |

You must have admin privileges in order to install statsd.net. It will run as NETWORK SERVICE.

### INSTALLATION

1. Download the latest release from <a target="_blank" href="https://github.com/signalfx/signalfx-statsd.net-plugin/releases">https://github.com/signalfx/signalfx-statsd.net-plugin/releases</a> and unzip it.

2. At a PowerShell admin prompt, run the following command to install statsd.net including the SignalFx statsd.net plugin:

        ./Install.ps1 @{APIToken='YOUR_SIGNALFX_API_TOKEN';SourceType='netbios';}

See below for additional configuration options.

### CONFIGURATION

For values not supplied the following defaults are used. You must supply values for `APIToken` and `SourceType`.

These values are stored in the configuration file `statsdnet.config` within the `<signalfx>` stanza.

| Setting            | Description     | Default  |
|--------------------|----------------------------|----------|
| APIToken | Your SignalFx API token. (YOUR_SIGNALFX_API_TOKEN) | No default. |
| SourceType | Configuration for what the "source" of metrics will be. Value must be one of `netbios` (use the netbios name of the server), `dns` (use the DNS name of the server), `fqdn` (use the FQDN name of the server), or `custom` (use a custom value specified in a parameter `SourceValue`). | No default. |
| DefaultDimensions | A hashtable of default dimensions to pass to SignalFx (see [Adding Default Dimensions](#adding-default-dimensions) below). | Empty dictionary. |
| AwsIntegration | If set to "true" then AWS integration will be turned on for SignalFx reporting. | false |
| SampleInterval | string of how often to send metrics to SignalFx. Supported values look like "5s" (every 5 seconds), or "1m" (every 1 minute). | 5s |

### USAGE

#### Adding Default Dimensions
To add dimensions that will be included in every metric emitted by statsd.net, add a nested `<defaultDimensions>` block to the `<signalfx>` stanza in `statsdnet.config` as follows. In the following example, dimensions "environment:prod" and "serverType:API" will be included in all metrics:

```xml
  <backends>
    <signalfx apiToken="YOUR_SIGNALFX_API_TOKEN" sourceType="netbios" sampleInterval="00:00:05">
      <defaultDimensions>
        <defaultDimension name="environment" value="prod"/>
        <defaultDimension name="serverType" value="API"/>
      </defaultDimensions>
    </signalfx>
  </backends>
```

#### Adding dimensions using tags
SignalFx's release of statsd.net supports tags being sent on metrics. To use tags, add a `|#tag1=value1,tag2=value2,...` to the end of the normal statsd lines sent. The SignalFx statsd.net listener will transform these tags into dimensions on the metric.

For example, the following statsd line produces a metric `api.count` with two dimensions: `apiType` and `success`.

 ```
 api.count:1|c|#apiType=login,success=true
 ```

#### Adding dimensions as a list appended to metric name

This plugin supports sending in dimensions in the metric name. In this case you put your `metric name` followed by `[name1=value1,name2=value2]` at the *end* of the metric name.

For example, the following metric name produces a metric `api.count` with two dimensions: `apiType` and `success`.

 ```
 api.count[apiType=Login,success=true]:1|c
 ```

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
