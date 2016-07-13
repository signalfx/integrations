# Ruby client library for SignalFx


- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Usage](#usage)
 - [Create client](#create-client)
 - [Sending metrics](#sending-metrics)
 - [Sending multi-dimensional metrics](#multi-dimensional)
 - [Sending events](#sending-events)
- [Examples](#examples)
- [License](#license)



### <a name="description"></a>DESCRIPTION

<code>signalfx-ruby</code> is a programmatic interface in
Ruby for SignalFx's metadata and ingest APIs. It is meant
to provide a base for communicating with SignalFx APIs
that can be easily leveraged by scripts and applications
to interact with SignalFx or report metric and event data
to SignalFx.


### <a name="requirements-and-dependencies"></a>REQUIREMENTS AND DEPENDENCIES

#### Ruby version

This library supports Ruby 2.x.

#### API access token

To use this library, you need a SignalFx API access
token. [Click here for more information on retrieving your API token](https://developers.signalfx.com/docs/authentication-overview).


### <a name="installation"></a>INSTALLATION

Add this line to your application's Gemfile:

    gem 'signalfx'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install signalfx


### <a name="usage"></a>USAGE

#### <a name="create-client">Create client

The default constructor `SignalFx` uses Protobuf to send data to SignalFx. If it cannot send Protobuf, it falls back to sending JSON.

```ruby
require('signalfx')

// Create client
client = SignalFx.new 'MY_SIGNALFX_TOKEN'
```

Optional constructor parameters:
+ **api_token** - Your private SignalFx token
+ **enable_aws_unique_id** - boolean, `false` by default.
       If `true`, library will retrieve Amazon unique identifier
       and set it as `AWSUniqueId` dimension for each datapoint and event.
       Use this option only if your application deployed to Amazon
+ **ingest_endpoint** - string
+ **api_endpoint** - string
+ **timeout** - number
+ **batch_size** - number
+ **user_agents** - array

#### <a name="sending-metrics">Sending metrics

The core function of the library is to send metric data to SignalFx. For example:

```ruby
require('signalfx')

client = SignalFx.new 'MY_SIGNALFX_TOKEN'

client.send(
           cumulative_counters:[
             {  :metric => 'myfunc.calls_cumulative',
                :value => 10,
                :timestamp => 1442960607000 },
             ...
           ],
           gauges:[
             {  :metric => 'myfunc.time',
                :value => 532,
                :timestamp => 1442960607000},
             ...
           ],
           counters:[
             {  :metric => 'myfunc.calls',
                :value => 42,
                :timestamp => 1442960607000},
             ...
           ])
```
The `timestamp` must be a millisecond precision timestamp; the number of milliseconds elapsed since Epoch. The `timestamp` field is optional, but strongly recommended. If not specified, it will be set by SignalFx's ingest servers automatically; in this situation, the timestamp of your datapoints will not accurately represent the time of their measurement (network latency, batching, etc. will all impact when those datapoints actually make it to SignalFx).


#### <a name="multi-dimensional">Sending multi-dimensional metrics

The SignalFx data format includes the concept of
dimensions. Time series dimensions are custom key/value
pairs in combination with the metric name that identify
the metric time series. Dimensions are also useful in
aggregating and filtering metrics. For example, sending
an "environment" dimension with each datapoint would
allow you to vary alerts based on the different
environments that metrics are being sent from.

Reporting dimensions for the data can be accomplished
by specifying a `dimensions` parameter on each datapoint
containing a dictionary of string to string key/value
pairs representing the dimensions:

```ruby
require('signalfx')

client = SignalFx.new 'MY_SIGNALFX_TOKEN'

client.send(
          cumulative_counters:[
            {   :metric => 'myfunc.calls_cumulative',
                :value => 10,
                :dimensions => [{:key => 'host', :value => 'server1'}]},
            ...
          ],
          gauges:[
            {   :metric => 'myfunc.time',
                :value=> 532,
                :dimensions=> [{:key => 'host', :value => 'server1'}]},
            ...
          ],
          counters:[
            {   :metric=> 'myfunc.calls',
                :value=> 42,
                :dimensions=> [{:key => 'host', :value => 'server1'}]},
            ...
          ])
```
See `examples/generic_usecase.rb` for a complete code example for Reporting data.


#### <a name="sending-events">Sending events

Events can be sent to SignalFx via the `send_event` function. The
event type must be specified, and dimensions and extra event properties
can be supplied as well. Also please specify event category: for that get
option from dictionary `EVENT_CATEGORIES`. Different categories of events are supported.
Available categories of events are `USER_DEFINED`, `ALERT`, `AUDIT`, `JOB`,
`COLLECTD`, `SERVICE_DISCOVERY`, `EXCEPTION`.

```ruby
require('signalfx')

client = SignalFx.new 'MY_SIGNALFX_TOKEN'

client.send_event(
          '[event_type]',
          '[event_category]',
          {
              host: 'myhost',
              service: 'myservice',
              instance: 'myinstance'
          },
          properties={
              version: 'event_version'},
          timestamp)
```

See `examples/generic_usecase.rb` for a complete code example for Reporting data.


### <a name="license"></a>LICENSE

Apache Software License v2 © [SignalFx](https://signalfx.com)
