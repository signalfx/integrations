# ![](./img/integration_awsec2.png) Amazon Elastic Compute Cloud (EC2)

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Amazon Elastic Compute Cloud (EC2) via [Amazon CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws). 

#### FEATURES

##### Infrastructure Page

- **Infrastructure Navigator**: On the Infrastructure page in SignalFx, the Infrastructure Navigator visualizes EC2 instances as squares, colored by CloudWatch metrics including CPU, disk, and network. Group and filter instances by AWS metadata like availability zone or service tag in order to discover trends and correlations. [Click here to read more about the Infrastructure Page](http://docs.signalfx.com/en/latest/built-in-content/infra-nav.html). 

  [<img src='./img/hosts_aws_instances.png' width=200px>](./img/hosts_aws_instances.png)

##### Built-in dashboards

- **EC2 Instances**: Overview of all data from EC2.
  
  [<img src='./img/dashboard_ec2_instances.png' width=200px>](./img/dashboard_ec2_instances.png)

- **EC2 Instance**: Focus on a single EC2 instance.
  
  [<img src='./img/dashboard_ec2_instance.png' width=200px>](./img/dashboard_ec2_instance.png)

### INSTALLATION

To access this integration, [connect to CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws) on the SignalFx Integrations page. 

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page. 

### USAGE

#### Uniquely identifying EC2 instances

EC2 instance IDs are not guaranteed to be unique. To uniquely identify an EC2 instance, SignalFx concatenates instanceId, AWS region, and AWS account ID separated by underscore in the dimension `AWSUniqueId`, as follows:

    instanceId_region_accountID

#### EC2 metadata

For EC2, SignalFx will scan every instance ID from your AWS account and pull out properties of the instance and any tags set on the instance.  Any dimension called “Host” or “InstanceId” in SignalFx that matches the instance ID’s value, private DNS name, or private IP address will now have the same tags and properties of the instance ID.  Each instance property is prefixed with “aws_”.

| EC2 Filter Name	| Custom Property	| Description |
|-----------------|-----------------|-------------|
| architecture	| aws_architecture	| Instance architecture (i386 or x86_64) |
| availability-zone	| aws_availability_zone	| The availability zone of the instance |
| dns-name	| aws_public_dns_name	| Public DNS name of the instance |
| hypervisor	| aws_hypervisor	| Hypervisor type of the instance (ovm or xen)  |
| image-id	| aws_image_id	| ID of the image used to launch the instance |
| instance-id	| aws_instance_id	| ID of the instance |
| instance-state-name	| aws_state	| An object defining the state code and name of the instance |
| instance-type	| aws_instance_type	| Type of the instance |
| ip-address	| aws_public_ip_address	| The address of the Elastic IP address bound to the network interface |
| kernel-id	| aws_kernel_id	| Kernel ID |
| launch-time	| aws_launch_time	| The time when the instance was launched |
| private-dns-name	| aws_private_dns_name	| Private DNS name of the instance |
| reason	| aws_state_reason	| The state reason for the instance (if provided) |
| region	| aws_region	| The region which the instance is running in |
| reservation-id	| aws_reservation_id	| ID of the instance’s reservation |
| root-device-type	| aws_root_device_type	| Type of root device that the instance uses |

For more information about the filters, see http://docs.aws.amazon.com/AWSEC2/latest/CommandLineReference/ApiReference-cmd-DescribeInstances.html.

### METRICS

For more information about the metrics emitted by Amazon EC2, click here or visit the service's homepage at https://aws.amazon.com/ec2/.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
