---
title: Master Slave Shutdowns Scheduled
brief: Number of slaves which have failed their health check and are scheduled to be removed
metric_type: counter
---
### Master Slave Shutdowns Scheduled

Number of slaves which have failed their health check and are scheduled to be removed, on this master. They will not be immediately removed due to the Slave Removal Rate-Limit, but master/slave_shutdowns_completed will start increasing as they do get removed.