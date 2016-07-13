---
title: PerfCounter Reporter Integration
brief: The SignalFx Integration for Windows Performance Counter Reporter.
---

# ![](https://github.com/signalfx/integrations/blob/master/win-perfcounter/img/integrations_windows.png) Metrics.NET Integration

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

### DESCRIPTION

PerfCounterReporter is a Windows service for reporting Windows Performance Counters to SignalFx.

This code is based on/inspired by [PerfTap](https://github.com/Iristyle/PerfTap) as a means of sending performance data to a monitoring system.

### REQUIREMENTS AND DEPENDENCIES

| Software          | Version        |
|-------------------|----------------|
| .NET Framework    |  4+ |
| Windows   | Windows Server 2003 SP2 or later |  
| Powershell (required to user the one-line installer) | v2+ |

You must have admin privileges in order to install PerfCounterReporter. It will run as NETWORK SERVICE.

### INSTALLATION

1. Download the latest release of the .MSI installer from the [PerfCounterReporter releases page](https://github.com/signalfx/PerfCounterReporter/releases).

1. Launch the .MSI and follow the prompts to configure the installation. 

1. After the installation process is complete, PerfCounterReporter will immediately begin sending metrics to SignalFx. Verify that metrics have arrived by looking for metrics from this host in the SignalFx catalog. If metrics do not arrive, examine the PerfCounterReporter log file for errors (details in [Usage](#usage)).

### CONFIGURATION

The file `PerfCounterReporter.exe.config` controls the configuration of PerfCounterReporter. 

The `signalFxReporter` block includes the following options: 

| Setting            | Description     | Default  |
|--------------------|----------------------------|----------|
| APIToken | Your SignalFx API token. | No default. |
| SourceType | Configuration for what the "source" of metrics will be. Value must be one of `netbios` (use the netbios name of the server), `dns` (use the DNS name of the server), `fqdn` (use the FQDN name of the server), or `custom` (use a custom value specified in a parameter `SourceValue`.) | No default. |
| DefaultDimensions | A hashtable of default dimensions to pass to SignalFx | Empty dictionary |
| AwsIntegration | If set to "true" then AWS metadata will accompany metrics. | false |
| SampleInterval | Controls how often to send metrics to SignalFx. | 00:00:05 |

**Example:** 

```
<signalFxReporter apiToken="<yourtoken>" sampleInterval="00:00:05" sourceType="netbios"/>
```

The `counterSampling` block includes the following options:

| Setting            | Description     | Default  |
|--------------------|----------------------------|----------|
| definitionFilePaths | List of file paths with counter definitions (see [Selecting counter sets](#selecting-counter-sets) below) |  CounterDefinitions\system.counters |
| counterNames | Names of indiviual counters to collect (see [Extra counter definitions](#extra-counter-definitions) below) | No default. |

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

#### Selecting counter sets

Counter files (`*.counter`) define thematically related groups of metrics. Blank lines and lines prefixed with the # character are ignored in .counter files. The following counter sets accompany this tool. Enable them by adding entries to `definitionFilePaths` in `PerfCounterReporter.exe.config`: 

| File       | Purpose      |
|------------|--------------|
| system.counters | standard Windows counters for CPU, memory and paging, disk IO and NIC (enabled by default) |
| dotnet.counters | the most critical .NET performance counters: exceptions, logical and physical threads, heap bytes, time in GC, committed bytes, pinned objects, etc. System totals are returned, as well as stats for all managed processes, as counters are specified with wildcards. |
| aspnet.counters | information about requests, errors, sessions, worker processes |
| sqlserver.counters  | the kitchen sink for things that are important to SQL server (including some overlap with system.counters): CPU time for SQL processes, data access performance counters, memory manager, user database size and performance, buffer manager and memory performance, workload (compiles, recompiles), users, locks and latches, and some mention in the comments of red herrings. This list of counters was heavily researched. |
| webservice.counters | wild card counters for current connections, isapi extension requests, total method requests and bytes |

#### Extra Counter Definitions

One-off counters may be added to `PerfCounterReporter.exe.config` as shown below:

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

For information on logging see [NLog documentation](http://nlog-project.org/wiki/Configuration_File).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
