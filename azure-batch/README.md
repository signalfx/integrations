# ![](./img/integrations_azurebatch.png) Microsoft Azure Batch

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Azure Batch via [Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

#### FEATURES

##### Built-in dashboards

- **Azure Batch Accounts**: Shows metrics of all batch accounts being monitored. Users can select a single batch account to view metrics related to the single account.

  [<img src='./img/batch.png' width=200px>](./img/batch.png)

### INSTALLATION

To access this integration, [connect to Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

### USAGE

#### Interpreting Built-in dashboards

**Azure Batch Accounts**

- **Running Nodes** - Number of nodes running.

  [<img src='./img/batch.running.nodes.png' width=200px>](./img/batch.running.nodes.png)

- **Idle Nodes** - Number of nodes running.

  [<img src='./img/batch.idle.nodes.png' width=200px>](./img/batch.idle.nodes.png)

- **Offline Nodes** - Number of nodes running.

  [<img src='./img/batch.offline.nodes.png' width=200px>](./img/batch.offline.nodes.png)

- **Starting Nodes** - Number of nodes running.

  [<img src='./img/batch.starting.nodes.png' width=200px>](./img/batch.starting.nodes.png)

- **Node States** - Shows number of nodes in each of the states: creating, starting, running, idle or offline.

  [<img src='./img/batch.node.states.png' width=200px>](./img/batch.node.states.png)

- **Task States** - Shows number of tasks in each of the states: completed, failed, or started.

  [<img src='./img/batch.task.states.png' width=200px>](./img/batch.task.states.png)

- **Tasks Started** - Number of tasks that started.

  [<img src='./img/batch.tasks.started.png' width=200px>](./img/batch.tasks.started.png)

- **Tasks Completed** - Number of tasks completed.

  [<img src='./img/batch.tasks.completed.png' width=200px>](./img/batch.tasks.completed.png)

- **Tasks Failed** - Number of tasks failed.

  [<img src='./img/batch.tasks.failed.png' width=200px>](./img/batch.tasks.failed.png)

- **Number of Cores** - Number of in each of the Accounts.

  [<img src='./img/batch.cores.png' width=200px>](./img/batch.cores.png)

- **Pool Events** - Number of pool events in each of the states: creating, deleted, node leaving or resizing.

  [<img src='./img/batch.pool.events.png' width=200px>](./img/batch.pool.events.png)



### METRICS

For more information about the metrics emitted by Azure Batch, visit <a target="_blank" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-supported-metrics#microsoftbatchbatchaccounts">here</a>.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
