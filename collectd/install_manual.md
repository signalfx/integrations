# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_collectd.png)Manual Install of SignalFx collectd agent

_Most customers should install and configure collectd using SignalFx’s shell script, which automates all the steps listed below. Find instructions here:[Install collectd using SignalFx's shell script](https://support.signalfx.com/hc/en-us/articles/205983375-Install-collectd-using-SignalFx-s-shell-script)_

SignalFx maintains packages of collectd for many widely-used versions of Linux. Use this procedure to prepare your environment, install the appropriate collectd package, and configure it to send metrics to SignalFx.

## Prerequisites

This procedure is intended for experienced Linux users. Text in `code font` indicates commands to be run in a terminal. 

To use this procedure, you must have administrator (sudo) privileges on a system running one of the following versions of Linux:

- [Debian 7 & 8](https://support.signalfx.com/hc/en-us/articles/205147119-Step-by-step-Install-collectd-using-SignalFx-packages#ubuntu)
- [Ubuntu 12.04, 14.04 & 15.04](https://support.signalfx.com/hc/en-us/articles/205147119-Step-by-step-Install-collectd-using-SignalFx-packages#ubuntu)
- [RHEL/Centos 6.x & 7.x](https://support.signalfx.com/hc/en-us/articles/205147119-Step-by-step-Install-collectd-using-SignalFx-packages#centos)
- [Amazon Linux 2014.09, 2015.03, & 2015.09](https://support.signalfx.com/hc/en-us/articles/205147119-Step-by-step-Install-collectd-using-SignalFx-packages#centos) 

## Ubuntu 12.04, 14.04, & 15.04 and Debian 7 & 8

This procedure directs apt-get to download collectd packages from SignalFx, then installs and configures collectd.

1. Update apt-get’s package lists.
 ```
 sudo apt-get update
 ```
1. Install libraries that will allow you to download SignalFx’s packages.

 _If you're using Ubuntu &lt; 14.04:_
 ```
 sudo apt-get install python-software-properties
 ```
 _If you're using Ubuntu &gt; 14.04 or 15.04:_
 ```
 sudo apt-get install software-properties-common
 ```
1. Add SignalFx’s collectd package to apt.
 ```
 sudo add-apt-repository ppa:signalfx/collectd-release
 ```
1. Update apt-get again to reference the new SignalFx package.
 ```
 sudo apt-get update
 ```
1. Install collectd.
 ```
 sudo apt-get install collectd
 ```
1. Download SignalFx’s configuration files for collectd to `/etc/collectd.d`.

 ```
 curl -s https://raw.githubusercontent.com/signalfx/signalfx-collectd-configs/master/collectd.conf -o /etc/collectd.conf  
 mkdir -p /etc/collectd.d/managed_config /etc/collectd.d/filtering_config  
 curl -s https://raw.githubusercontent.com/signalfx/signalfx-collectd-configs/master/managed_config/10-signalfx.conf -o /etc/collectd.d/managed_config/10-signalfx.conf  
 curl -s https://raw.githubusercontent.com/signalfx/signalfx-collectd-configs/master/managed_config/10-aggregation-cpu.conf -o /etc/collectd.d/managed_config/10-aggregation-cpu.conf  
 curl -s https://raw.githubusercontent.com/signalfx/signalfx-collectd-configs/master/managed_config/10-write_http.conf -o /etc/collectd.d/managed_config/10-write_http.conf  
 curl -s https://raw.githubusercontent.com/signalfx/signalfx-collectd-configs/master/filtering_config/filtering.conf -o /etc/collectd.d/filtering_config/filtering.conf
 ```

1. (Optional) If running in AWS, construct a unique ID for this instance using AWS metadata.

 This allows SignalFx to correlate metrics from AWS CloudWatch with metrics from collectd. [Click here to learn more.](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-dynamic-data-retrieval)
 ```
 # generate a unique amazon id for signalfx to correlate aws metrics with collectd metrics.

 AWS_UNIQUE_ID=$(curl -s --connect-timeout 1 http://169.254.169.254/latest/dynamic/instance-identity/document | jq -r '.instanceId + "_" + .accountId + "_" + .region')[ -n "$AWS_UNIQUE_ID" ] && AWS_VALUE="?sfxdim_AWSUniqueId=$AWS_UNIQUE_ID"
 ```
1. The configuration files downloaded in step 6 contain template fields. Replace them with actual values.

 In the commands given below, you must provide a value for &lt;YOUR_API_TOKEN&gt;. Find your API token on your [SignalFx profile page](https://app.signalfx.com/#/myprofile).
 ```
 perl -pi -e 's#%%%INGEST_HOST%%%#https://ingest.signalfx.com/v1/collectd#g'  /etc/collectd.d/managed_config/10-signalfx.conf /etc/collectd.d/managed_config/10-write_http.conf  
 perl -pi -e 's#%%%API_TOKEN%%%#&lt;YOUR_API_TOKEN&gt;#g'  /etc/collectd.d/managed_config/10-signalfx.conf /etc/collectd.d/managed_config/10-write_http.conf  
 perl -pi -e 's#%%%EXTRA_DIMS%%%##g'  /etc/collectd.d/managed_config/10-signalfx.conf /etc/collectd.d/managed_config/10-write_http.conf
 ```
1. Restart collectd.
 ```
 service collectd restart
 ```
1. Start viewing your data in SignalFx.

 With collectd installed and reporting to SignalFx, you'll be able to view your data in minutes. [Click here to start viewing important infrastructure data on the Hosts page](https://app.signalfx.com/#/hosts/). 

## RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09

This procedure directs yum to install collectd from an RPM that SignalFx provides.

1. Install wget.
 ```
 sudo yum install wget
 ```
1. Look up the URL of the SignalFx RPM for your operating system.

 This page lists URLs to current SignalFx RPMs: [SignalFx RPMs to install collectd](https://support.signalfx.com/hc/en-us/articles/205066479) 

 Locate the RPM for your operating system on the list, and copy its URL.

1. Use wget with the URL from step 2 to download the SignalFx RPM.

 Run the command below, replacing SIGNALFX_URL with the URL you retrieved in step 2.
 ```
 wget SIGNALFX_URL
 ```
1. Use yum to install the SignalFx RPM you just downloaded.

 Run the command below, replacing /path/to/SIGNALFX_RPM_FILENAME with the name and location of the file you downloaded in step 3. 
 ```
 sudo yum install /path/to/SIGNALFX_RPM_FILENAME
 ```
1. Install collectd and required plugins.
 ```
 sudo yum install collectd collectd-disk collectd-write_http
 ```
1. Download SignalFx’s configuration files for collectd to `/etc/collectd.d`.
 ```
 curl -s https://raw.githubusercontent.com/signalfx/signalfx-collectd-configs/master/collectd.conf -o /etc/collectd.conf  
 mkdir -p /etc/collectd.d/managed_config /etc/collectd.d/filtering_config  
 curl -s https://raw.githubusercontent.com/signalfx/signalfx-collectd-configs/master/managed_config/10-signalfx.conf -o /etc/collectd.d/managed_config/10-signalfx.conf  
 curl -s https://raw.githubusercontent.com/signalfx/signalfx-collectd-configs/master/managed_config/10-aggregation-cpu.conf -o /etc/collectd.d/managed_config/10-aggregation-cpu.conf  
 curl -s https://raw.githubusercontent.com/signalfx/signalfx-collectd-configs/master/managed_config/10-write_http.conf -o /etc/collectd.d/managed_config/10-write_http.conf  
 curl -s https://raw.githubusercontent.com/signalfx/signalfx-collectd-configs/master/filtering_config/filtering.conf -o /etc/collectd.d/filtering_config/filtering.conf
 ```
1. (Optional) If running in AWS, construct a unique ID for this instance using AWS metadata.

 This allows SignalFx to correlate metrics from AWS CloudWatch with metrics from collectd. [Click here to learn more.](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-dynamic-data-retrieval)
 ```
 # generate a unique amazon id for signalfx to correlate aws metrics with collectd metrics.

 AWS_UNIQUE_ID=$(curl -s --connect-timeout 1 http://169.254.169.254/latest/dynamic/instance-identity/document | jq -r '.instanceId + "_" + .accountId + "_" + .region')[ -n "$AWS_UNIQUE_ID" ] && AWS_VALUE="?sfxdim_AWSUniqueId=$AWS_UNIQUE_ID"
 ```
1. The configuration files downloaded in step 6 contain template fields. Replace them with actual values.

 In the commands given below, you must provide a value for &lt;YOUR_API_TOKEN&gt;. Find your API token on your [SignalFx profile page](https://app.signalfx.com/#/myprofile).
 ```
 perl -pi -e 's#%%%INGEST_HOST%%%#https://ingest.signalfx.com/v1/collectd#g'  /etc/collectd.d/managed_config/10-signalfx.conf /etc/collectd.d/managed_config/10-write_http.conf  
 perl -pi -e 's#%%%API_TOKEN%%%#&lt;YOUR_API_TOKEN&gt;#g'  /etc/collectd.d/managed_config/10-signalfx.conf /etc/collectd.d/managed_config/10-write_http.conf  
 perl -pi -e 's#%%%EXTRA_DIMS%%%##g'  /etc/collectd.d/managed_config/10-signalfx.conf /etc/collectd.d/managed_config/10-write_http.conf
 ```
1. Restart collectd.
 ```
 service collectd restart
 ```
1. Start viewing your data in SignalFx.

 With collectd installed and reporting to SignalFx, you'll be able to view your data in minutes. [Click here to start viewing important infrastructure data on the Hosts page](https://app.signalfx.com/#/hosts/). 
