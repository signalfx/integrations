# ![](./img/integration_aws.png) Google Cloud Platform

- [Description](#description)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Google Cloud Platform (GCP) services via StackDriver
Monitoring. This integration enables data collection from all GCP web services
that report to StackDriver.

#### FEATURES

Connecting to GCP allows you to take advantage of SignalFx’s extensive GCP support.

- The SignalFx Infrastructure page visualizes GCP Compute instances.

  [<img src='./img/hosts_aws.png' width=200px>](./img/hosts_aws.png)
- SignalFx can sync metadata about your GCP hosts to enrich metrics reported by
    StackDriver or the [SignalFx collectd
    agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd).
- SignalFx provides built-in dashboards for many GCP services that report to
    StackDriver, such as [Firebase](https://fixme.com)[](sfx_link:gcp-firebase)
    and [Datastore](https://fixme.com)[](sfx_link:gcp-datastore).



### CONFIGURATION

Connect to GCP on the Integrations page in SignalFx.

To connect SignalFx to GCP, simply add our GCP user to your IAM member list for
the projects you want to integrate with SignalFx.  The email of our user is
`gcp@signalfx.com`.  It needs the following IAM roles in your projects:

- Project Viewer

You must be an administrator of your SignalFx account to connect SignalFx to
CloudWatch. [Click here for detailed
instructions](http://docs.signalfx.com/en/latest/getting-started/send-data.html#gcp).

### USAGE

#### Data available from GCP

##### Importing CloudWatch metrics and dimensions

SignalFx can sync CloudWatch metrics from AWS into SignalFx. By default, AWS CloudWatch metric data is sent in 5-minute periods. If you are using Detailed Monitoring on an AWS service, you can change the interval for syncing data from CloudWatch to SignalFx in 1-minute periods.

To enable CloudWatch metrics to be sent to SignalFx, make sure the “Import CloudWatch” checkbox is checked. SignalFx syncs all CloudWatch metrics data for all services and all regions in use in a given AWS account, but this can be filtered down by clicking on the “All Services” link and selecting the desired services, or by clicking on the “All Regions” link and selecting the desired regions.

SignalFx automatically imports relevant dimensions for each CloudWatch metric. For example, if you are using Detailed Monitoring for EC2 instances, SignalFx imports the dimensions AutoScalingGroupName, ImageId, InstanceId and InstanceType. These dimensions can be used to filter EC2 instance data.

##### Importing account metadata and custom tags

SignalFx can apply or sync other AWS metadata with metrics reported, allowing it to be used as filters or in group-bys when visualizing metrics. Metadata is available for [EC2](https://github.com/signalfx/integrations/tree/master/aws-ec2)[](sfx_link:aws-ec2), [EBS](https://github.com/signalfx/integrations/tree/master/aws-ebs)[](sfx_link:aws-ebs) and [ELB](https://github.com/signalfx/integrations/tree/master/aws-elb)[](sfx_link:aws-elb) services. It may take up to 15 minutes for metadata to be synced to your SignalFx data.

The following metadata is available for filtering metrics:

| Custom Property	| Description |
|-----------------|-------------|
| `aws_account_alias` | AWS account alias that the instance, volume or load balancer is running under |
| `aws_account_id` | AWS account ID that the instance, volume or load balancer is running under |
| `aws_tag_[Name of tag]` | Custom tags applied to the instance, volume or load balancer (e.g., aws\_tag\_Name)|

Account alias and ID can be useful because SignalFx allows you to import metrics from more than one AWS account. To distinguish between metrics from different accounts, the account alias and account ID are added as properties to the relevant metric time series.

SignalFx also syncs AWS tags and makes them available as properties on metrics associated with the relevant resources with the key `aws_tag_[Name of tag]`.

#### Using CloudWatch data

##### Recognizing CloudWatch statistics in SignalFx

Much like SignalFx, AWS CloudWatch uses rollups to summarize metrics, and it refers to them as “statistics”. However, because there is not a one-for-one mapping to SignalFx’s data model, the CloudWatch rollups are not directly accessible through the rollup selection menu in the chart builder. Instead, they are captured as individual time series through the use of the dimension `stat`.

| AWS Statistic	| SignalFx dimension |	Definition |
|---------------|--------------------|-------------|
| Average	| stat:mean	| Mean value of metric over the sampling period |
| Maximum	| stat:upper	| Maximum value of metric over the sampling period |
| Minimum	| stat:lower	| Minimum value of metric over the sampling period |
| Data Samples	| stat:count	| Number of samples over the sampling period |
| Sum	| stat:sum	| Sum of all values that occurred over the sampling period |

To use a CloudWatch metric in a plot, you must always specify the metric name along with a filter for `stat` that is appropriate to the metric you have chosen. For example, if you are using the metric `NetworkPacketsIn`, per the AWS CloudWatch documentation for EC2 metrics, the only statistics that are meaningful are Minimum, Maximum and Average, so you should choose the dimension stat with a value of either `lower`, `upper` or `mean`, respectively, depending on which statistic you want to use.

When syncing data from CloudWatch to SignalFx a 60-second sampling period is used. See [CloudWatch documentation](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html) for more detailed information.

##### AWS namespaces

SignalFx imports the namespace for AWS services using the dimension `namespace`. For most services, the namespaces take the format of “AWS/<name_of_service>”, e.g. “AWS/EC2” or “AWS/ELB”. This distinction is important when you want to use metrics that have the same name across services, such as `CPUUtilization`, but only for one service (say, EC2 and not ECS).

##### Uniquely identifying AWS instances

Amazon services that report to CloudWatch do not always provide unique identifiers. For example, the EC2 dimension `InstanceID` is not guaranteed to be unique across all availability zones. SignalFx synthesizes unique identifiers for [EC2](https://github.com/signalfx/integrations/tree/master/aws-ec2)[](sfx_link:aws-ec2), [EBS](https://github.com/signalfx/integrations/tree/master/aws-ebs)[](sfx_link:aws-ebs) and [ELB](https://github.com/signalfx/integrations/tree/master/aws-elb)[](sfx_link:aws-elb) instances, in the dimension called `AWSUniqueId`. This allows us to attach metadata to CloudWatch metrics from these services.

### METRICS

For more information about the metrics emitted by GCP StackDriver, see the documentation for individual services.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
