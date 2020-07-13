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


By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page.

#### RDS ENHANCED MONITORING

SignalFx supports an integration with <a target="_blank" href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html">RDS Enhanced Monitoring</a> using an AWS Lambda function, described below. This integration also includes built-in dashboards designed specifically for the metrics from Enhanced Monitoring. This Enhanced Monitoring integration complements the CloudWatch-based integration described above.  

You can choose to deploy the function either from the Serverless Application Repository (recommended) or from source. Choose a deployment method and follow the steps below to encrypt your SignalFx access token, customize the metrics that will be sent to SignalFx, and create and deploy the new function.

Before you begin, you must enable the Enhanced Monitoring option for the RDS instances you want to monitor using this integration. <a target="_blank" href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html">Click here for instructions on enabling Enhanced Monitoring</a>.

##### Note: Encryption of your SignalFx access token
This Lambda function uses your SignalFx access token to send metrics to SignalFx, as an environment variable to the function. While Lambda encrypts all environment variables at rest and decrypts them upon invocation, AWS recommends that all sensitive information such as access tokens be encrypted using a KMS key before function deployment, and decrypted at runtime within the code.

Both procedures below include instructions for using either an encrypted or non-encrypted access token.

- [Deploying through the Serverless Application Repository](#deploying-through-the-serverless-application-repository)
- [Building from source](#building-from-source)
- [Metrics collected by this integration](#metric-groups-collected-by-this-integration)

#### Deploying through the Serverless Application Repository

##### 1. Set up an encryption key and encrypt your access token (if desired)
Only follow this step if you chose to manually encrypt your access token. Either create a new KMS encryption key or select a preexisting one. **The key must be in the same availability zone as the RDS instances you are monitoring.** You can create and manage encryption keys from IAM in the AWS management console. Documentation on KMS encryption from the CLI can be found <a target="_blank" href="http://docs.aws.amazon.com/cli/latest/reference/kms/encrypt.html">here</a>. Make sure you have access to the cipher text output by the encryption as well as the key id of the encryption key you used.

##### 2. Create the Lambda function
Click `Create Function` from the list of Lambda functions in your AWS console. Make sure you are in the intended availability zone. Select the `Serverless Application Repository` option in the upper right hand corner. Search for `signalfx rds` and choose the appropriate entry based on whether you encrypted your access token.

To access the templates directly, find the template for encrypted access tokens <a target="_blank" href="https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-2:254067382080:applications~signalfx-enhanced-rds-metrics-encrypted">here</a>. The template for non-encrypted access tokens is <a target="_blank" href="https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-2:254067382080:applications~signalfx-enhanced-rds-metrics">here</a>.

##### 3. Fill out application parameters
Under `Configure application parameters`, choose a name for your function, and fill out the fields accordingly.

**Parameters for template using encrypted access tokens**
- `EncryptedSignalFxAuthToken`: The Ciphertext blob output from your encryption of your SignalFx organization's access token
- `KeyId`: The key id of your KMS encryption key; it is the last section of the key's ARN.
- `SelectedMetricGroups`: The metric groups you wish to send. Enter `All` if you want all available metrics. Otherwise, list the names of desired metric groups, spelled exactly as they are in [Metrics collected by this integration](#metric-groups-collected-by-this-integration), separated by single spaces.
- `Realm`: Your SignalFx Realm: YOUR_SIGNALFX_REALM. To determine what realm you are in, check your profile page in the SignalFx web application. Default: `us0`.

**Parameters for template using non-encrypted access tokens**
- `SignalFxAuthToken`: Your SignalFx organization's access token (YOUR_SIGNALFX_API_TOKEN)
- `SelectedMetricGroups`: The metric groups you wish to send. Enter `All` if you want all available metrics. Otherwise, list the names of desired metric groups, spelled exactly as they are in [Metrics collected by this integration](#metric-groups-collected-by-this-integration), separated by single spaces.
- `Realm`: Your SignalFx Realm: YOUR_SIGNALFX_REALM. To determine what realm you are in, check your profile page in the SignalFx web application. Default: `us0`.

#### A note on SignalFx realms:
A realm is a self-contained deployment of SignalFx in which your organization is hosted.
Different realms have different API endpoints.
For example, the endpoint for sending data in the us1 realm is ingest.us1.signalfx.com,
and the endpoint for the eu0 realm is ingest.eu0.signalfx.com. If you try to send data to the incorrect realm, your access token will be denied.


##### 4. Deploy function and configure trigger
Click `Deploy`. After the function has finished deploying, navigate to the function's main page.


By default, SignalFx imports all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page.

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

There are no CloudWatch recommended statistics for this integration.

#### METRICS

For more information about the metrics emitted by Amazon Relational Database Service, visit the RDS service homepage at <a target="_blank" href="https://aws.amazon.com/rds/">https://aws.amazon.com/rds/<a>.

#### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
