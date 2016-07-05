---
title: Error response
brief: Corresponds to haproxy's eresp metric. Response errors. srv_abrt will be counted here also. Responses denied because of security concerns.
metric_type: derive
---
### Error response

Corresponds to haproxy's eresp metric. Response errors. srv_abrt will be counted here also.
     Some other errors are:
     - write error on the client socket (won't be counted for the server stat)
     - failure applying filters to the response.
