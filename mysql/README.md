# ![](./img/integrations_mysql.png) MySQL

#### FEATURES

##### Built-in dashboards

- **MySQL Nodes**: Overview of data from all MySQL nodes.

  [<img src='./img/dashboard_mysql_nodes.png' width=200px>](./img/dashboard_mysql_nodes.png)

- **MySQL Node**: Focus on a single MySQL node.

  [<img src='./img/dashboard_mysql_node.png' width=200px>](./img/dashboard_mysql_node.png)  


#### Note: Monitoring a MySQL environment that is configured for replication
If you have configured MySQL to use replication you may want to collect information relevant to the performance and status of your master and/or slave nodes. This can be achieved by utilizing the `MasterStats`, `SlaveStats`, and `SlaveNotifications` options as described in <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd-mysql/10-mysql.conf">10-mysql.conf</a>

### USAGE

Below are screen captures of dashboards created for this plugin by SignalFx, illustrating the metrics emitted by this plugin.

For general reference on how to monitor MySQL performance using this plugin, see <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:MySQL">documentation on collectd.org</a>.

**Monitoring multiple MySQL nodes**

![Example dashboard showing MySQL nodes](././img/MySQL_nodes_dashboard.png)

*Example dashboard showing performance of multiple MySQL nodes.*

**Monitoring a single MySQL node**

![Example dashboard showing a single MySQL host](././img/MySQL_node_dashboard.png)

*Example dashboard showing performance of a single MySQL node.*

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
