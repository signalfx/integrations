# ![](https://github.com/signalfx/integrations/blob/master/win-metrics.net/img/integrations_windows.png) Metrics.NET

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

## DESCRIPTION

The Metrics.NET library provides a way of instrumenting applications with custom metrics (timers, histograms, counters etc) that can be reported in various ways and can provide insights on what is happening inside a running application.

This assembly provides a mechanism to report the metrics gathered by Metrics.NET to SignalFx.

## REQUIREMENTS AND DEPENDENCIES

| Software          | Version        |
|-------------------|----------------|
| .NET Framework    |  4+ |
| Windows   | Windows Server 2003 SP2 or later |  
| Powershell (required to user the one-line installer) | v2+ |

* Admin rights for installing services (the service is setup to run as NETWORK SERVICE)

Sorry Mono, this is the Win32 only club -- besides, Linux distros already have better tools for this!

## INSTALLATION

In order to send dimensions to SignalFx with Metrics.NET you use the MetricTags object and use `Metrics.Core.TaggedMetricsContext`. This unfortunately (currently) means that you will to have a second context (think `.` in metric name). MetricTags are currently a list of strings. To send a dimension just add a string that looks like `key=value` to the MetricTags object you use to initialize your metrics.

E.g

```
csharp

public MetricContext getContext() {
   MetricsContext context = Metric.Context("app", (ctxName) => { return new TaggedMetricsContext(ctxName); });
}

//Setup counters for API usage
public void setupCounters(string env) {
    this,loginAPICount = getContext().Counter("api.use", Unit.Calls, new MetricTags("environment="+env, "api_type=login"));
    this.purchaseAPICount = getContext().Counter("api.use", Unit.Calls, new MetricTags("environment="+env, "api_type=purchase"));
}
```

This will create a context called `app` so metrics reported will look like `yourhostname.app.api.use`.
This will allow you to see all of of your `api.use` metrics together or split it out by `environment` or by `api_type`.

## CONFIGURATION

To configure Metrics.Net to report you need to set up two things
 - Your SignalFx API token
 - The default source

### Your SignalFx API Token

Your API SignalFx API token is available if you click on your avatar in the SignalFx UI.

### Default source name

When reporting to SignalFx we need to associate the reported metrics to a "source". Some choices are:
 - NetBIOS Name
 - DNS Name
 - FQDN
 - Custom Source

### AWS Integration

If your code will be running on an AWS instance and you have integrated SignalFx with AWS. You can configure the Metrics.Net.SignalFX reporter to send the instance id as one of the dimensions so that you can use the discovered AWS instance attributes to filter and group metrics.

### Default Dimensions
If there are dimensions that you wish to send on all the metrics that you report to SignalFx. You can configure a set of _**default dimensions**_ when you configure the SignalFXReporter

### C# Configuration

#### Basic Configuration

```csharp
// Configure with NetBios Name as the default source
 Metric.Config.WithReporting(report =>
      report.WithSignalFx("<your API token>", TimeSpan.FromSeconds(5)).WithNetBiosNameSource().Build());
```

```csharp
// Configure with DNS Name as the default source
Metric.Config.WithReporting(report =>
     report.WithSignalFx("<your API token>", TimeSpan.FromSeconds(5)).WithDNSNameSource().Build());
```

```csharp
// Configure with FQDN as the default source
Metric.Config.WithReporting(report =>
     report.WithSignalFx("<your API token>", TimeSpan.FromSeconds(5)).WithFQDNSource().Build());
```

```csharp
// Configure with custom source name
Metric.Config.WithReporting(report =>
     report.WithSignalFx("<your API token>", TimeSpan.FromSeconds(5)).WithSource("<source name>").Build());
```

#### AWS Integration

```csharp
// Add AWS Integration
Metric.Config.WithReporting(report =>
     report.WithSignalFx("<your API token>", TimeSpan.FromSeconds(10)).WithAWSInstanceIdDimension().WithNetBiosNameSource().Build());
```

