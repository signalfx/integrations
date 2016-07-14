# ![](./img/integration_awsebs.png) Amazon Elastic Block Store (EBS)

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Amazon Elastic Block Store (EBS) via [Amazon CloudWatch](../aws)<!-- sfx_link:aws -->. 

#### FEATURES

##### Built-in dashboards

- **EBS Volumes**: Overview of all data from EBS.
  
  [<img src='./img/dashboard_ebs_volumes.png' width=200px>](./img/dashboard_ebs_volumes.png)

- **EBS Volume**: Focus on a single EBS volume.
  
  [<img src='./img/dashboard_ebs_volume.png' width=200px>](./img/dashboard_ebs_volume.png)

### INSTALLATION

To access this integration, [connect to CloudWatch](../aws)<!-- sfx_link:aws --> on the SignalFx Integrations page. 

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page. 

### USAGE

#### Uniquely identifying EBS Volumes

SignalFx synthesizes a unique ID for each EBS volume in the dimension `AWSUniqueId`.

#### EBS metadata 

For EBS, SignalFx will scan every volume ID from your AWS account and pull out properties of the volume and any tags set on the volume.

| EBS Filter Name	| Custom Property	| Description |
|-----------------|-----------------|-------------|
| availability-zone	| aws_availability_zone |	The Availability Zone in which the volume was created |
| create-time	| aws_create_time |	The time stamp when the volume was created |
| encrypted	| aws_encrypted |	The encryption status of the volume |
| iops	| aws_iops |	The number of I/O operations per second (IOPS) that the volume supports |
| kms_key_id	| aws_kms_key_id |	The full ARN of the AWS customer master key used to protect the volume encryption key for the volume |
| size	| aws_size |	The size of the volume, in GiB |
| snapshot_id	| aws_snapshot_id |	The snapshot from which the volume was created |
| state	| aws_state |	The status of the volume |
| volume_id	| aws_volume_id |	The volume ID |
| volume_type	| aws_volume_type |	The Amazon EBS volume type |

### METRICS

For more information about the metrics emitted by Amazon Elastic Block Store, click here or visit the service's homepage at https://aws.amazon.com/ebs/.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
