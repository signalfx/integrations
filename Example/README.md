# SAMPLE README.MD

>This is a SAMPLE repository to be used as a template for submitting plugins for to the SignalFX validated directory
>This README will provide examples of the following:
>
>- REPO Structure
>- Sample `README.md` (this file)
>- code SAMPLES:
>  - Python
>  - C
>  - JMX
>- Sample Config
>- Sample YAML (for directory metadata)
>
> In this document, sections in block quotes (like this one) contain instructions for plugin authors. Remove them before submitting your contribution. 

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

> This file outlines the requirements for monitoring plugins that are included in SignalFx’s list of validated solutions. 
>
> In order to be validated, the repository for a monitoring plugin must contain the following:
>
>- A LICENSE file 
>- Code for the plugin
>- Configuration for the plugin
>- A YAML file that describes the plugin 
>- Documentation of the metrics emitted by the plugin
>- A README file formatted as in this example. 

collectd-rabbitmq is a collectd plugin that collects statistics from [RabbitMQ](http://rabbitmq.com). The plugin uses the [RabbitMQ Management HTTP API](http://hg.rabbitmq.com/rabbitmq-management/raw-file/rabbitmq_v3_3_4/priv/www/api/index.html) to poll for statistics on a RabbitMQ server, then reports them to collectd.

When collectd is configured to publish metrics to SignalFx, metrics from this plugin will be named according to the format: <metric type>.<category>.<statistic>

For example:

```
gauge.connection.recv_oct_details.rate
counter.connection.send_oct
gauge.queue.message_stats.deliver_get_details.rate
```

### REQUIREMENTS AND DEPENDENCIES

>In this section, list:
>- collectd version requirements
>- Version and configuration requirements for the application being monitored
>- Other plugins that this plugin depends on (like the Python or Java plugins for collectd)
>- Any other dependencies that this plugin requires in order to run successfully

This plugin requires: 

- Collectd 4.9 or later
- Python 2.6 or later
- Python plugin for collectd ??version??
- RabbitMQ 3.0 or later
- [RabbitMQ Management Plugin](https://www.rabbitmq.com/management.html)

### INSTALLATION

>In this section, provide step-by-step instructions that a user can follow to install this plugin. Each step should allow the user to verify that it has been completed successfully. 
>
>This section should also contain instructions for any steps that the user must take to modify or reconfigure the software to be monitored. For instance, the plugin might collect data from an API endpoint that must be enabled by the user.

Before installing this plugin, make sure that the server on which it will run satisfies the dependencies listed above. 

1. Download the contents of this repository to the collectd server on which it will run. 
1. Supply configuration for this module in `10-rabbitmq.conf`. See *Configuration* section below for details. 
1. Add the following line to `/etc/collectd.conf`, replacing the example path with the location of the configuration file you modified in the last step.

```
include `/path/to/10-rabbitmq.conf`
```

1. Restart collectd. 

To verify that this plugin has been installed and is emitting metrics, ??????what??

### CONFIGURATION 

>Provide in this section instructions on how to configure the plugin, before and after installation. If this plugin has a configuration file with properties then list each property, define its purpose and give an example or list the default value.

An example configuration file for this plugin can be found here in this repository: `[10-rabbitmq.conf](linky)`

#### Required configuration 

The following configuration options are *required* and have no defaults. This means that they must be present in the configuration file `10-rabbitmq.conf` in order for the plugin to work:

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| ModulePath | The location on disk of this module. | `/opt/collectd-rabbitmq` |
| Username | The username that this plugin will use to connect to RabbitMQ | `guest` | 
| Password | The password that this plugin will use to connect to RabbitMQ | `guest` | 
| Host | hostname or IP address of the RabbitMQ server running the RabbitMQ Management Plugin | `localhost` | 
| Port | The port at which this plugin can access the RabbitMQ Management API | `15672` |

#### Optional configuration 

The following boolean configuration options specify the data that will be collected by this plugin. Specify them in the configuration file with value `true` to enable collection of specific statistics:

| configuration option | definition | default value |
| ---------------------|------------|---------------| 
| CollectChannels | When `true`, enables collection of channel statistics | `false` |
| CollectConnections | When `true`, enables collection of connection statistics | `false` |
| CollectExchanges | When `true`, enables collection of exchange statistics | `false` |
| CollectNodes |  When `true`, enables collection of node statistics | `false` |
| CollectQueues | When `true`, enables collection of queue statistics | `false` | 

The following configuration options are *optional*. You may specify them in the configuration file in order to override default values provided by the plugin. 

| configuration option | definition | default value |
| ---------------------|------------|---------------|
| HTTPTimeout | Integer value in seconds to wait before timing out when connecting to the RabbitMQ Management API. | 1 | 
| FieldLength | Set the number of characters used to encode dimension data. Set this option *only* if you specifically compiled collectd with a non-default value for `DATA_MAX_NAME_LEN` in `plugin.h`. | 63 |

### USAGE

>This section contains information about how best to monitor the software in question, using the data from this plugin. In this section, the plugin author shares experience and expertise with the software to be monitored, for the benefit of users of the plugin. This section includes:
>
>- Important conditions to watch out for in the software
>- Common failure modes, and the values of metrics that will allow the user to spot them
>- Charts demonstrating each important condition or failure mode

### METRICS

>In this section, list and define each metric that this plugin emits. Metric names can be difficult to understand, and users need clear definitions in order to interpret the data that they see in their environments.
>
>If this plugin emits metrics that can be grouped together by level of analysis or by topic, group their definitions together. For example, a plugin that monitors software running on distributed systems may emit metrics about a single instance of the software as well as the health of the cluster as a whole. 

The statistics collected by this plugin are grouped by category. 

#### Channels

| metric name | type | definition | 
| ------------|------|------------|
| counter.channel.message_stats.ack.md | counter | definition |
| counter.channel.message_stats.confirm.md | counter | definition |
| counter.channel.message_stats.deliver.md | counter | definition |
| counter.channel.message_stats.deliver_get.md | counter | definition |
| counter.channel.message_stats.publish.md | counter | definition |
| gauge.channel.connection_details.peer_port.md | gauge | definition |
| gauge.channel.consumer_count.md | gauge | definition |
| gauge.channel.global_prefetch_count.md | gauge | definition |
| gauge.channel.message_stats.ack_details.rate.md | gauge | definition |
| gauge.channel.message_stats.confirm_details.rate.md | gauge | definition |
| gauge.channel.message_stats.deliver_details.rate.md | gauge | definition |
| gauge.channel.message_stats.deliver_get_details.rate.md | gauge | definition |
| gauge.channel.message_stats.publish_details.rate.md | gauge | definition |
| gauge.channel.messages_unacknowledged.md | gauge | definition |
| gauge.channel.messages_uncommitted.md | gauge | definition |
| gauge.channel.messages_unconfirmed.md | gauge | definition |
| gauge.channel.number.md | gauge | definition |
| gauge.channel.prefetch_count.md | gauge | definition |

#### Connections

| metric name | type | definition | 
| ------------|------|------------|
| counter.connection.channel_max.md | counter | definition |
| counter.connection.recv_cnt.md | counter | definition |
| counter.connection.recv_oct.md | counter | definition |
| counter.connection.send_cnt.md | counter | definition |
| counter.connection.send_oct.md | counter | definition |
| gauge.connection.channels.md | gauge | definition |
| gauge.connection.connected_at.md | gauge | definition |
| gauge.connection.frame_max.md | gauge | definition |
| gauge.connection.peer_port.md | gauge | definition |
| gauge.connection.port.md | gauge | definition |
| gauge.connection.recv_oct_details.rate.md | gauge | definition |
| gauge.connection.send_oct_details.rate.md | gauge | definition |
| gauge.connection.send_pend.md | gauge | definition |
| gauge.connection.timeout.md | gauge | definition |

#### Exchanges

| metric name | type | definition | 
| ------------|------|------------|
| counter.exchange.message_stats.confirm.md | counter | definition |
| counter.exchange.message_stats.publish_in.md | counter | definition |
| counter.exchange.message_stats.publish_out.md | counter | definition |
| gauge.exchange.message_stats.confirm_details.rate.md | gauge | definition |
| gauge.exchange.message_stats.publish_in_details.rate.md | gauge | definition |
| gauge.exchange.message_stats.publish_out_details.rate.md | gauge | definition |

#### Nodes

| metric name | type | definition | 
| ------------|------|------------|
| counter.node.io_read_bytes.md | counter | definition |
| counter.node.io_read_count.md | counter | definition |
| counter.node.mnesia_disk_tx_count.md | counter | definition |
| counter.node.mnesia_ram_tx_count.md | counter | definition |
| gauge.node.disk_free.md | gauge | definition |
| gauge.node.disk_free_details.rate.md | gauge | definition |
| gauge.node.disk_free_limit.md | gauge | definition |
| gauge.node.fd_total.md | gauge | definition |
| gauge.node.fd_used.md | gauge | definition |
| gauge.node.fd_used_details.rate.md | gauge | definition |
| gauge.node.io_read_avg_time.md | gauge | definition |
| gauge.node.io_read_avg_time_details.rate.md | gauge | definition |
| gauge.node.io_read_bytes_details.rate.md | gauge | definition |
| gauge.node.io_read_count_details.rate.md | gauge | definition |
| gauge.node.io_sync_avg_time.md | gauge | definition |
| gauge.node.io_sync_avg_time_details.rate.md | gauge | definition |
| gauge.node.io_write_avg_time.md | gauge | definition |
| gauge.node.io_write_avg_time_details.rate.md | gauge | definition |
| gauge.node.mem_limit.md | gauge | definition |
| gauge.node.mem_used.md | gauge | definition |
| gauge.node.mem_used_details.rate.md | gauge | definition |
| gauge.node.mnesia_disk_tx_count_details.rate.md | gauge | definition |
| gauge.node.mnesia_ram_tx_count_details.rate.md | gauge | definition |
| gauge.node.net_ticktime.md | gauge | definition |
| gauge.node.proc_total.md | gauge | definition |
| gauge.node.proc_used.md | gauge | definition |
| gauge.node.proc_used_details.rate.md | gauge | definition |
| gauge.node.processors.md | gauge | definition |
| gauge.node.run_queue.md | gauge | definition |
| gauge.node.sockets_total.md | gauge | definition |
| gauge.node.sockets_used.md | gauge | definition |
| gauge.node.sockets_used_details.rate.md | gauge | definition |
| gauge.node.uptime.md | gauge | definition |

#### Queues

| metric name | type | definition | 
| ------------|------|------------|
| counter.queue.disk_reads.md | counter | definition |
| counter.queue.disk_writes.md | counter | definition |
| counter.queue.message_stats.ack.md | counter | definition |
| counter.queue.message_stats.deliver.md | counter | definition |
| counter.queue.message_stats.deliver_get.md | counter | definition |
| counter.queue.message_stats.publish.md | counter | definition |
| gauge.queue.backing_queue_status.avg_ack_egress_rate.md | gauge | definition |
| gauge.queue.backing_queue_status.avg_ack_ingress_rate.md | gauge | definition |
| gauge.queue.backing_queue_status.avg_egress_rate.md | gauge | definition |
| gauge.queue.backing_queue_status.avg_ingress_rate.md | gauge | definition |
| gauge.queue.backing_queue_status.len.md | gauge | definition |
| gauge.queue.backing_queue_status.next_seq_id.md | gauge | definition |
| gauge.queue.backing_queue_status.q1.md | gauge | definition |
| gauge.queue.backing_queue_status.q2.md | gauge | definition |
| gauge.queue.backing_queue_status.q3.md | gauge | definition |
| gauge.queue.backing_queue_status.q4.md | gauge | definition |
| gauge.queue.consumer_utilisation.md | gauge | definition |
| gauge.queue.consumers.md | gauge | definition |
| gauge.queue.memory.md | gauge | definition |
| gauge.queue.message_bytes.md | gauge | definition |
| gauge.queue.message_bytes_persistent.md | gauge | definition |
| gauge.queue.message_bytes_ram.md | gauge | definition |
| gauge.queue.message_bytes_ready.md | gauge | definition |
| gauge.queue.message_bytes_unacknowledged.md | gauge | definition |
| gauge.queue.message_stats.ack_details.rate.md | gauge | definition |
| gauge.queue.message_stats.deliver_details.rate.md | gauge | definition |
| gauge.queue.message_stats.deliver_get_details.rate.md | gauge | definition |
| gauge.queue.message_stats.publish_details.rate.md | gauge | definition |
| gauge.queue.messages.md | gauge | definition |
| gauge.queue.messages_details.rate.md | gauge | definition |
| gauge.queue.messages_persistent.md | gauge | definition |
| gauge.queue.messages_ram.md | gauge | definition |
| gauge.queue.messages_ready.md | gauge | definition |
| gauge.queue.messages_ready_details.rate.md | gauge | definition |
| gauge.queue.messages_ready_ram.md | gauge | definition |
| gauge.queue.messages_unacknowledged.md | gauge | definition |
| gauge.queue.messages_unacknowledged_details.rate.md | gauge | definition |
| gauge.queue.messages_unacknowledged_ram.md | gauge | definition |

### LICENSE

> Include licensing information in this section.

This plugin is released under the Apache License v2.0. See `LICENSE.md` in this repository for details. 
