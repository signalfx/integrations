# ![](./img/integration_awsrds.png) Amazon Relational Database Service (RDS)

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Amazon Relational Database Service (RDS) via [Amazon CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws). 

#### FEATURES

##### Built-in dashboards

- **RDS Instances**: Overview of all data from RDS.
  
  [<img src='./img/dashboard_rds_instances.png' width=200px>](./img/dashboard_rds_instances.png)

- **RDS Instance**: Focus on a single RDS instance.
  
  [<img src='./img/dashboard_rds_instance.png' width=200px>](./img/dashboard_rds_instance.png)

### INSTALLATION

To access this integration, [connect to CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws) on the SignalFx Integrations page. 

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page. 

### USAGE

SignalFx provides built-in dashboards for this service. Examples are shown below. 

![](./img/dashboard_rds_instances.png)

![](./img/dashboard_rds_instance.png)

### METRICS

For more information about the metrics emitted by Amazon Relational Database Service, visit the service's homepage at https://aws.amazon.com/rds/.

### ENHANCED MONITORING

SignalFx now offers a Lambda-based integration of enhanced monitoring from RDS.
This integration can be used regardless of whether the standard RDS integration
is in use. Set up only requires a bit of configuration on AWS to start sending
enhanced metrics to SignalFx at the desired granularity.

#### Enable Enhanced Monitoring

Enhanced monitoring must be enabled on each RDS instance for them to report
metrics. This can be done from the RDS dashboard by selecting Modify under the
dropdown of instance actions. The Enable Enhanced Monitoring section is towards
the bottom. After selecting Yes, you will have options for which monitoring
role to use, as well as the resolution of your data points. If there is no role
available on the dropdown you can allow one to be created for you by selecting
a checkbox, or reuse a preexisting one. Each instance will take a few minutes
to change its configuration, after which the metrics will be sent to a
CloudWatch Logs stream.

#### Create an Encryption Key

Creating an Encryption Key allows you to keep your SignalFx access token
encrypted in the configuration of the Lambda function. To create a new one, go
to the Encryption Keys tab on the IAM Management Console. Make sure to add the
users who will need to have access to the Lambda function, as well as
appropriate admins.

#### Create the Lambda function

##### Select the blueprint

A new Lambda can be created from the Functions page of the Lambda Management
Console. Filter the available blueprints by **signalfx**, and select *insert
blueprint name here*.

##### Set up the trigger

The next step is to configure the function trigger, which will be CloudWatch
Logs. The metrics are automatically directed through the RDSOSMetrics log
group (which will only be available if Enhanced Monitoring is already enabled).
The only other required field is the Filter Name; it doesn't matter what name
you choose.

##### Configuration

The name of the function itself will be how it appears on the list in the
Management Console, so pick whatever makes sense. Don't touch the runtime;
leave it as Python 2.7.

You will want to create 1 or 2 environment variables. The access token for the
SignalFx org is required so that the metrics can be sent to your account. The
key should be `access_token`, and the value should be the org access token.
This is where the encryption key comes in. Select the checkbox labeled **Enable
encryption helpers**, and select the key created for this purpose from the
dropdown that appears. Once this is done, an Encrypt button should have
appeared next to the environment variable you just created. Click it, and your
token will be encrypted (you only need to do this once).

Another environment variable is only necessary if you are certain that you only
want a subset of the available metrics. The full list can be found
[here](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html).
You can either provide the names of the metric groups that you want included or
the groups you want excluded. If you create both lists, only the 'include' list
will be used. The list should simply be the names of the groups, spelled
exactly as they are in the documentation (including capitals) separated by a
single space. The key for this environment variable should be either `groups`
for the inclusive group or `groups_out` for the exclusive group.

The only other step is to create the execution role. The easiest way forward
here is to select **Create new role from template(s)** from the Role dropdown.
Choose a good name for the role, then check to see that `KMS decryption
permissions` already appears at the bottom. If it doesn't you can select it
from the **Policy templates** dropdown. Since that is the only permission
needed, you're all set! All that's left is to review the settings for the
function, create it, and enable the trigger (unless you selected to enable the
trigger during that step of setup). This can be done from the Triggers tab on
the function dashboard. Once you do, your metrics will be sent to SignalFx!

  
### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
