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

Windows service for reporting Windows Performance Counters to SignalFx

This code is based on/inspired by [PerfTap](https://github.com/Iristyle/PerfTap) as a means of sending performance data to a monitoring system.

### REQUIREMENTS AND DEPENDENCIES

| Software          | Version        |
|-------------------|----------------|
| .NET Framework    |  4+ |
| Windows   | Windows Server 2003 SP2 or later |  
| Powershell (required to user the one-line installer) | v2+ |

* Admin rights for installing services (the service is setup to run as NETWORK SERVICE)

Sorry Mono, this is the Win32 only club -- besides, Linux distros already have better tools for this!

### INSTALLATION

Download the [latest release](https://github.com/signalfx/PerfCounterReporter/releases) and unzip it.

At a PowerShell admin prompt

```
     ./Install.ps1
```

Alternatively, specify any or all of the configuration options.

```
    ./Install.ps1 @{APIToken='yourtoken';SourceType='netbios';DefinitionPaths='CounterDefinitions\system.counters','CounterDefinitions\webservice.counters';CounterNames='\Processor(*)\% Processor Time';}
```

Or if readability is your thing:

```
    $config = @{
        APIToken='yourtoken';
        SourceType='netbios';
        SampleInterval = '00:00:01';
        DefinitionPaths = 'CounterDefinitions\system.counters','CounterDefinitions\webservice.counters';
        CounterNames = '\Processor(*)\% Processor Time';
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
* **DefinitionPaths** - List of file paths with counter definitions. Default Value: CounterDefinitions\system.counters
* **CounterNames** - List of strings. Any additional "one off" counters to collect. Default Value: (empty list)

### CONFIGURATION

The PerfCounterReporter.config file controls what counters are enabled, how often they're sampled  Paths may be absolute, relative to the current working directory of the application, or relative to the current directory of where the binaries are installed.
It also controls the configuration of how to send metrics to SignalFX (TODO fix this so it is not only SignalFx reporting)

```xml
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <configSections>
    <section name="signalFxReporter" type=" Metrics.SignalFX.Configuration.SignalFxReporterConfiguration, Metrics.NET.SignalFX"/>
    <section name="counterSampling" type="PerfCounterReporter.Configuration.CounterSamplingConfiguration, PerfCounterReporter" />
  </configSections>
  <signalFxReporter apiToken="<yourtoken>" sampleInterval="00:00:05" sourceType="netbios"/>
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
</configuration>
```

#### Counter Definitions in the box

| File       | Purpose      |
|------------|--------------|
| system.counters | standard Windows counters for CPU, memory and paging, disk IO and NIC |
| dotnet.counters | the most critical .NET performance counters - exceptions, logical and physical threads, heap bytes, time in GC, committed bytes, pinned objects, etc. System totals are returned, as well as stats for all managed processes, as counters are specified with wildcards. |
| aspnet.counters | information about requests, errors, sessions, worker processes |
| sqlserver.counters  | the kitchen sink for things that are important to SQL server (including some overlap with system.counters) - CPU time for SQL processes, data access performance counters, memory manager, user database size and performance, buffer manager and memory performance, workload (compiles, recompiles), users, locks and latches, and some mention in the comments of red herrings. This list of counters was heavily researched. |
| webservice.counters | wild card counters for current connections, isapi extension requests, total method requests and bytes |

#### Extra Counter Definitions

One-off counters may be added to the configuration file as shown in the example above.  Counter files may also be created to group things together.  Blank lines and lines prefixed with the # character are ignored.

The names of all counters are combined together from all the configured files and individually specified names.  However, these names have not yet been wildcard expanded.  So, if for instance, both the name `\processor(*)\% processor time` and `\processor(_total)\% processor time` have been specified, `\processor(_total)\% processor time` will be read twice.

#### Logging

NLog is used for logging, and the default configuration ships with just file logging enabled.  The logs are dumped to `%ALLUSERSPROFILE%\PerfCounterReporter\logs`.  Generally speaking, on modern Windows installations, this will be `C:\ProgramData\PerfCounterReporter\logs`.  Obviously this can be modified to do whatever you want per the NLog [documentation](http://nlog-project.org/wiki/Configuration_File).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
