# ![](https://github.com/signalfx/integrations/blob/master/collectd-varnish/img/integrations_varnish.png) Varnish

_This is a directory that consolidates all the metadata associated with the Varnish collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/varnish.c)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

The Varnish collectd plugin collects metrics from Varnish and sends them to SignalFx.

Varnish Cache is a web application accelerator also known as a caching HTTP reverse proxy. You install it in front of any server that speaks HTTP and configure it to cache the contents. Varnish Cache is really, really fast. It typically speeds up delivery with a factor of 300 - 1000x, depending on your architecture.

#### FEATURES

##### Built-in dashboards

- **Varnish (a)**: Overview of data from all Varnish servers.

  [<img src='./img/dashboard_varnish_a.png' width=200px>](./img/dashboard_varnish_a.png)

- **Varnish**: Focus on a single Varnish server.

  [<img src='./img/dashboard_varnish.png' width=200px>](./img/dashboard_varnish.png)

### REQUIREMENTS AND DEPENDENCIES

| Software  | Version        |
|-----------|----------------|
| collectd  |  5.1* or later (varnish 4.0+ requires collectd 5.5+)  |


### INSTALLATION

1. On RHEL/CentOS and Amazon Linux systems, run the following command to install this plugin:

         yum install collectd-varnish

1. Download SignalFx's [sample configuration file](https://github.com/signalfx/integrations/blob/master/collectd-varnish/10-varnish.conf) to `/etc/collectd/managed_config`.

