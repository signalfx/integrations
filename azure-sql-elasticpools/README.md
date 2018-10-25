# ![](./img/integrations_azuresqlelasticpools.png) Microsoft Azure SQL Elastic Pools

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Azure SQL Elastic Pools via [Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

#### FEATURES

- **Azure SQL Server Elastic Pool**: Shows metrics of an Elastic Pool.

- **Azure SQL Server Elastic Pools**: Shows metrics of all Elastic Pools being monitored.

### INSTALLATION

To access this integration, [connect to Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

### USAGE

#### Interpreting Built-in dashboards

**Azure SQL Server Elastic Pool**

- **eDTU Used per Database in Elastic Pool vs eDTU Limit** - Shows a comparison of the eDTU limit to the eDTU used aggregated by database.

- **DTU Percentage Trend** - Trend of the DTU used percentage aggregated by database.

- **Server CPU Percentage** - Shows the load on the CPU aggregated by database.

- **Data I/O Percentage** - Shows the used percentage of Data I/O aggregated by database.

- **Log I/O Percentage** - Used percentage of Log I/O aggregated by database.

- **Elastic Pool Storage Used Percentage** - Trend of total elastic pool storage used.

- **Elastic Pool Storage Used per Database** - Trend of total elastic pool storage used aggregated by database.

**Azure SQL Server Elastic Pools**

- **Top Elastic Pools by DTU Consumption percent** - Lists the elastic pools with top DTU consumption percent.

- **Top Elastic Pools by eDTU Used** - Shows the eDTU used stacked by elastic pool.

- **Top Elastic Pools by Total Storage** - Shows a stacked chart of the total storage aggregated by elastic pool.

- **Top Elastic Pools by Workers Percentage** - Shows the trend of workers percent for top elastic pools

- **Top Elastic Pools by Storage percent** - List of the elastic pools with top used storage.

- **Top Elastic Pools by Sessions Percentage** - Shows the trend of sessions percent for top elastic pools



### METRICS

For more information about the metrics emitted by Azure SQL Elastic Pools, visit <a target="_blank" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-supported-metrics#microsoftsqlserverselasticpools">here</a>.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
