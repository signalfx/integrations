# ![](./img/integration_awslambda.png) Amazon Lambda

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

If you have enabled the SignalFx Amazon Web Services integration and are syncing Cloudwatch metrics, metrics related to Lambda functions will automatically be available to view, as shown in [Importing Lambda Metadata](https://docs.signalfx.com/en/latest/integrations/aws-info.html#lambda-metadata).

You can use one of our wrappers (discussed below) to monitor your functions. If you use a wrapper, in addition to viewing the standard metrics our wrappers make available, you can send in custom metrics to monitor apps running inside the Lambda.

#### FEATURES

##### Built-in dashboards

- **Lambda (AWS) Overview**: Overview of all data from Lambda via CloudWatch.

  [<img src='./img/lambda-aws-overview-db.png' width=200px>](./img/lambda-aws-overview-db.png)

- **Lambda (SignalFx) Overview**: Overview of all data from Lambda via SignalFx Wrapper.

  [<img src='./img/lambda-sfx-overview-db.png' width=200px>](./img/lambda-sfx-overview-db.png)
  
- **Lambda (AWS) Function**: Instance view for specific Lambda function via CloudWatch.

  [<img src='./img/lambda-aws-function-db.png' width=200px>](./img/lambda-aws-function-db.png)
  
- **Lambda (SignalFx) Function**: Instance view for specific Lambda function via SignalFx Wrapper.

  [<img src='./img/lambda-sfx-function-db.png' width=200px>](./img/lambda-sfx-function-db.png)

### INSTALLATION 

#### SignalFx Wrapper

SignalFx Wrapper provides real time monitoring of lambda functions as well as ability to send custom metric from your applications to SignalFx.

To use SignalFx Wrapper, include SignalFx Lambda Wrapper in your Lambda function.

Instructions are provided in each of the Lambda wrapper.

- [Java](https://github.com/signalfx/lambda-java)
- [NodeJs](https://github.com/signalfx/lambda-nodejs)
- [Python](https://github.com/signalfx/lambda-python)

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
| function.invocations  | Counter  | Count of Lambda invocations|
| function.cold_starts  | Counter  | Count of cold starts|
| function.errors  | Counter  | Count of errors from underlying Lambda handler|
| function.duration  | Gauge  | Milliseconds in execution time of underlying Lambda handler|

The Lambda wrappers add several dimensions to data points sent to SignalFx. These dimensions can be used for filtering and aggregation.

| Dimension | Description |
| ------------- | ---|
| lambda_arn  | Amazon Resource Name (ARN) of the Lambda function instance |
| aws_region  | AWS Region where the Lambda function is executed  |
| aws_account_id | AWS Account ID associated with the Lambda function  |
| aws_function_name  | Name of the Lambda function |
| aws_function_version  | Version if the Lambda function |
| aws_function_qualifier  | AWS Function Version Qualifier (version or version alias if it is not an event source mapping Lambda invocation) |
| event_source_mappings  | AWS Function Name (if it is an event source mapping Lambda invocation) |
| aws_execution_env  | AWS execution environment (e.g. AWS_Lambda_nodejs6.10) |
| function_wrapper_version  | SignalFx function wrapper qualifier (e.g. signalfx-lambda-0.0.9) |
| metric_source | The literal value of 'lambda_wrapper' |

#### CloudWatch

For more information about the metrics emitted by Lambda, see the documentation at https://docs.signalfx.com/en/latest/integrations/aws-info.html#lambda-metadata.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