#### Default Dimensions

```csharp
// Add default Dimensions
IDictionary<string, string> defaultDims = new Dictionary<string, string>();
defaultDims["environment"] = "prod";
defaultDims["serverType"] = "API";
Metric.Config.WithReporting(report =>
     report.WithSignalFx("<your API token>", TimeSpan.FromSeconds(10)).WithDefaultDimensions(defaultDims).WithAWSInstanceIdDimension().WithNetBiosNameSource().Build());
```

#### Aggregations
The Metrics.NET library calculates aggregations for almost all of the metric types:

 - Counter(with items) -> percentage

 - Histogram -> count, last, min, mean, max, stddev, median, percent\_75, percent\_95, percent\_98, percent\_99, percent\_999

 - Meter(no items) -> rate\_mean, rate\_1min, rate\_5min, rate\_15min
 - Meter(with items) -> per Item: percent, rate\_mean, rate\_1min, rate\_5min, rate\_15min


 - Timer -> count, active\_sessions, rate\_mean, rate\_1min, rate\_5min, rate\_15min, last, min, mean, max, stddev, median, percent\_75, percent\_95, percent\_98, percent\_99, percent\_999

The client can specify which of these aggregations they wish to send. By default count,min,mean,max aggregations are sent.

```csharp
// Send the 99 percentile metrics
Metric.Config.WithReporting(report =>
     report.WithSignalFx("<your API token>", TimeSpan.FromSeconds(10)).WithMetricDetail(MetricDetails.percent_99).Build());
```

### App.Config Configuration
It is also possible to use App.Config to configure the SignalFxReporter.

To configure via App.Config use the following code to initialize your Metrics:

```csharp
Metric.Config.WithReporting(report => report.WithSignalFxFromAppConfig());
```

#### Basic Configuration
You need to first setup a section in the <configSections> portion at the
top of your App.Config file.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <configSections>
    <section name="signalFxReporter" type=" Metrics.SignalFx.Configuration.SignalFxReporterConfiguration, Metrics.NET.SignalFx"/>
  </configSsections>
  ....
</configuration>
```

Next you need to add a <signalFxReporter> stanza
You must specify the following attributes:

|Attribute | definition |
|----------|------------|
|apiToken | Your SignalFx token (YOUR_SIGNALFX_API_TOKEN) |

The following attributes are optional

|Attribute | definition |
|----------|------------|
|sourceDimension | What the name of the "source" dimension is.|
| sourceType | How you would like to configure the default source. Your choices are:<ui><li>netbios</li><li>dns</li><li>fqdn</li><li>custom - If you specify this you must also specify the "sourceValue" attribute to specify the custom source.</li></ui>|
| sampleInterval | TimeSpan (defaults to 00:00:05, mininum 00:00:01) How often to report metrics to SignalFx |
| maxDatapointPerMessage | Integer (defaults to 10000, min 1, max 10000) The maximumum of points to report per message to SignalFx|
| awsIntegration | Boolean (default to false) If set to true then the AWS integration will be turned on.|

E.g

```xml
  <signalFxReporter apiToken="YOUR_SIGNALFX_API_TOKEN" sourceType="netbios" sampleInterval="00:00:05"/>
```

### Source Value for a Metric

It is often useful, but not required, to identify the "source" of a metric. An example of this is a hostname. There are two things that needs to be configured:

|Attribute | definition |
|----------|------------|
| sourceDimension | The name of the "source" metric.|
| defaultSource | The value to send when the source metric value is not specified.|

### Default Dimensions

To add default dimensions add a nested <defaultDimensions> in your <signalFxReporter> stanza:

```xml
  <signalFxReporter apiToken="YOUR_SIGNALFX_API_TOKEN" sourceType="netbios" sampleInterval="00:00:05"/>
    <defaultDimensions>
      <defaultDimension name="environment" value="prod"/>
      <defaultDimension name="serverType" value="API"/>
    </defaultDimensions>
  </signalFxReporter>
```

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
