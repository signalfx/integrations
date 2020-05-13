# ![](./img/integration_awsalb.png) Amazon Application Load Balancing (ALB)

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [Recommended Statistics](#recommended-statistics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Application Load Balancing (ALB) via [Amazon Web Services](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

### FEATURES

##### Built-in dashboards

- **ApplicationELB Instances**: Overview of all data from ALB.

  [<img src='./img/dashboard_alb_instances.png' width=200px>](./img/dashboard_alb_instances.png)

- **ApplicationELB Instance**: Focus on a single ALB load balancer.

  [<img src='./img/dashboard_alb_instance.png' width=200px>](./img/dashboard_alb_instance.png)

### INSTALLATION

To access this integration, [connect to CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page.

### USAGE

#### Uniquely identifying ALBs

SignalFx synthesizes a unique ID for each ALB in the dimension `AWSUniqueId`.

#### METRICS

For more information about the metrics emitted by Application Load Balancing, visit the service's homepage at <a target="_blank" href="https://aws.amazon.com/elasticloadbalancing/">https://aws.amazon.com/elasticloadbalancing/</a>.

<!--- METRICS --->
### RECOMMENDED STATISTICS

The following are a subset of available metrics; these statistics are recommended by Amazon for collection.

_Load balancer metrics_

| Metric                                 | Recommended Statistics |
| -------------------------------------- | ---------------------- |
| ActiveConnectionCount                  | Sum                    |
| ClientTLSNegotiationErrorCount         | Sum                    |
| ConsumedCUs                            | Average, Sum           |
| HTTP_Fixed_Response_Count              | Sum                    |
| HTTP_Redirect_Count                    | Sum                    |
| HTTP_Redirect_Url_Limit_Exceeded_Count | Sum                    |
| HTTPCode_ELB_3XX_Count                 | Sum                    |
| HTTPCode_ELB_4XX_Count                 | Sum                    |
| HTTPCode_ELB_5XX_Count                 | Sum                    |
| IPv6ProcessedBytes                     | Sum                    |
| IPv6RequestCount                       | Sum                    |
| NewConnectionCount                     | Sum                    |
| ProcessedBytes                         | Sum                    |
| RejectedConnectionCount                | Sum                    |
| RequestCount                           | Sum                    |
| RuleEvaluations                        | Sum                    |
| StandardProcessedBytes                 | Sum                    |



_ALB metrics for targets_

| Metric                         | Recommended Statistics    |
| ------------------------------ | ------------------------- |
| HealthyHostCount               | Average, Minimum, Maximum |
| HTTPCode_Target_2XX_Count      | Sum                       |
| HTTPCode_Target_3XX_Count      | Sum                       |
| HTTPCode_Target_4XX_Count      | Sum                       |
| HTTPCode_Target_5XX_Count      | Sum                       |
| NonStickyRequestCount          | Sum                       |
| RequestCountPerTarget          | Sum                       |
| TargetConnectionErrorCount     | Sum                       |
| TargetResponseTime             | Average, Percentile       |
| TargetTLSNegotiationErrorCount | Sum                       |
| UnHealthyHostCount             | Average, Minimum, Maximum |



_ALB metrics for Lambda targets_

| Metrics                    | Recommended Statistics |
| -------------------------- | ---------------------- |
| LambdaInternalError        | Sum                    |
| LambdaTargetProcessedBytes | Sum                    |
| LambdaUserError            | Sum                    |



_ELB user authentication metrics_

| Metrics                       | Recommended Statistics |
| ----------------------------- | ---------------------- |
| ELBAuthError                  | Sum                    |
| ELBAuthFailure                | Sum                    |
| ELBAuthLatency                | Sum                    |
| ELBAuthRefreshTokenSuccess    | Sum                    |
| ELBAuthSuccess                | Sum                    |
| ELBAuthUserClaimsSizeExceeded | Sum                    |




#### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
