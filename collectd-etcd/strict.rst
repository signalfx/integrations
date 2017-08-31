|image0| etcd
=============

*This directory consolidates all the metadata associated with the etcd
plugin for collectd. The relevant code for the plugin can be found
`here <https://github.com/signalfx/collectd-etcd>`__*

-  `Description <#description>`__
-  `Requirements and Dependencies <#requirements-and-dependencies>`__
-  `Installation <#installation>`__
-  `Configuration <#configuration>`__
-  `Usage <#usage>`__
-  `Metrics <#metrics>`__
-  `License <#license>`__

DESCRIPTION
~~~~~~~~~~~

This is the SignalFx etcd plugin. Follow these instructions to install
the etcd plugin for collectd.

The ```etcd-collectd`` <https://github.com/signalfx/collectd-etcd>`__
plugin collects metrics from etcd instances hitting these endpoints:
`statistics <https://coreos.com/etcd/docs/latest/v2/api.html#statistics>`__
(default metrics) and
`metrics <https://coreos.com/etcd/docs/latest/v2/metrics.html>`__
(optional metrics).

FEATURES
^^^^^^^^

Built-in dashboards
^^^^^^^^^^^^^^^^^^^

-  **ETCD CLUSTER**: Provides a high-level overview of metrics for a
   single etcd cluster.

` <./img/etcd-cluster-dashboard-top.png>`__

` <./img/etcd-cluster-dashboard-bottom.png>`__

-  **ETCD INSTANCE**: Provides metrics from a single etcd instance.

` <./img/etcd-instance-dashboard.png>`__

-  **ETCD INSTANCES**: Provides metrics from hosts on a particular host.

` <./img/etcd-instance-dashboard.png>`__

REQUIREMENTS AND DEPENDENCIES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Version information
^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <table>

.. raw:: html

   <thead>

.. raw:: html

   <tr class="header">

.. raw:: html

   <th>

Software

.. raw:: html

   </th>

.. raw:: html

   <th>

Version

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   </thead>

.. raw:: html

   <tbody>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

collectd

.. raw:: html

   </td>

.. raw:: html

   <td>

4.9 or later

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>

python

.. raw:: html

   </td>

.. raw:: html

   <td>

2.6 or later

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

etcd

.. raw:: html

   </td>

.. raw:: html

   <td>

2.0.8 or later

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>

Python plugin for collectd

.. raw:: html

   </td>

.. raw:: html

   <td>

(included with SignalFx collectd agent)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

INSTALLATION
~~~~~~~~~~~~

1. Download
   `collectd-etcd <https://github.com/signalfx/collectd-etcd>`__. Place
   the ``etcd_plugin.py`` file in ``/usr/share/collectd/collectd-etcd``

2. Modify the `sample configuration
   file <https://github.com/signalfx/integrations/tree/release/collectd-etcd/10-etcd.conf>`__
   for this plugin to ``/etc/collectd/managed_config``

3. Modify the sample configuration file as described in
   `Configuration <#configuration>`__, below

4. Install the Python requirements with sudo
   ``pip install -r requirements.txt``

5. Restart collectd

CONFIGURATION
~~~~~~~~~~~~~

Using the example configuration file
`10-etcd.conf <https://github.com/signalfx/integrations/tree/release/collectd-etcd/10-etcd.conf>`__
as a guide, provide values for the configuration options listed below
that make sense for your environment and allow you to connect to the
etcd members

.. raw:: html

   <table style="width:71%;">

.. raw:: html

   <colgroup>

.. raw:: html

   <col width="30%" />

.. raw:: html

   <col width="18%" />

.. raw:: html

   <col width="22%" />

.. raw:: html

   </colgroup>

.. raw:: html

   <thead>

.. raw:: html

   <tr class="header">

.. raw:: html

   <th>

configuration option

.. raw:: html

   </th>

.. raw:: html

   <th>

definition

.. raw:: html

   </th>

.. raw:: html

   <th>

example value

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   </thead>

.. raw:: html

   <tbody>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

ModulePath

.. raw:: html

   </td>

.. raw:: html

   <td>

Path on disk where collectd can find this module.

.. raw:: html

   </td>

.. raw:: html

   <td>

"/usr/share/collectd/collectd-etcd/"

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>

Host

.. raw:: html

   </td>

.. raw:: html

   <td>

Host name of the etcd member

.. raw:: html

   </td>

