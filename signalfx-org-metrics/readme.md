# SignalFx organization metrics


- [Description](#description)
- [Usage](#usage)
- [Metrics](#metrics)


### DESCRIPTION

SignalFx generates a number of metrics you can use to monitor the status of your organization, including:

-  Ingest-related metrics, such as the number of active and inactive time series or how many datapoints were sent using a backfill API.

-  Organization status metrics, such as the number of unique metrics across all metric or event time series or the number of dashboards or charts in the organization

-  Metrics related to AWS and GCP, such as `sf.org.num.awsServiceCallCount` (number of calls made to the Amazon API) and `sf.org.num.gcpStackdriverClientCallCount` (number of calls to each Stackdriver client method).


### USAGE

SignalFx admins can see some of these values in built-in charts on the Organization Overview page. And, like any other metrics, you can display them on charts you build to monitor your system health.


#### About ByToken metrics

Some metrics send both a total value and a ByToken value (such as `sf.org.numAddDatapointCalls` and `sf.org.numAddDatapointCallsByToken`).The sum of all the ByToken values may be less than the value of the counterpart (non-token-based) metric; this is because no per-token value is sent for data that SignalFx retrieves on your behalf from integrations such as AWS, Google Cloud Platform (StackDriver), or New Relic, as data sent from those integrations is not associated with a token. 

For example, if you sum the values sent for `sf.org.numAddDatapointCallsByToken`, the value may be less than the value of `sf.org.numAddDatapointCalls`, because the latter includes data from the specified integrations while the former does not.

Conversely, the total number of MTS shown for a ByToken metric can be higher than its non-token counterpart. For example, if you have 10 unique MTS and 2 tokens, you could have  20 MTS for the ByToken metric (10 MTS per token). 

#### About "per metric type" metrics

Some metrics send a value for each metric type. That is, you can have up to three MTS for these metrics; each MTS is sent with a dimension named  `category` with a value of Counter, Cumulative Counter, or Gauge. Because you can have multiple MTS for these metrics, you would need to use the Sum analytics function to see the total value. 

For example, you might receive 3 MTS for `sf.org.numMetricTimeSeriesCreated`, one representing the number of MTS that are counters, another for the number of MTS that are cumulative counters, and a third for the number of MTS that are gauges. To find the total number of MTS created, you need to sum those values.

Also, you could filter by a category, such as Gauge, to see all metrics of that type.

### METRICS

For documentation of the organization metrics and dimensions sent by SignalFx, [click here](./docs).

