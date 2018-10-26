# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_collectd.png) Write-HTTP

Metadata associated with the Write-HTTP collectd plugin can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-write_http">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/write_http.c">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

### DESCRIPTION

The Write HTTP plugin sends the values collected by collectd to a web-server using HTTP POST requests. The data is formatted as PUTVAL commands, see plain text protocol. The <a target="_blank" href="https://github.com/signalfx/collectd">SignalFx collectd agent</a> version of this plugin has been extended with **Buffer Flushing** to ensure that metrics always arrive in a timely manner, we’ve added a timer so that it transmits data to SignalFx either when the data buffer is full or when a time limit is reached, whichever happens first. This capability is particularly useful if you are only collecting small quantities of time-sensitive metrics.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software | Version |
|----------|---------|
| collectd |  4.8+   |

### INSTALLATION

Installation and initial configuration options are available as part of the <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd">SignalFx collectd agent</a>.


### CONFIGURATION

From <a target="_blank" href="https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_write_http">collectd wiki</a>:

>This output plugin submits values to an HTTP server using POST requests and encoding metrics with JSON or using the PUTVAL command described in collectd-unixsock(5).

```
Synopsis:

 <Plugin "write_http">
   <Node "example">
     URL "http://example.com/post-collectd";
     User "collectd"
     Password "weCh3ik0"
     Format JSON
   </Node>
 </Plugin>
```

> The plugin can send values to multiple HTTP servers by specifying one <Node Name> block for each server. Within each Node block, the following options are available:

| Option | type | description |
|----------|---------|---------------------|
|URL| URL|URL to which the values are submitted to. Mandatory.|
|User| Username|Optional user name needed for authentication.|
|Password| Password|Optional password needed for authentication.|
|VerifyPeer| true/false|Enable or disable peer SSL certificate verification. See http://curl.haxx.se/docs/sslcerts.html for details. Enabled by default.|
|VerifyHost| true/false|Enable or disable peer host name verification. If enabled, the plugin checks if the Common Name or a Subject Alternate Name field of the SSL certificate matches the host name provided by the URL option. If this identity check fails, the connection is aborted. Obviously, only works when connecting to a SSL enabled server. Enabled by default.|
|CACert |File|File that holds one or more SSL certificates. If you want to use HTTPS you will possibly need this option. What CA certificates come bundled with libcurl and are checked by default depends on the distribution you use.|
|CAPath| Directory|Directory holding one or more CA certificate files. You can use this if for some reason all the needed CA certificates aren't in the same file and can't be pointed to using the CACert option. Requires libcurl to be built against OpenSSL.|
|ClientKey| File|File that holds the private key in PEM format to be used for certificate-based authentication.|
|ClientCert| File|File that holds the SSL certificate to be used for certificate-based authentication.|
|ClientKeyPass| Password|Password required to load the private key in ClientKey.|
|SSLVersion | SSLv2/SSLv3/TLSv1/TLSv1\_0/TLSv1\_1/TLSv1\_2|Define which SSL protocol version must be used. By default libcurl will attempt to figure out the remote SSL protocol version. See curl\_easy\_setopt(3) for more details.|
|Format |Command/JSON|Format of the output to generate. If set to Command, will create output that is understood by the Exec and UnixSock plugins. When set to JSON, will create output in the JavaScript Object Notation (JSON). Defaults to Command.|
|StoreRates| true/false|If set to true, convert counter values to rates. If set to false (the default) counter values are stored as is, i.e. as an increasing integer number.|
|BufferSize| Bytes|Sets the send buffer size to Bytes. By increasing this buffer, less HTTP requests will be generated, but more metrics will be batched / metrics are cached for longer before being sent, introducing additional delay until they are available on the server side. Bytes must be at least 1024 and cannot exceed the size of an int, i.e. 2 GByte. Defaults to 4096.|
|LowSpeedLimit| Bytes per Second|Sets the minimal transfer rate in Bytes per Second below which the connection with the HTTP server will be considered too slow and aborted. All the data submitted over this connection will probably be lost. Defaults to 0, which means no minimum transfer rate is enforced.|
|Timeout| Timeout|Sets the maximum time in milliseconds given for HTTP POST operations to complete. When this limit is reached, the POST operation will be aborted, and all the data in the current send buffer will probably be lost. Defaults to 0, which means the connection never times out.|

>The write_http plugin regularly submits the collected values to the HTTP server. How frequently this happens depends on how much data you are collecting and the size of BufferSize. The optimal value to set Timeout to is slightly below this interval, which you can estimate by monitoring the network traffic between collectd and the HTTP server.


### LICENSE

License for this plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/write_http.c">in the header of the plugin</a>
