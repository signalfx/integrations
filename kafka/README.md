# ![](https://github.com/signalfx/integrations/blob/master/kafka/img/integrations_kafka.png) Kafka

#### FEATURES

##### Built-in dashboards

- **Broker**: Focus on a single Kafka broker.

- **Brokers**: Overview of data from all Kafka brokers. `cluster` dimension which is available in the SignalFx Agent can be used to get a per cluster view of Brokers.

- **Producer**: Focus on a single Java based Producer.

- **Producers**: Overview of Java based Producers.

- **Consumer**: Focus on a single Java based Consumer.

- **Consumers**: Overview of Java based Consumers.

- **JVM**: Focus on the java virtual machine performance on a single instance.


**Note**: Metrics from Java based Kafka consumers and producers are available by default only when using the SignalFx Agent.

### USAGE

Sample of built-in dashboard in SignalFx:

![](././img/dashboard_kafka.png)

### ADDITIONAL METRIC INFO

For a comprehensive list of metrics, other the ones available by default, see <a target="_blank" href="https://kafka.apache.org/documentation.html#monitoring">here</a>.

Note that the metrics prefixed by `kafka.consumer` and `kafka.producer` are available only via the `kafka_consumer` and `kafka_producer` monitors of SignalFx Agent. Also, if using the SignalFx Agent, metrics from Broker will be added with
a user provided `cluster` dimension.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
