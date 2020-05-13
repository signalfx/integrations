# ![](./img/integration_awsapigateway.png) Amazon API Gateway

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [Recommended Statistics](#Recommended-statistics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Amazon API Gateway via [Amazon Web Services](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

### FEATURES

##### Built-in dashboards

- **Overview**: Overview of CloudWatch data of the number of API calls, average latency and error responses for all API resources.
  [<img src='./img/dashboard-awsapigateway-overview.png' width=200px>](./img/dashboard-awsapigateway-overview.png)

- **API Resource**: CloudWatch data of the number of API calls, average latency, error responses and cache hit/miss filtered for individual API resources.
  [<img src='./img/dashboard-awsapigateway-apiresource.png' width=200px>](./img/dashboard-awsapigateway-apiresource.png)

### INSTALLATION

#### Step 1: Connect to CloudWatch

To access this integration, [connect to CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

#### Step 2: Enable CloudWatch metrics

Enable detailed CloudWatch metrics for your API stage in AWS.

1. In your Amazon API Gateway console, click the name of your API.
2. Click **Stages**.
3. Click on your stage.
4. Click **Logs/Tracing**, specify **Enable Detailed CloudWatch Metrics**, and then click **Save Changes**.

#### Step 3: Set up CloudWatch API logging

To set up CloudWatch API logging, add the ARN for the IAM role that has write access to CloudWatch logs.

To do this, visit AWS's documentation site, and see [Set up CloudWatch API logging using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html).


### USAGE

SignalFx provides built-in dashboards for this service. Examples are shown below.

![](./img/dashboard-awsapigateway-overview.png)

![](./img/dashboard-awsapigateway-apiresource.png)

#### METRICS

For more information about the metrics emitted by Amazon API Gateway, visit the service's homepage at <a target="_blank" href="https://aws.amazon.com/api-gateway/">https://aws.amazon.com/api-gateway/</a>.

<!--- METRICS --->
### RECOMMENDED STATISTICS

The following is a subset of all available statistics; these are recommended for monitoring by Amazon.

| Metric            | Recommended Statistics                |
| ----------------- | ------------------------------------- |
| 4XXError          | Count, Average                        |
| 5XXError          | Count, Average                        |
| CacheHitCount     | Sum, Average                          |
| CacheMissCount    | Sum, Average                          |
| Count             | Count                                 |
| IntegrationLegacy | Average, Count, Minimum, Maximum, Sum |
| Latency           | Average, Count, Minimum, Maximum, Sum |


#### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
