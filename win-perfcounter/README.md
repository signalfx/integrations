# ![](https://github.com/signalfx/integrations/blob/master/win-perfcounter/img/integrations_windows.png) PerfCounterReporter

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

### DESCRIPTION

PerfCounterReporter is a Windows service for reporting Windows Performance Counters to SignalFx. Use this to monitor infrastructure of Windows hosts, including CPU, disk, memory and network. 

This code is based on/inspired by [PerfTap](https://github.com/Iristyle/PerfTap) as a means of sending performance data to a monitoring system.

### REQUIREMENTS AND DEPENDENCIES

| Software          | Version        |
|-------------------|----------------|
| .NET Framework    |  4.5+ |
| Windows   | Windows 7+ (Desktop) or Windows Server 2008+ (Server) |  

You must have admin privileges in order to install PerfCounterReporter. It will run as LOCAL SERVICE.

### INSTALLATION

1. Download the latest release of the .MSI installer from the [PerfCounterReporter releases page](https://github.com/signalfx/PerfCounterReporter/releases).

1. Launch the .MSI and follow the prompts to configure the installation.

1. After the installation process is complete, PerfCounterReporter will immediately begin sending metrics to SignalFx. Verify that metrics have arrived by looking for metrics from this host in the SignalFx catalog. If metrics do not arrive, examine the PerfCounterReporter log file for errors (details in [Usage](#usage)).

### CONFIGURATION

The file `PerfCounterReporter.exe.config` controls the configuration of PerfCounterReporter. If you installed this tool using the .MSI installer, it is not necessary to directly modify this file. 

#### Selecting counter sets

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

For information on logging see [NLog documentation](http://nlog-project.org/wiki/Configuration_File).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
