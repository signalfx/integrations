# ![](./img/integrations_hadoop.png) Apache Hadoop

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Apache Hadoop YARN, HDFS, and MapReduce.

#### FEATURES

##### Built-in dashboards
- **Hadoop YARN** Resource Manager and Application metrics

  [<img src='./img/yarn_resource_manager.png' width=200px>](./img/yarn_resource_manager.png)
  [<img src='./img/yarn_application.png' width=200px>](./img/yarn_application.png)

- **Hadoop HDFS** HDFS Overview, NameNode, and DataNode metrics

  [<img src='./img/hdfs_overview.png' width=200px>](./img/hdfs_overview.png)
  [<img src='./img/hdfs_namenode.png' width=200px>](./img/hdfs_namenode.png)
  [<img src='./img/hdfs_datanode.png' width=200px>](./img/hdfs_datanode.png)

- **Haddop MapReduce** MapReduce applications, jobs, and resource usage

  [<img src='./img/mapreduce_apps.png' width=200px>](./img/mapreduce_apps.png)
  [<img src='./img/mapreduce_jobs.png' width=200px>](./img/mapreduce_jobs.png)
  [<img src='./img/mapreduce_usage.png' width=200px>](./img/mapreduce_usage.png)

### INSTALLATION

To access this integration, [install the Collectd-Hadoop integration](https://github.com/signalfx/integrations/tree/master/collectd-hadoop).


### USAGE

SignalFx provides built-in dashboards for this service. Examples are shown above.


### METRICS

See the following links for more information of specific metrics:

>https://hadoop.apache.org/docs/r2.7.4/hadoop-project-dist/hadoop-common/Metrics.html

>https://hadoop.apache.org/docs/r2.7.4/hadoop-yarn/hadoop-yarn-site/ResourceManagerRest.html

>https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapredAppMasterRest.html

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
