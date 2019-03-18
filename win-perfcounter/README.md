# ![](https://github.com/signalfx/integrations/blob/master/win-perfcounter/img/integrations_windows.png) PerfCounterReporter (deprecated)

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

### DESCRIPTION

PerfCounterReporter is a deprecated Windows service for reporting Windows
Performance Counters to SignalFx. It was used to monitor infrastructure of
Windows hosts, including CPU, disk, memory and network. Please use the
[SignalFx Smart Agent](https://github.com/signalfx/integrations/tree/release/signalfx-agent)
and its [Windows Perf Counter](https://github.com/signalfx/signalfx-agent/blob/master/docs/monitors/telegraf-win_perf_counters.md) monitor instead.

This code is based on/inspired by <a target="_blank" href="https://github.com/Iristyle/PerfTap">PerfTap</a> as a means of sending performance data to a monitoring system.

### REQUIREMENTS AND DEPENDENCIES

| Software          | Version        |
|-------------------|----------------|
| .NET Framework    |  4.5+ |
| Windows   | Windows 7+ (Desktop) or Windows Server 2008+ (Server) |  

You must have admin privileges in order to install PerfCounterReporter. It will run as LOCAL SERVICE.

### INSTALLATION

1. Download the latest release of the .MSI installer from the <a target="_blank" href="https://github.com/signalfx/PerfCounterReporter/releases">PerfCounterReporter releases page</a>.

2. Launch the .MSI and follow the prompts to configure the installation.

3. After the installation process is complete, PerfCounterReporter will immediately begin sending metrics to SignalFx. Verify that metrics have arrived by looking for metrics from this host in the SignalFx catalog. If metrics do not arrive, examine the PerfCounterReporter log file for errors (details in [Usage](#usage)).

### CONFIGURATION

The file `PerfCounterReporter.exe.config` controls the configuration of PerfCounterReporter. If you installed this tool using the .MSI installer, it is not necessary to directly modify this file.

`PerfCounterReporter.exe.config` controls what performance counters are enabled and how often they are sampled. Paths to these counters may be absolute, relative to the current working directory of the application, or relative to the current directory of where the binaries are installed. This file also controls the configuration of how to report metrics to SignalFx.

The `signalFxReporter` block includes the following options:

| Setting            | Description     | Default  |
|--------------------|----------------------------|----------|
| APIToken | Your SignalFx API token. (YOUR_SIGNALFX_API_TOKEN) | No default. |
| SourceType | Configuration for what the "source" of metrics will be. Value must be one of `netbios` (use the netbios name of the server), `dns` (use the DNS name of the server), `fqdn` (use the FQDN name of the server), or `custom` (use a custom value specified in a parameter `SourceValue`). | No default. |
| DefaultDimensions | A hashtable of default dimensions to pass to SignalFx (see [Adding Default Dimensions](#adding-default-dimensions) below). | Empty dictionary |
| AwsIntegration | If set to "true" then AWS metadata will accompany metrics. | false |
| SampleInterval | Controls the interval at which to send metrics to SignalFx, as hh:mm:ss. | 00:00:05 |

**Example:**

```xml
<signalFxReporter apiToken="YOUR_SIGNALFX_API_TOKEN" sampleInterval="00:00:05" sourceType="netbios"/>
```

#### Adding default dimensions
To add dimensions that will be included in every metric emitted by PerfCounterReporter, add a nested `<defaultDimensions>` block in your `<signalFxReporter>` stanza. In the following example, dimensions "environment:prod" and "serverType:API" will be included in all metrics:

```xml
  <signalFxReporter apiToken="YOUR_SIGNALFX_API_TOKEN" sourceType="netbios" sampleInterval="00:00:05">
    <defaultDimensions>
      <defaultDimension name="environment" value="prod"/>
      <defaultDimension name="serverType" value="API"/>
    </defaultDimensions>
  </signalFxReporter>
```

#### Selecting counter sets

The `counterSampling` block includes the following options:

| Setting            | Description     | Default  |
|--------------------|----------------------------|----------|
| definitionFilePaths | List of file paths with counter definitions (see [Selecting counter sets](#selecting-counter-sets) below) |  CounterDefinitions\system.counters |
| counterNames | Names of individual counters to collect (see [Extra counter definitions](#extra-counter-definitions) below) | No default. |

**Example:**

```
<counterSampling>
  <definitionFilePaths>
    <definitionFile path="CounterDefinitions\\system.counters" />
    <!-- <definitionFile path="CounterDefinitions\\aspnet.counters" /> -->
    <!-- <definitionFile path="CounterDefinitions\\dotnet.counters" /> -->
    <!-- <definitionFile path="CounterDefinitions\\sqlserver.counters" /> -->
    <!-- <definitionFile path="CounterDefinitions\\webservice.counters" /> -->
  </definitionFilePaths>
  <!--
  <counterNames>
    <counter name="\network interface(*)\bytes total/sec" />
  </counterNames>
  -->
</counterSampling>
```

Counter files (`*.counter`) define the metrics that PerfCounterReporter will collect. The following counter sets accompany this tool. Enable them by adding entries to `definitionFilePaths` in `PerfCounterReporter.exe.config`:

| File       | Purpose      |
|------------|--------------|
| system.counters | (Enabled by default) Standard Windows counters for CPU, memory and paging, disk IO and NIC. |
| dotnet.counters | The most critical .NET performance counters: exceptions, logical and physical threads, heap bytes, time in GC, committed bytes, pinned objects, etc. System totals are returned, as well as stats for all managed processes, as counters are specified with wildcards. |
| aspnet.counters | Information about requests, errors, sessions, worker processes. |
| sqlserver.counters  | The kitchen sink for things that are important to SQL server (including some overlap with system.counters): CPU time for SQL processes, data access performance counters, memory manager, user database size and performance, buffer manager and memory performance, workload (compiles, recompiles), users, locks and latches, and some mention in the comments of red herrings. |
| webservice.counters | Wild card counters for current connections, isapi extension requests, total method requests and bytes. |

Outside of .counter files, counters to collect may also be added directly to `PerfCounterReporter.exe.config` as shown below:

```
<counterNames>
  <counter name="\network interface(*)\bytes total/sec" />
</counterNames>
```

##### Note: Using wildcards in counter names

The names of all counters to be reported are combined together from all the configured files and individually specified names.  However, these names have not yet been wildcard-expanded.  For instance, if both `\processor(*)\% processor time` and `\processor(_total)\% processor time` have been specified to be collected, `\processor(_total)\% processor time` will be read twice.

### USAGE

#### Logging

NLog is used for logging, and the default configuration of this tool ships with just file logging enabled.  The logs are written to `%ALLUSERSPROFILE%\PerfCounterReporter\logs`.  Generally speaking, on modern Windows installations, this will be `C:\ProgramData\PerfCounterReporter\logs`.  

For information on logging see <a target="_blank" href="http://nlog-project.org/wiki/Configuration_File">NLog documentation</a>.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
