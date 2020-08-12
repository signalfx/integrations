# ![](./img/integration_googlecloudfunctions.png) Google Cloud Functions

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

## DESCRIPTION

To monitor Google Cloud Functions, integrate SignalFx with [Google Cloud Platform](https://docs.signalfx.com/en/latest/integrations/google-cloud-platform.html#connect-to-gcp).

### Wrappers

You can monitor the health and performance of Google Cloud Functions through metrics on total invocations, errors, durations, and more. In addition, you can send custom application or business metrics from within Google Cloud Functions.

- You can use a language-specific wrapper to monitor your functions. Using a wrapper lets you see invocations, errors, and durations for your functions in real time, and also provides insight into whether a given function is being impacted by cold starts.
- The wrapper is also a way for you to send in custom application or business metrics from within a function, analogous to what you can do with client libraries for code running in non-Function environments. See [Wrappers](https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.google.cloud.functions.html#wrappers) for more information.

## FEATURES

### Built-in dashboards

- **Cloud Functions Overview:** Overview of project-level metrics for Google Cloud Functions.

  [<img src='./img/cloud_functions_overview.png' width=200px>](./img/cloud_functions_overview.png)

- **Cloud Function:** Metrics for a single cloud function.

  [<img src='./img/cloud_function.png' width=200px>](./img/cloud_function.png)


## INSTALLATION

To access this integration, [connect to Google Cloud Platform](https://docs.signalfx.com/en/latest/integrations/google-cloud-platform.html#connect-to-gcp).

### Prerequisites

None

### Wrappers

#### Differences between the SignalFx Wrapper and Google Cloud Monitoring

##### Step 1: Review and select a deployment method

You can use both the SignalFx Wrapper and Google Cloud Monitoring methods to monitor functions at the same time, or you can choose to only use one method.

Before you select a method, consider the following statements:
- Each method sends different metrics and uses different properties to uniquely identify a cloud function.
- Google Cloud Monitoring data is reported with a delay. The time varies according to the monitored resource and other factors. The SignalFx Wrapper sends data immediately when it becomes available.
- Google Cloud Monitoring data is sent automatically for all Google Cloud Functions, whereas the SignalFx Wrapper needs to be added to each function.
- The SignalFx Wrapper is the only method that can send custom applications or business metrics from within Google Cloud Functions.

##### Step 2: Review set up documentation

*Option 1: Use the SignalFx Wrapper*

You can include the SignalFx Wrapper in your Google Cloud Functions to provide real-time monitoring, as well as the ability to send custom metrics from your applications to SignalFx.

To view the three installation methods for each Google Cloud Functions wrapper, review the following README files:
- <a href="https://github.com/signalfx/serverless-go/blob/master/gcfwrapper/README.md" target="_blank">Go</a>
- <a href="https://github.com/signalfx/serverless-nodejs/blob/master/gcf-wrapper/README.md" target="_blank">Node.js</a>
- <a href="https://github.com/signalfx/serverless-python/blob/master/signalfx_gcf/README.rst" target="_blank">Python</a>

*Option 2: Use Google Cloud Monitoring*

By default, SignalFx imports all Google Cloud Monitoring metrics that are available in your account. To retrieve metrics for a subset of available services or regions, you need to modify the connection on the Integrations page.

For more information, see <a href="https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.google.cloud.platform.html">connect to Google Cloud Platform</a>.

## USAGE

### Interpreting Built-in Dashboards

**Cloud Function**

- **Executions / min:** Count of function executions per minute.

  [<img src='./img/function-exces-per-min.png' width=200px>](./img/function-exces-per-min.png)

- **Executions / min Trend:** Trend of function executions per minute.

  [<img src='./img/function-execs-per-min-trend.png' width=200px>](./img/function-execs-per-min-trend.png)

- **Average Execution Time (ms):** Average execution time for a function.

  [<img src='./img/function-avg-exec-time.png' width=200px>](./img/function-avg-exec-time.png)

- **Average Execution Time (ms) Trend:** Average execution time trend for a function.

  [<img src='./img/function-avg-exec-time-trend.png' width=200px>](./img/function-avg-exec-time-trend.png)

**Cloud Functions Overview**

- **Executions / min:** List of executions per minute for all functions.

  [<img src='./img/functions-overview-execs-per-min.png' width=200px>](./img/functions-overview-execs-per-min.png)

- **Executions / min by Status:** List of function executions per minute grouped by status.

  [<img src='./img/functions-overview-execs-per-min-status.png' width=200px>](./img/functions-overview-execs-per-min-status.png)

- **Average Execution Time (ms):** List of average execution times for all functions.

  [<img src='./img/functions-overview-exec-times.png' width=200px>](./img/functions-overview-exec-times.png)

- **Execution Time (ms):** Trend of average execution times for all functions.

  [<img src='./img/functions-overview-exec-times.png' width=200px>](./img/functions-overview-exec-times.png)

## METRICS

For more information about the metrics emitted by Google Cloud Functions, see <a target="_blank" href="https://cloud.google.com/monitoring/api/metrics#gcp-cloudfunctions">Metrics list</a>.

#### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
