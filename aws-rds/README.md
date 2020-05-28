# ![](./img/integration_awsrds.png) Amazon Relational Database Service (RDS)

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [Recommended Statistics](#recommended-statistics)
- [License](#license)

## DESCRIPTION

Use SignalFx to monitor Amazon Relational Database Service (RDS) via [Amazon Web Services](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

## FEATURES

### Built-in dashboards

- **RDS Instances**: Overview of all data from RDS.

  [<img src='./img/dashboard_rds_instances.png' width=200px>](./img/dashboard_rds_instances.png)

- **RDS Instance**: Focus on a single RDS instance.

  [<img src='./img/dashboard_rds_instance.png' width=200px>](./img/dashboard_rds_instance.png)

## INSTALLATION

### Step 1: Connect to CloudWatch

Before you can integrate with RDS, you must connect to CloudWatch.

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page.

To complete this task, access the AWS tile, and review the listed instructions to [connect to CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

### Step 2: Deploy the Lambda function for Enhanced Monitoring

SignalFx supports an integration with RDS Enhanced Monitoring using an AWS Lambda function.

There are two ways to deploy the Lambda function:

- Option 1: Deploy from the Serverless Application Repository
    - SignalFx recommends this option.

- Option 2: Deploy (building) from the source

To learn how to deploy the Lambda function for Enhanced Monitoring, see <a target="_blank" href="https://github.com/signalfx/enhanced-rds-monitoring">SignalFx Enhanced RDS Monitoring Integration</a>.


## USAGE

SignalFx provides built-in dashboards for this service. Examples are shown below.

![](./img/dashboard_rds_instances.png)

![](./img/dashboard_rds_instance.png)


<!--- METRICS --->
### RECOMMENDED STATISTICS

No CloudWatch recommended statistics for this integration.

#### METRICS

For more information about the metrics emitted by Amazon Relational Database Service, visit the service's homepage at <a target="_blank" href="https://aws.amazon.com/rds/">https://aws.amazon.com/rds/<a>.

#### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