.. raw:: html

   <td>

"localhost"

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

Port

.. raw:: html

   </td>

.. raw:: html

   <td>

Port at which the member can be reached

.. raw:: html

   </td>

.. raw:: html

   <td>

"2379"

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>

Cluster

.. raw:: html

   </td>

.. raw:: html

   <td>

Name of this etcd cluster.

.. raw:: html

   </td>

.. raw:: html

   <td>

"1"

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

EnhancedMetrics

.. raw:: html

   </td>

.. raw:: html

   <td>

Boolean to indicate whether stats from /metrics are needed

.. raw:: html

   </td>

.. raw:: html

   <td>

"false"

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>

IncludeMetric

.. raw:: html

   </td>

.. raw:: html

   <td>

Metric name from the /metric endpoint to include(valid when
EnhancedMetrics is "false")

.. raw:: html

   </td>

.. raw:: html

   <td>

"etcd\_debugging\_mvcc\_slow\_watcher\_total"

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

ExcludeMetric

.. raw:: html

   </td>

.. raw:: html

   <td>

Metric name from the /metric endpoint to exclude(valid when
EnhancedMetrics is "true")

.. raw:: html

   </td>

.. raw:: html

   <td>

"etcd\_server\_has\_leader"

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>

Dimension

.. raw:: html

   </td>

.. raw:: html

   <td>

Space separated key-value pair for a user-defined dimension

.. raw:: html

   </td>

.. raw:: html

   <td>

dimension\_name dimension\_value

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

Interval

.. raw:: html

   </td>

.. raw:: html

   <td>

Number of seconds between calls to etcd API.

.. raw:: html

   </td>

.. raw:: html

   <td>

10

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>

ssl\_keyfile

.. raw:: html

   </td>

.. raw:: html

   <td>

Path to the keyfile

.. raw:: html

   </td>

.. raw:: html

   <td>

"path/to/file"

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

ssl\_certificate

.. raw:: html

   </td>

.. raw:: html

   <td>

Path to the certificate

.. raw:: html

   </td>

.. raw:: html

   <td>

"path/to/file"

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>

ssl\_ca\_certs

.. raw:: html

   </td>

.. raw:: html

   <td>

Path to the ca file

.. raw:: html

   </td>

.. raw:: html

   <td>

"path/to/file"

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

Example configuration:

::

    LoadPlugin python
    <Plugin python>
      ModulePath "/usr/share/collectd/collectd-etcd/"

      Import etcd_plugin
      <Module etcd_plugin>
        Host "localhost"
        Port "2379"
        Interval 10
        Cluster "1"
        Dimension dimension_name dimension_value
        EnhancedMetrics False
        IncludeMetric metric_name_from_metrics_endpoint
        ssl_keyfile "/Users/as001/work/play/etcd/etcd-ca/etcd-ca/private/etcd-client.key"
        ssl_certificate "/Users/as001/work/play/etcd/etcd-ca/etcd-ca/certs/etcd-client.crt"
        ssl_ca_certs "/Users/as001/work/play/etcd/etcd-ca/etcd-ca/certs/ca.crt"
      </Module>
    </Plugin>

The plugin can be configured to collect metrics from multiple instances
in the following manner.

::

    LoadPlugin python

    <Plugin python>
      ModulePath "/usr/share/collectd/collectd-etcd/"
      Import etcd_plugin
      <Module etcd_plugin>
        Host "localhost"
        Port "2379"
        Interval 10
        Cluster "prod"
      </Module>
      <Module etcd_plugin>
        Host "localhost"
        Port "22379"
        Interval 10
        Cluster "prod"
        IncludeMetric "etcd_debugging_mvcc_slow_watcher_total"
        IncludeMetric "etcd_debugging_store_reads_total"
        IncludeMetric "etcd_server_has_leader"
        IncludeMetric "etcd_network_peer_sent_bytes_total"
      </Module>
      <Module etcd_plugin>
        Host "localhost"
        Port "32379"
        Interval 10
        Cluster "test"
      </Module>
    </Plugin>

USAGE
~~~~~

Interpreting Built-in dashboards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  **ETCD CLUSTER**:

-  **Number of Followers**: Shows the number of followers in the
   cluster. A cluster that is expected to have 2n + 1 members, can
   tolerate failure of n members. By virtue of raft consensus algorithm,
   a cluster should have at least 3 members.

   ` <./img/chart-etcd-cluster-number-followers.png>`__

