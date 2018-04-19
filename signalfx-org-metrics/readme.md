# SignalFx organization metrics


- [Description](#description)
- [Usage](#usage)
- [Metrics](#metrics)


### DESCRIPTION

SignalFx generates a number of metrics you can use to monitor your usage of SignalFx, including:

-  Ingest-related metrics that characterize the volume and nature of data that you are sending to SignalFx, such as the number of datapoints that were sent or how many metric time series were created in response to the datapoints and dimensions sent.

-  Usage or engagement metrics, such as the number of dashboards or charts in the organization.

-  Metrics that tell you how SignalFx pulls data on your behalf from cloud services like Amazon Web Services or Google Cloud Platform, such as the number of calls to each GCP Stackdriver client method or how many of the calls to the AWS CloudWatch API are being throttled by AWS.

Your organization is not charged for these metrics, and they do not count against any limits.


### USAGE

SignalFx admins can see some of these values in built-in charts on the Organization Overview page. And, like any other metrics, you can display them on charts you build to monitor your system health.


#### About ByToken metrics

Some metrics send both a total value and a ByToken value, such as `sf.org.numAddDatapointCalls` and `sf.org.numAddDatapointCallsByToken`.

The sum of all the ByToken values may be less than the value of the counterpart (non-token-based) metric; this is because no per-token value is sent for data that SignalFx retrieves on your behalf via AWS CloudWatch, GCP StackDriver, AppDynamics, or New Relic, as data sent from those integrations is not associated with a token. For example, if you sum the values sent for `sf.org.numAddDatapointCallsByToken`, the value may be less than the value of `sf.org.numAddDatapointCalls`, because the latter includes data from the specified integrations while the former does not.


#### About "per metric type" metrics

Some metrics send a value for each metric type (counter, cumulative counter or gauge), resulting in three MTS for these metrics. Each MTS is sent with a dimension named `category` with a value of `COUNTER`, `CUMULATIVE_COUNTER`, or `GAUGE`. Because you can have multiple MTS for these metrics, you would need to use the Sum analytics function to see the total value. 

For example, you might receive 3 MTS for `sf.org.numMetricTimeSeriesCreated`, one representing the number of MTS that are counters, another for the number of MTS that are cumulative counters, and a third for the number of MTS that are gauges. To find the total number of MTS created, you need to sum those values.

Also, you could filter by a single value of `category`, such as `GAUGE`, to see only the metrics of that type.

### METRICS

For documentation of the organization metrics and dimensions sent by SignalFx, [click here](./docs).

