# ![](https://github.com/signalfx/integrations/blob/master/haproxy/img/integrations_haproxy.png) HAProxy

Metadata associated with the HAProxy collectd plugin can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/haproxy">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd-haproxy">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### USAGE
#### Default metrics
- **HAProxy Overview**
    - Connection Rate - Total number of connections per second being made.
    - Requests per Second - Number of incoming requests per second.
    - Idle Percent - HAProxy runs on an event loop and waits for new events using poll(). Idle_pct is the ratio of polling time versus total time. Near 100% means load is low, near 0% means the load is very high.
    - Current Sessions - Current number of active sessions in the system. A session is an end-to-end connection.
    - Sessions Rate - Chart showing the rate at which sessions are being created.
    - Top Servers Selected - List of which servers are being selected the most by the load balancer algorithm.
    - Highest Bytes Out - List of which servers are outputting the most data.
    - Average Session Time - List of the average session time over the last 1024 requests
- **HAProxy Frontend**
    - Request Rate - The rate of requests being made to the frontend, useful to monitor spikes in traffic.
    - Session Rate - Number of sessions per second being created, also useful to monitor spikes in traffic.
    - Response 2xx, 4xx, 5xx - The ratio between 2xx and 4xx/5xx responses is ideally very low. Watch for spikes in 4xx or 5xx as they may show a misconfiguration or other potential errors.
    - Request Errors - Rate of error requests being made in the system. These may stem from early client termination, read errors from the client, client timeouts, or other various bad requests from the client.
    - Denied Requests - Rate of requests denied because of security concerns. This could be denied requests because they do not satisfy an ACL configuration, or some other deny.
    - Bytes Out - Number of bytes sent out.
    - Bytes In - Number of bytes sent in.
- **HAProxy Backend**
    - Current Queue Size - Number of items in the queued requests. If HAProxy hits the configured max number of connections, HAProxy will queue new incoming requests until a server becomes available.
    - Average Response Time - Lists average response time in seconds over the past 1024 requests. Backend must be using mode http, otherwise the metric will report 0.
    - Average Queue Time - The average time a request spends in the queue. This value should be low to keep the system latency low.
    - Top Servers Selected - List of which servers are being selected the most by the load balancer algorithm.
    - Response Errors - The backend error response rate. This metric can be correlated with denied responses and frontend requests to gain insight on potential errors.
    - Server Retries and Redispatches - Server retries occur when a server is not reached the first time. The request will be redispatched to another server if the retry limit is hit.
    - Connection Errors - The rate of connection errors includes both failed backend requests and general backend errors. Correlate with response errors and response codes to track down an issue.
    - Denied Responses - The rate of denied responses by the backend. Most denied responses will come from an ACL and can be correlated with 5xx responses.



### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