-  **Number of Watchers**: Shows the total number of watchers on all the
   members of the cluster put together. Gives an overview of memory
   consumption by the watchers on the cluster as a whole.

   ` <./img/chart-etcd-cluster-number-watchers.png>`__

-  **Followers with Max Number of Watchers**: Get an overview of the
   members that are being requested for watching. Watching is memory
   intensive. The list gives information about the members
   (``host:port`` information) and the corresponding states.

   ` <./img/chart-etcd-cluster-Max-Watchers.png>`__

-  **Top Current Latency**: Gives an overview of the followers
   (``host:port``) with max current latency with the leader. Since raft
   relies on log replication throughout all the members, this is helps
   in flushing out followers that have max latency.

   ` <./img/chart-etcd-cluster-top-latency.png>`__

-  **Total RPC Requests (successful/failed)**: A stacked chart that
   shows successful (in green) and failed (in red) RPC requests per
   second across all the followers. Leader sends RPC requests and
   followers receive.

   ` <./img/chart-etcd-cluster-total-rpcs.png>`__

-  **Per Member Failed RPCs**: A stacked chart showing failed RPC
   requests per second on a per follower basis. On comparing this chart
   with one above, followers that cause more failures can be flushed
   out.

   ` <./img/chart-etcd-cluster-member-rpc-failure.png>`__

-  **Top RPC Requests**: Followers with top RPC requests, both
   successful and failed.

   ` <./img/chart-etcd-cluster-top-rpcs.png>`__

-  **Store operations (successful/failed)**: This includes the following
   charts: Creates, Sets, Updates, Deletes, Compare-and-Swaps and
   Compare-and-Deletes. These charts are stacked charts that show
   successful operations (in green) and failed operations (in red) per
   second. This gives an idea of the ratio between success and failure
   for each operation type.

   ` <./img/chart-etcd-cluster-creates.png>`__
   ` <./img/chart-etcd-cluster-sets.png>`__
   ` <./img/chart-etcd-cluster-updates.png>`__
   ` <./img/chart-etcd-cluster-deletes.png>`__
   ` <./img/chart-etcd-cluster-cas.png>`__
   ` <./img/chart-etcd-cluster-cad.png>`__

-  **Receive Packet Rate**: Stacked chart of the packets received per
   second for each follower. At given point in time, followers receive
   packets from the leader (leader sends information as part of log
   replication).

   ` <./img/chart-etcd-cluster-packet-recv.png>`__

-  **Receive Append Requests**: Stacked chart of the append requests
   received per second for each follower. At given point in time,
   followers receive append requests from the leader (leader sends
   information as part of log replication).

   ` <./img/chart-etcd-cluster-append-recv.png>`__

-  **Send Packet Rate**: Chart for the packets sent per second for the
   leader. At given point in time, only leader sends packets. In the
   ideal world, every packet sent by the leader should be received by
   one of the followers. Comparing this chart with **Receive Packet
   Rate** would explain if packets are not received by followers (or an
   individual follower). Latency can also be observed through these
   charts.

   ` <./img/chart-etcd-cluster-packet-sent.png>`__

-  **Send Append Requests**: Chart for the append requests sent per
   second for the leader. At given point in time, only leader sends
   append requests. In the ideal world, all append requests sent by the
   leader should be received by one of the followers. Comparing this
   chart with **Receive Append Requests** would explain if append
   requests are not received by followers (or an individual follower).
   Latency can also be observed through these charts.

   ` <./img/chart-etcd-cluster-append-sent.png>`__

-  **ETCD INSTANCE**:

-  **Number of Watchers**: Shows the number of watchers on this
   particular instance. Watching is memory intensive and might explain
   high memory utilization.

   ` <./img/chart-etcd-instance-number-watchers.png>`__

-  **Expire Rate**: The number of keys and directories that expire per
   second. This is common to the distributed key-value store. However,
   when a member leaves the cluster, this metric becomes instance
   specific.

   ` <./img/chart-etcd-instance-expire-rate.png>`__

-  **Gets (successful/failed)**: A stacked chart that shows successful
   gets (in green) and failed gets (in red) per second. This gives
   insight to the ratio between successful and failed get requests per
   second for the instance. It is possible that a high fail count for
   gets is because of a high expire rate.

   ` <./img/chart-etcd-instance-gets.png>`__

