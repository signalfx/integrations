---
title: StatsD.NET Integration
brief: The SignalFx Integration for Windows StatsD.NET.
---

# ![](https://github.com/signalfx/Integrations/blob/master/win-statsd.net/img/integrations_windows.png) SignalFx StatsD.NET Integration

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

## DESCRIPTION

Plugin for statsd.net (https://github.com/lukevenediger/statsd.net/) to send metrics to SignalFx

You can find the SignalFx version of statsd.net that is released here:
https://github.com/signalfx/statsd.net/

## REQUIREMENTS AND DEPENDENCIES

| Software          | Version        |
|-------------------|----------------|
| .NET Framework    |  4+ |
| Windows   | Windows Server 2003 SP2 or later |  
| Powershell (required to user the one-line installer) | v2+ |

* Admin rights for installing services (the service is setup to run as NETWORK SERVICE)

Sorry Mono, this is the Win32 only club -- besides, Linux distros already have better tools for this!

## INSTALLATION

Download the latest release from https://github.com/signalfx/signalfx-statsd.net-plugin/releases and unzip it.

At a PowerShell admin prompt

```     
./Install.ps1
```

Alternatively, specify any or all of the configuration options.

```
./Install.ps1 @{APIToken='yourtoken';SourceType='netbios';}
```

Or if readability is your thing:

 ```
    $config = @{
        APIToken='yourtoken';
        SourceType='netbios';
        SampleInterval = '5s';
    }
    ./Install.ps1 $config
 ```

For hash values not supplied the following defaults are used. APIToken and SourceType are required.  

* **APIToken** - Your SignalFx API token. No default.
* **SourceType** - Configuration for what the "source" of metrics will be. No default. Value must be one of:
	* **netbios** - use the netbios name of the server
	* **dns** - use the DNS name of the server
	* **fqdn** - use the FQDN name of the server
	* **custom** - use a custom value. If the is specified then a SourceValue parameter must be specified.
* **DefaultDimensions** - A hashtable of default dimensions to pass to SignalFx. Default: Empty dictionary.
* **AwsIntegration** - If set to "true" then AWS integration will be turned on for SignalFx reporting. Default: false
* **SampleInterval** - string of how often to send metrics to SignalFx. Looks supported values look like "5s", or "1m". Default Value: 5s

## CONFIGURATION

### Extensions to statsd protocol to support Dimensions
There are two ways you can add dimensions to your metrics:
  * tags
  * metric name

#### Tags
In additon to the standard statsd protocol. This version of the listener also supports tags being sent on metrics. Adding a `|#tag1=value1,tag2=value2,...` to the end of the normal statsd lines sent will make the tags available to the server. With the SignalFx reporter, these tags will be turned into Dimensions on the metric.

 E.g.

 ```
 api.count:1|c|#apiType=login,success=true
 ```

 will give you a metric `api.count` with two dimensions `apiType` and `success`.

#### Metric Name
This server also supports sending in dimensions in the metric names. In this case you put your `metric name` followed by `[name1=value1,name2=value2]` at the *end* of the metric name.

 E.g.

 ```
 api.count[apiType=Login,success=true]:1|c
 ```

 will give you a metric `api.count` with two dimensions `apiType` and `success`.

## LICENSE

This plugin is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/PerfCounterReporter/blob/master/LICENSE) for more details.
