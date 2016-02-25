---
title: RabbitMQ Metrics
brief: Metrics collected from RabbitMQ 3.0.0 or above
---
### RabbitMQ Metrics

Use the [collectd-rabbitmq](https://github.com/signalfx/collectd-rabbitmq) collectd plugin to collect metrics about RabbitMQ. An example config file for collecting data about RabbitMQ using this plugin can be found in our [collectd configs repo](https://github.com/signalfx/signalfx-collectd-configs/blob/master/managed_config/10-rabbitmq.conf).

Use this plugin to monitor the following components of RabbitMQ:

* Channels
* Connections
* Exchanges
* Nodes
* Queues


### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| rabbitmq  | 3.0.0 or later |
