# ![](./img/integrations_azurelogicapps.png) Microsoft Azure Logic Apps

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Azure Logic Apps via [Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

#### FEATURES

##### Built-in dashboards

- **Azure Logic App**: Shows metrics of a Logic App.

  [<img src='./img/logic.png' width=200px>](./img/logic.png)

- **Azure Logic Apps**: Shows metrics of all Logic Apps being monitored.

  [<img src='./img/logics.png' width=200px>](./img/logics.png)


### INSTALLATION

To access this integration, [connect to Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

### USAGE

#### Interpreting Built-in dashboards

**Azure Logic App**

- **Billable Executions** - Number of billable actions/triggers by app.

  [<img src='./img/logic.billable.png' width=200px>](./img/logic.billable.png)

- **Runs Completed** - Number of workflow runs that have completed for the app.

  [<img src='./img/logic.runs.completed.png' width=200px>](./img/logic.runs.completed.png)

- **Actions Completed** - Number of actions that completed for the app.

  [<img src='./img/logic.actions.completed.png' width=200px>](./img/logic.actions.completed.png)

- **Runs Succeeded / Failed / Throttled** - Number of workflow runs that succeeded/failed/got throttled for the app.

  [<img src='./img/logic.runs.png' width=200px>](./img/logic.runs.png)

- **Actions Succeeded / Failed / Throttled** - Number of actions that succeeded/failed/got throttled for the app.

  [<img src='./img/logic.actions.png' width=200px>](./img/logic.actions.png)

- **Triggers Succeeded / Failed / Throttled** - Number of triggers that succeeded/failed/got throttled for the app.

  [<img src='./img/logic.triggers.png' width=200px>](./img/logic.triggers.png)

- **Run Latency (s)** - Run latency for the app.

  [<img src='./img/logic.run.latency.png' width=200px>](./img/logic.run.latency.png)

- **Action Latency (s)** - Action latency for the app.

  [<img src='./img/logic.action.latency.png' width=200px>](./img/logic.action.latency.png)

**Azure Logic Apps**

- **Runs Succeeded** - Aggregated number of workflow runs that succeed.

  [<img src='./img/logics.run.succeeded.png' width=200px>](./img/logics.run.succeeded.png)

- **Successful Run Latency (s)** - Average latency of succeeded workflow runs.

  [<img src='./img/logics.success.runlatency.png' width=200px>](./img/logics.success.runlatency.png)

- **Runs Failed** - Aggregated number of workflow runs that failed.

  [<img src='./img/logics.runs.failed.png' width=200px>](./img/logics.runs.failed.png)

- **Runs Throttled** - Aggregated number of workflow runs that throttled.

  [<img src='./img/logics.runs.throttled.png' width=200px>](./img/logics.runs.throttled.png)

- **Runs Completed** - Aggregated number of workflow runs that completed.

  [<img src='./img/logics.runs.completed.png' width=200px>](./img/logics.runs.completed.png)

- **Total Billable Executions** - Aggregated number of workflow executions that are billed.

  [<img src='./img/logics.billable.png' width=200px>](./img/logics.billable.png)




### METRICS

For more information about the metrics emitted by Azure Logic Apps, visit <a target="_blank" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-supported-metrics#microsoftlogicworkflows">here</a>.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
