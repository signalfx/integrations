---
title: sf.org.numAddDatapointCallsByToken
brief: Per token number of calls to send in metrics
metric_type: counter
---
### sf.org.numAddDatapointCallsByToken

This metric shows the number of calls to ingest used by each token to send in metrics.

Dimension(s): `orgId, tokenId`
Resolution: 1 second

Note that the sum of all the `sf.org.numAddDatapointCallsByToken` values may be less than the value of `sf.org.numAddDatapointCalls`. For an explanation, see [About ByToken metrics](./readme.md#bytoken).
