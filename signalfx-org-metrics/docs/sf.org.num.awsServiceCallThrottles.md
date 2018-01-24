---
title: sf.org.num.awsServiceCallThrottles 
brief: Number of Amazon API calls throttled by Amazon
metric_type: gauge
---
### sf.org.num.awsServiceCallThrottles

Number of calls made to the Amazon API that are being throttled by AWS because you have exceeded your AWS API Call limits.

Dimension(s): `orgId`, `namespace` (AWS service, such as AWS/Cloudwatch), `method` (the API being called, such as `getMetricStatistics`)

Data Resolution: 5 seconds
