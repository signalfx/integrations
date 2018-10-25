# ![](./img/integration_googlecloudfunctions.png) Google Cloud Functions

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Google Cloud Functions via [Google Cloud Platform](https://github.com/signalfx/integrations/tree/master/gcp)[](sfx_link:gcp).

#### FEATURES

##### Built-in dashboards

- **Cloud Functions Overview**: Overview of project level metrics for Google Cloud Functions

  [<img src='./img/cloud_functions_overview.png' width=200px>](./img/cloud_functions_overview.png)

- **Cloud Function**: Metrics for a single cloud function

  [<img src='./img/cloud_function.png' width=200px>](./img/cloud_function.png)


### INSTALLATION

To access this integration, [connect to Google Cloud Platform](https://github.com/signalfx/integrations/tree/master/gcp)[](sfx_link:gcp).

### USAGE

#### Interpreting Built-in dashboards

**Cloud Function**

- **Executions / min** - Count of function executions per minute.

  [<img src='./img/function-exces-per-min.png' width=200px>](./img/function-exces-per-min.png)

- **Executions / min Trend** - Trend of function executions per minute.

  [<img src='./img/function-execs-per-min-trend.png' width=200px>](./img/function-execs-per-min-trend.png)

- **Average Execution Time (ms)** - Average execution time for a function.

  [<img src='./img/function-avg-exec-time.png' width=200px>](./img/function-avg-exec-time.png)

- **Average Execution Time (ms) Trend** - Average execution time trend for a function.

  [<img src='./img/function-avg-exec-time-trend.png' width=200px>](./img/function-avg-exec-time-trend.png)

**Cloud Functions Overview**

- **Executions / min** - List of executions per minute for all functions.

  [<img src='./img/functions-overview-execs-per-min.png' width=200px>](./img/functions-overview-execs-per-min.png)

- **Executions / min by Status** - List of function executions per minute grouped by status.

  [<img src='./img/functions-overview-execs-per-min-status.png' width=200px>](./img/functions-overview-execs-per-min-status.png)

- **Average Execution Time (ms)** - List of average execution times for all functions.

  [<img src='./img/functions-overview-exec-times.png' width=200px>](./img/functions-overview-exec-times.png)

- **Execution Time (ms)** - Trend of average execution times for all functions.

  [<img src='./img/functions-overview-exec-times.png' width=200px>](./img/functions-overview-exec-times.png)

### METRICS

For more information about the metrics emitted by Google Cloud Functions, visit the service's metric page at <a target="_blank" href="https://cloud.google.com/monitoring/api/metrics#gcp-cloudfunctions">https://cloud.google.com/monitoring/api/metrics#gcp-cloudfunctions</a>

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
