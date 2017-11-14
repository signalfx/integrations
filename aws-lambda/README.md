# ![](./img/integration_awslambda.png) Amazon Lambda

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Lambda via [Amazon CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

#### FEATURES

##### Built-in dashboards

- **Lambda Overview Cloudwatch**: Overview of all data from Lambda via CloudWatch.

  [<img src='./img/dashboard_lambda_overview_cloudwatch.png' width=200px>](./img/dashboard_lambda_overview_cloudwatch.png)

- **Lambda Overview SignalFx Wrapper**: Overview of all data from Lambda via SignalFx Wrapper.

  [<img src='./img/dashboard_lambda_overview_cloudwatch.png' width=200px>](./img/dashboard_lambda_overview_wrapper.png)
  
- **Lambda Instance Cloudwatch**: Instance view for specific Lambda function via CloudWatch.

  [<img src='./img/dashboard_lambda_instance_cloudwatch.png' width=200px>](./img/dashboard_lambda_instance_cloudwatch.png)
  
- **Lambda Instance Cloudwatch**: Instance view for specific Lambda function via SignalFx Wrapper.

  [<img src='./img/dashboard_lambda_instance_wrapper.png' width=200px>](./img/dashboard_lambda_instance_wrapper.png)

### INSTALLATION

SignalFx provides two methods of monitoring Lambda metrics. SignalFx Wrapper provides real-time invocations, errors and cold starts while CloudWatch provides an accurate durations. 

#### SignalFx Wrapper

SignalFx Wrapper provides real time monitoring of lambda functions as well as ability to send custom metric from your applications to SignalFx.

To use SignalFx Wrapper, include SignalFx Lambda Wrapper in the your Lambda function.

Instructions are provided in each of the Lambda wrapper.

- [Java](https://github.com/signalfx/lambda-java)
- [Python](https://github.com/signalfx/lambda-nodejs)
- [NodeJs](https://github.com/signalfx/lambda-python)

#### CloudWatch

To access this integration, [connect to CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page.

### USAGE

#### Uniquely identifying Lambda

##### SignalFx Wrapper

SignalFx uses a unique ARN (Amazon Resource Names) of the function instance in the dimension `lambda_arn`.

##### CloudWatch

SignalFx synthesizes a unique ID for each Lambda function instance in the dimension `AWSUniqueId`.

### METRICS

#### SignalFx Wrapper

The SignalFx Lambda wrapper sends the following metrics to SignalFx:

| Metric Name  | Type | Description |
| ------------- | ------------- | ---|
| function.invocations  | Counter  | Count number of Lambda invocations|
| function.cold_starts  | Counter  | Count number of cold starts|
| function.errors  | Counter  | Count number of errors from underlying Lambda handler|
| function.duration  | Gauge  | Milliseconds in execution time of underlying Lambda handler|

The Lambda wrapper adds the following dimensions to all data points sent to SignalFx:

| Dimension | Description |
| ------------- | ---|
| lambda_arn  | ARN of the Lambda function instance |
| aws_region  | AWS Region  |
| aws_account_id | AWS Account ID  |
| aws_function_name  | AWS Function Name |
| aws_function_version  | AWS Function Version |
| aws_function_qualifier  | AWS Function Version Qualifier (version or version alias if it is not an event source mapping Lambda invocation) |
| event_source_mappings  | AWS Function Name (if it is an event source mapping Lambda invocation) |
| aws_execution_env  | AWS execution environment (e.g. AWS_Lambda_nodejs6.10) |
| function_wrapper_version  | SignalFx function wrapper qualifier (e.g. signalfx-lambda-0.0.9) |
| metric_source | The literal value of 'lambda_wrapper' |

#### CloudWatch

For more information about the metrics emitted by Lambda, visit the service's homepage at https://aws.amazon.com/lambda/.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