1. Modify the sample configuration file to provide values that make sense for your environment, as described in [Configuration](#configuration) below.

1. Restart collectd.

#### Special Instructions for installing Varnish 3 on Ubuntu

Starting with collectd 5.6.1-sfx0, the varnish plugin provided within the SignalFx Package only supports varnish 4.
Follow these steps to add varnish 3 plugin support:

1. Copy the [varnish3.so](https://dl.signalfx.com/debs/collectd-varnish/varnish3.so) file to the library directory at /usr/lib/share/collectd/.

1. Update the configuration file `10-varnish.conf` in your `/etc/collectd/managed_config` directory to show varnish3 instead of varnish as the name used by the LoadPlugin and Plugin lines.

1. Restart collectd.


### CONFIGURATION

There is no configuration required for the varnish collectd plugin. The default configuration is setup to bring in data on a large variety of metrics.

If using the sample configuration file [10-varnish.conf](https://github.com/signalfx/integrations/tree/master/collectd-varnish/10-varnish.conf), no additional configuration is required. The following optional settings allow you to configure the metrics that will be sent using this plugin:

| Setting            | Description     | Default  |
|--------------------|----------------------------|----------|
| CollectBackend     | Back-end connection statistics, such as successful, reused, and closed connections.                               | enabled  |
| CollectCache       | Cache hits and misses.                                                                                            | enabled  |
| CollectConnections | Number of client connections received, accepted and dropped.                                                      | enabled  |
| CollectESI         | Edge Side Includes (ESI) parse statistics.                                                                        | enabled |
| CollectFetch       | Statistics about fetches (HTTP requests sent to the backend).                                                     | enabled |
| CollectHCB         | Inserts and look-ups in the crit bit tree based hash. Look-ups are divided into locked and unlocked look-ups.     | enabled |
| CollectSHM         | Statistics about the shared memory log, a memory region to store log messages which is flushed to disk when full. | enabled  |
| CollectSM          | file (memory mapped file) storage statistics.                                                                     | enabled |
| CollectSMA         | malloc or umem (umem_alloc(3MALLOC) based) storage statistics. The umem storage component is Solaris specific.    | enabled |
| CollectSMS         | synth (synthetic content) storage statistics. This storage component is used internally only.                     | enabled |
| CollectTotals      | Collects overview counters, such as the number of sessions created, the number of requests and bytes transferred. | enabled |
| CollectWorkers     | Collect statistics about worker threads.                                                                          | enabled |

### USAGE

Sample of pre-built dashboard in SignalFx:

![](././img/dashboard_varnish.png)

### METRICS

| Field name        | Description                   | Collected (Yes/No) | Collectd option    |
|-------------------|-------------------------------|--------------------|--------------------|
| uptime            | Child uptime                  | No                 | n/a                |
| client_conn       | Client connections accepted   | Yes                | CollectConnections |
| client_drop       | Connection dropped, no sess   | Yes                |                    |
| client_req        | Client requests received      | Yes                |                    |
| cache_hit         | Cache hits                    | Yes                | CollectCache       |
| cache_hitpass     | Cache hits for pass           | Yes                |                    |
| cache_miss        | Cache misses                  | Yes                |                    |
| backend_conn      | Backend conn. success         | Yes                | CollectBackend     |
| backend_unhealthy | Backend conn. not attempted   | Yes                |                    |
| backend_busy      | Backend conn. too many        | Yes                |                    |
| backend_fail      | Backend conn. failures        | Yes                |                    |
| backend_reuse     | Backend conn. reuses          | Yes                |                    |
| backend_toolate   | Backend conn. was closed      | Yes                |                    |
| backend_recycle   | Backend conn. recycles        | Yes                |                    |
| backend_unused    | Backend conn. unused          | Yes                |                    |
| fetch_head        | Fetch head                    | Yes                | CollectFetch       |
| fetch_length      | Fetch with Length             | Yes                |                    |
| fetch_chunked     | Fetch chunked                 | Yes                |                    |
| fetch_eof         | Fetch EOF                     | Yes                |                    |
| fetch_bad         | Fetch had bad headers         | Yes                |                    |
| fetch_close       | Fetch wanted close            | Yes                |                    |
| fetch_oldhttp     | Fetch pre HTTP/1.1 closed     | Yes                |                    |
| fetch_zero        | Fetch zero len                | Yes                |                    |
| fetch_failed      | Fetch failed                  | Yes                |                    |
| n_sess_mem        | N struct sess_mem             | No                 | n/a                |
| n_sess            | N struct sess                 | No                 |                    |
| n_object          | N struct object               | No                 |                    |
| n_vampireobject   | N unresurrected objects       | No                 |                    |
| n_objectcore      | N struct objectcore           | No                 |                    |
| n_objecthead      | N struct objecthead           | No                 |                    |
| n_smf             | N struct smf                  | No                 |                    |
| n_smf_frag        | N small free smf              | No                 |                    |
| n_smf_large       | N large free smf              | No                 |                    |
| n_vbe_conn        | N struct vbe_conn             | No                 |                    |
| n_wrk             | N worker threads              | Yes                | CollectWorkers     |
| n_wrk_create      | N worker threads created      | Yes                |                    |
| n_wrk_failed      | N worker threads not created  | Yes                |                    |
| n_wrk_max         | N worker threads limited      | Yes                |                    |
| n_wrk_queue       | N queued work requests        | Yes                |                    |
| n_wrk_overflow    | N overflowed work requests    | Yes                |                    |
| n_wrk_drop        | N dropped work requests       | Yes                |                    |
| n_backend         | N backends                    | No                 | n/a                |
| n_expired         | N expired objects             | No                 |                    |
| n_lru_nuked       | N LRU nuked objects           | No                 |                    |
| n_lru_saved       | N LRU saved objects           | No                 |                    |
| n_lru_moved       | N LRU moved objects           | No                 |                    |
| n_deathrow        | N objects on deathrow         | No                 |                    |
| losthdr           | HTTP header overflows         | No                 |                    |
| n_objsendfile     | Objects sent with sendfile    | No                 |                    |
| n_objwrite        | Objects sent with write       | No                 |                    |
| n_objoverflow     | Objects overflowing workspace | No                 |                    |
| s_sess            | Total Sessions                | Yes                | CollectTotals      |
| s_req             | Total Requests                | Yes                |                    |
| s_pipe            | Total pipe                    | Yes                |                    |
| s_pass            | Total pass                    | Yes                |                    |
| s_fetch           | Total fetch                   | Yes                |                    |
| s_hdrbytes        | Total header bytes            | Yes                |                    |
| s_bodybytes       | Total body bytes              | Yes                |                    |
| sess_closed       | Session Closed                | No                 | n/a                |
| sess_pipeline     | Session Pipeline              | No                 |                    |
| sess_readahead    | Session Read Ahead            | No                 |                    |
| sess_linger       | Session Linger                | No                 |                    |
| sess_herd         | Session herd                  | No                 |                    |
| shm_records       | SHM records                   | Yes                | CollectSHM         |
| shm_writes        | SHM writes                    | Yes                |                    |
| shm_flushes       | SHM flushes due to overflow   | Yes                |                    |
| shm_cont          | SHM MTX contention            | Yes                |                    |
| shm_cycles        | SHM cycles through buffer     | Yes                |                    |
| sm_nreq           | allocator requests            | Yes                | CollectSM          |
| sm_nobj           | outstanding allocations       | Yes                |                    |
| sm_balloc         | bytes allocated               | Yes                |                    |
| sm_bfree          | bytes free                    | Yes                |                    |
| sma_nreq          | SMA allocator requests        | Yes                | CollectSMA         |
| sma_nobj          | SMA outstanding allocations   | Yes                |                    |
| sma_nbytes        | SMA outstanding bytes         | Yes                |                    |
| sma_balloc        | SMA bytes allocated           | Yes                |                    |
| sma_bfree         | SMA bytes free                | Yes                |                    |
| sms_nreq          | SMS allocator requests        | Yes                | CollectSMS         |
| sms_nobj          | SMS outstanding allocations   | Yes                |                    |
| sms_nbytes        | SMS outstanding bytes         | Yes                |                    |
| sms_balloc        | SMS bytes allocated           | Yes                |                    |
| sms_bfree         | SMS bytes freed               | Yes                |                    |
| backend_req       | Backend requests made         | No                 | n/a                |
| n_vcl             | N vcl total                   | No                 |                    |
| n_vcl_avail       | N vcl available               | No                 |                    |
| n_vcl_discard     | N vcl discarded               | No                 |                    |
| n_purge           | N total active purges         | No                 |                    |
| n_purge_add       | N new purges added            | No                 |                    |
| n_purge_retire    | N old purges deleted          | No                 |                    |
| n_purge_obj_test  | N objects tested              | No                 |                    |
| n_purge_re_test   | N regexps tested against      | No                 |                    |
| n_purge_dups      | N duplicate purges removed    | No                 |                    |
| hcb_nolock        | HCB Lookups without lock      | Yes                | CollectHCB         |
| hcb_lock          | HCB Lookups with lock         | Yes                |                    |
| hcb_insert        | HCB Inserts                   | Yes                |                    |
| esi_parse         | Objects ESI parsed (unlock)   | Yes                | CollectESI         |
| esi_errors        | ESI parse errors (unlock)     | Yes                |                    |

For segmented metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
