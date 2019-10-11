# ![](./img/integrations_jenkins.png) Jenkins

### FEATURES

#### Built-in dashboards

- **Jenkins**: Provides a high-level overview of metrics for a jenkins cluster.

  [<img src='./img/jenkins-dashboard-top.png' width=200px>](./img/jenkins-dashboard-top.png)

  [<img src='./img/jenkins-dashboard-bottom.png' width=200px>](./img/jenkins-dashboard-bottom.png)  

- **Jenkins MASTER**: Provides metrics from jenkins instance(s) on a particular host.

  [<img src='./img/jenkins-master-dashboard.png' width=200px>](./img/jenkins-master-dashboard.png)  


### USAGE

#### Interpreting Built-in dashboards

- **Jenkins**:

  - **Alive Status**: Shows the number of Jenkins Masters that are alive.

    [<img src='./img/chart-jenkins-alive-status.png' width=200px>](./img/chart-jenkins-alive-status.png)

  - **Health Score**: Shows the mean health score of each Jenkins instance on all hosts.

    [<img src='./img/chart-jenkins-health-score.png' width=200px>](./img/chart-jenkins-health-score.png)

  - **Job Failure Rate**: Shows the rate of jobs failed in the past day.

    [<img src='./img/chart-jenkins-job-failure-rate.png' width=200px>](./img/chart-jenkins-job-failure-rate.png)

  - **Executor Usage**: Shows the usage pattern of the executors. Gives an overview of the load on the Jenkins instances.

    [<img src='./img/chart-jenkins-executor-usage.png' width=200px>](./img/chart-jenkins-executor-usage.png)

  - **Top 5 Failed Jobs**: Shows the top 5 failed jobs over the past day based on the total failure count.

    [<img src='./img/chart-jenkins-top-5-failed-jobs.png' width=200px>](./img/chart-jenkins-top-5-failed-jobs.png)

  - **Busy Executors vs Pending Jobs**: A line graph showing comparison between in-use executors and pending jobs in queue. On comparing this chart with two above, reason for job failures can be narrowed down further quickly.

    [<img src='./img/chart-jenkins-busy-executors-vs-pending-jobs.png' width=200px>](./img/chart-jenkins-busy-executors-vs-pending-jobs.png)

  - **Average Duration - Past Day**: Shows average duration of top 5 jobs that are taking the most time.

    [<img src='./img/chart-jenkins-average-duration-past-day.png' width=200px>](./img/chart-jenkins-average-duration-past-day.png)

  - **Slave Status**: Shows the number of slave agents that are alive.

    [<img src='./img/chart-jenkins-slave-status.png' width=200px>](./img/chart-jenkins-slave-status.png)

  - **VM Memory Utilization**: Area graph of the memory used by each Jenkins JVM.

    [<img src='./img/chart-jenkins-vm-memory-utilization.png' width=200px>](./img/chart-jenkins-vm-memory-utilization.png)

  - **Heap Usage**: Line graph of the utilization percentage of Heap memory by each Jenkins instance.

    [<img src='./img/chart-jenkins-heap-usage.png' width=200px>](./img/chart-jenkins-heap-usage.png)

  - **Non-Heap Used**: Line graph of the non-heap memory used by each Jenkins instance.

    [<img src='./img/chart-jenkins-non-heap-used.png' width=200px>](./img/chart-jenkins-non-heap-used.png)

- **Jenkins Master**:

  - **Top 5 Failed Jobs**: Shows the top 5 failed jobs over the past day based on the total failure count in an instance(s).
    
    [<img src='./img/chart-jenkins-master-top-5-failed-jobs.png' width=200px>](./img/chart-jenkins-master-top-5-failed-jobs.png)

  - **Health Checks**: The status of each health check as reported by DropWizard Metrics. This gives a quick overview of what's wrong with the instance.

    [<img src='./img/chart-jenkins-master-health-checks.png' width=200px>](./img/chart-jenkins-master-health-checks.png)

  - **Slave Status**: Shows the number of slave agents of the instance(s) that are alive.
  
      [<img src='./img/chart-jenkins-master-slave-status.png' width=200px>](./img/chart-jenkins-master-slave-status.png)

  - **Busy Executors vs Pending Jobs**: A line chart showing comparison between in-use executors and pending jobs in queue in an instance(s). On comparing this chart with two above, reason for job failures can be narrowed down further quickly.
  
      [<img src='./img/chart-jenkins-master-busy-executors-vs-pending-jobs.png' width=200px>](./img/chart-jenkins-busy-executors-vs-pending-jobs.png)
  
  - **VM Memory Utilization**: Area chart of the memory used by the Jenkins JVM instance(s) on a host.
  
      [<img src='./img/chart-jenkins-master-vm-memory-utilization.png' width=200px>](./img/chart-jenkins-vm-memory-utilization.png)

All DropWizard metrics reported by the jenkins collectd plugin will not contain any dimensions by default. Whereas, the job metrics sent will contain the following dimensions by default:

* `Job`, name of the job
* `Result`, the status of the job

A few other details:

* `plugin` is always set to `jenkins`
* `plugin_instance` will contain the IP address and the port of the member given in the configuration
* To add metrics from the `/metrics/<MetricsKey>/metrics` endpoint, use the configuration options mentioned in [configuration](#configuration). If metrics are being included individually, make sure to give names that are valid. For example, `vm.daemon.count` or `vm.terminated.count`


### ADDITIONAL METRIC INFO
By default, metrics about a job and instance are provided. Metrics from `/metrics/<MetricsKey>/metrics` endpoint can be activated through the configuration file. Note, that SignalFx does not support `histograms`, `meter` and `timer` metric types as they are too verbose in Jenkins and also values of type string and list(hence, metrics of these will be skipped if provided in the configuration). See [usage](#usage) for details.


#### Metric naming
`<metric type>.jenkins.node.<name of metric>`. This is the format of default metric names reported by the plugin. Optional metrics are named as available from the `/metrics/<MetricsKey>/metrics` endpoint.


### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