-  **Receive / Send Bandwidth Rate** A line graph showing both, sent (in
   blue) and received (in green) bandwidth rate for the instance.
   Followers receive and Leader sends.

   ` <./img/chart-etcd-instance-bandwidth.png>`__

-  **Receive / Send Append Requests** A line graph showing both, sent
   (in blue) and received (in green) append requests per second for the
   instance. Followers receive and Leader sends.

   ` <./img/chart-etcd-instance-appends.png>`__

-  **ETCD INSTANCES**: Provides metrics from hosts on a particular host.

-  **Number of instances**: The total number of etcd isntances running
   on the host, group by type (follower/leader).

   ` <./img/chart-etcd-instances-number-instances.png>`__

-  **Instances by Number of Watchers**: A line graph that shows number
   of watchers on each of the instances on the host. Instances with more
   number of watchers consume more memory.

   ` <./img/chart-etcd-instances-number-watchers.png>`__

-  **Instances with Most Number of Wacthers**: Shows the instances with
   most number of watchers. Watching is memory intensive.

   ` <./img/chart-etcd-instances-most-watchers.png>`__

-  **Packets Exchange Trend**: A stacked chart showing packets sent (in
   blue) and received (in green) across all instances on the host. Gives
   an idea of bandwidth usage.

   ` <./img/chart-etcd-instances-packets.png>`__

-  **Bandwidth Trend Rate**: A stacked chart showing send bandwidth (in
   blue) and receive bandwidth (in green) rates across all instances on
   the host. Gives an idea of bandwidth usage and should shows similar
   trends as the above chart.

   ` <./img/chart-etcd-instances-bandwidth.png>`__

-  **Top Bandwidth Rate**: Gives a list of the instances that consume
   max bandwidth, both for sending and receiving put together.

   ` <./img/chart-etcd-instances-top-bandwidth.png>`__

-  **Gets Successful Trend**: A stacked chart showing the number of
   successful get operations per second for each of the instances
   running on the host.

   ` <./img/chart-etcd-instances-gets-success.png>`__

-  **Gets Failed Trend**: A stack chart showing the number of failed get
   operations per second for each of the instances running on the host.
   Compare with above chart to analyze the success ratio.

   ` <./img/chart-etcd-instances-gets-fail.png>`__

-  **Top Gets per second** A list of the instances on the host that
   perform the max number of gets per second, both successful and failed
   gets put together.

   ` <./img/chart-etcd-instances-gets-top.png>`__

-  **Expire Rate Trend**: A line chart showing the rate of expiry of
   keys/directories for all the instances on host.

` <./img/chart-etcd-instances-expire-trend.png>`__

-  **Top Expire Rate**: A list of instances with top expire rates. Can
   be used to analyze if gets fail due to a high expiry rate.

   ` <./img/chart-etcd-instances-top-expire.png>`__

All metrics reported by the etcd collectd plugin will contain the
following dimensions by default:

-  ``state``, whether the member is a follower or a leader
-  ``cluster``, human readable cluster name used to group by members by
   cluster
-  ``follower``, metrics from the leader endpoint will have this
   dimension to group by follower

A few other details:

-  ``plugin`` is always set to ``etcd``
-  ``plugin_instance`` will contain the IP address and the port of the
   member given in the configuration
-  To add metrics from the ``/metrics`` endpoint, use the configuration
   options mentioned in `configuration <#configuration>`__. If metrics
   are being included individually, make sure to give names that are
   valid. For example, ``etcd_debugging_mvcc_slow_watcher_total`` or
   ``etcd_network_peer_sent_bytes_total``

METRICS
~~~~~~~

By default, metrics about a member, leader and store are provided. Click
`here <./docs>`__ for details. Metrics from ``/metrics`` endpoint can be
activated through the configuration file. Note, that SignalFx does not
support ``histogram`` and ``summary`` metric types (hence, metrics of
these will be skipped if provided in the configuration). See
`usage <#usage>`__ for details.

Metric naming
^^^^^^^^^^^^^

``<metric type>.etcd.<endpoint name>.<name of metric>``. This is the
format of default metric names reported by the plugin. Optional metrics
are named as available from the ``/metrics`` endpoint with ``_``
replaced by ``.``.

LICENSE
~~~~~~~

This integration is released under the Apache 2.0 license. See
`LICENSE <./LICENSE>`__ for more details.

.. |image0| image:: ./img/integrations_etcd.png

