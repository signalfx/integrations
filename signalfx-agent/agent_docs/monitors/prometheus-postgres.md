
<!--- Generated by to-integrations-repo script in Smart Agent repo, DO NOT MODIFY HERE --->
<!--- GENERATED BY gomplate from scripts/docs/monitor-page.md.tmpl --->

# prometheus/postgres

Monitor Type: `prometheus/postgres` ([Source](https://github.com/signalfx/signalfx-agent/tree/master/internal/monitors/prometheus/postgres))

**Accepts Endpoints**: **Yes**

**Multiple Instances Allowed**: Yes

## Overview

This monitor scrapes [Prmoetheus PostgreSQL Server
Exporter](https://github.com/wrouesnel/postgres_exporter) metrics and sends
them to SignalFx.  It is a wrapper around the
[prometheus-exporter](./prometheus-exporter.md) monitor that provides a
restricted but expandable set of metrics.


## Configuration

To activate this monitor in the Smart Agent, add the following to your
agent config:

```
monitors:  # All monitor config goes under this key
 - type: prometheus/postgres
   ...  # Additional config
```

**For a list of monitor options that are common to all monitors, see [Common
Configuration](../monitor-config.html#common-configuration).**


| Config option | Required | Type | Description |
| --- | --- | --- | --- |
| `host` | **yes** | `string` | Host of the exporter |
| `port` | **yes** | `integer` | Port of the exporter |
| `username` | no | `string` | Basic Auth username to use on each request, if any. |
| `password` | no | `string` | Basic Auth password to use on each request, if any. |
| `useHTTPS` | no | `bool` | If true, the agent will connect to the exporter using HTTPS instead of plain HTTP. (**default:** `false`) |
| `skipVerify` | no | `bool` | If useHTTPS is true and this option is also true, the exporter's TLS cert will not be verified. (**default:** `false`) |
| `useServiceAccount` | no | `bool` | Use pod service account to authenticate. (**default:** `false`) |
| `metricPath` | no | `string` | Path to the metrics endpoint on the exporter server, usually `/metrics` (the default). (**default:** `/metrics`) |
| `sendAllMetrics` | no | `bool` | Send all the metrics that come out of the Prometheus exporter without any filtering.  This option has no effect when using the prometheus exporter monitor directly since there is no built-in filtering, only when embedding it in other monitors. (**default:** `false`) |


## Metrics

These are the metrics available for this monitor.
Metrics that are categorized as
[container/host](https://docs.signalfx.com/en/latest/admin-guide/usage.html#about-custom-bundled-and-high-resolution-metrics)
(*default*) are ***in bold and italics*** in the list below.


 - `pg_exporter_last_scrape_duration_seconds` (*gauge*)<br>    Duration of the last scrape of metrics from PostgresSQL.
 - `pg_exporter_last_scrape_error` (*gauge*)<br>    Whether the last scrape of metrics from PostgreSQL resulted in an error (1 for error, 0 for success).
 - `pg_exporter_scrapes_total` (*cumulative*)<br>    Total number of times PostgresSQL was scraped for metrics.
 - `pg_exporter_user_queries_load_error` (*gauge*)<br>    Whether the user queries file was loaded and parsed successfully (1 for error, 0 for success).
 - `pg_locks_count` (*gauge*)<br>    Number of locks
 - `pg_postmaster_start_time_seconds` (*gauge*)<br>    Time at which postmaster started
 - `pg_replication_is_replica` (*gauge*)<br>    Indicates if this host is a slave
 - `pg_replication_lag` (*gauge*)<br>    Replication lag behind master in seconds
 - `pg_settings_allow_system_table_mods` (*gauge*)<br>    Allows modifications of the structure of system tables.
 - `pg_settings_archive_timeout_seconds` (*gauge*)<br>    Forces a switch to the next xlog file if a new file has not been started within N seconds. [Units converted to seconds.]
 - `pg_settings_array_nulls` (*gauge*)<br>    Enable input of NULL elements in arrays.
 - `pg_settings_authentication_timeout_seconds` (*gauge*)<br>    Sets the maximum allowed time to complete client authentication. [Units converted to seconds.]
 - `pg_settings_autovacuum` (*gauge*)<br>    Starts the autovacuum subprocess.
 - `pg_settings_autovacuum_analyze_scale_factor` (*gauge*)<br>    Number of tuple inserts, updates, or deletes prior to analyze as a fraction of reltuples.
 - `pg_settings_autovacuum_analyze_threshold` (*gauge*)<br>    Minimum number of tuple inserts, updates, or deletes prior to analyze.
 - `pg_settings_autovacuum_freeze_max_age` (*gauge*)<br>    Age at which to autovacuum a table to prevent transaction ID wraparound.
 - `pg_settings_autovacuum_max_workers` (*gauge*)<br>    Sets the maximum number of simultaneously running autovacuum worker processes.
 - `pg_settings_autovacuum_multixact_freeze_max_age` (*gauge*)<br>    Multixact age at which to autovacuum a table to prevent multixact wraparound.
 - `pg_settings_autovacuum_naptime_seconds` (*gauge*)<br>    Time to sleep between autovacuum runs. [Units converted to seconds.]
 - `pg_settings_autovacuum_vacuum_cost_delay_seconds` (*gauge*)<br>    Vacuum cost delay in milliseconds, for autovacuum. [Units converted to seconds.]
 - `pg_settings_autovacuum_vacuum_cost_limit` (*gauge*)<br>    Vacuum cost amount available before napping, for autovacuum.
 - `pg_settings_autovacuum_vacuum_scale_factor` (*gauge*)<br>    Number of tuple updates or deletes prior to vacuum as a fraction of reltuples.
 - `pg_settings_autovacuum_vacuum_threshold` (*gauge*)<br>    Minimum number of tuple updates or deletes prior to vacuum.
 - `pg_settings_autovacuum_work_mem_bytes` (*gauge*)<br>    Sets the maximum memory to be used by each autovacuum worker process. [Units converted to bytes.]
 - `pg_settings_backend_flush_after_bytes` (*gauge*)<br>    Number of pages after which previously performed writes are flushed to disk. [Units converted to bytes.]
 - `pg_settings_bgwriter_delay_seconds` (*gauge*)<br>    Background writer sleep time between rounds. [Units converted to seconds.]
 - `pg_settings_bgwriter_flush_after_bytes` (*gauge*)<br>    Number of pages after which previously performed writes are flushed to disk. [Units converted to bytes.]
 - `pg_settings_bgwriter_lru_maxpages` (*gauge*)<br>    Background writer maximum number of LRU pages to flush per round.
 - `pg_settings_bgwriter_lru_multiplier` (*gauge*)<br>    Multiple of the average buffer usage to free per round.
 - `pg_settings_block_size` (*gauge*)<br>    Shows the size of a disk block.
 - `pg_settings_bonjour` (*gauge*)<br>    Enables advertising the server via Bonjour.
 - `pg_settings_check_function_bodies` (*gauge*)<br>    Check function bodies during CREATE FUNCTION.
 - `pg_settings_checkpoint_completion_target` (*gauge*)<br>    Time spent flushing dirty buffers during checkpoint, as fraction of checkpoint interval.
 - `pg_settings_checkpoint_flush_after_bytes` (*gauge*)<br>    Number of pages after which previously performed writes are flushed to disk. [Units converted to bytes.]
 - `pg_settings_checkpoint_timeout_seconds` (*gauge*)<br>    Sets the maximum time between automatic WAL checkpoints. [Units converted to seconds.]
 - `pg_settings_checkpoint_warning_seconds` (*gauge*)<br>    Enables warnings if checkpoint segments are filled more frequently than this. [Units converted to seconds.]
 - `pg_settings_commit_delay` (*gauge*)<br>    Sets the delay in microseconds between transaction commit and flushing WAL to disk.
 - `pg_settings_commit_siblings` (*gauge*)<br>    Sets the minimum concurrent open transactions before performing commit_delay.
 - `pg_settings_cpu_index_tuple_cost` (*gauge*)<br>    Sets the planner's estimate of the cost of processing each index entry during an index scan.
 - `pg_settings_cpu_operator_cost` (*gauge*)<br>    Sets the planner's estimate of the cost of processing each operator or function call.
 - `pg_settings_cpu_tuple_cost` (*gauge*)<br>    Sets the planner's estimate of the cost of processing each tuple (row).
 - `pg_settings_cursor_tuple_fraction` (*gauge*)<br>    Sets the planner's estimate of the fraction of a cursor's rows that will be retrieved.
 - `pg_settings_data_checksums` (*gauge*)<br>    Shows whether data checksums are turned on for this cluster.
 - `pg_settings_db_user_namespace` (*gauge*)<br>    Enables per-database user names.
 - `pg_settings_deadlock_timeout_seconds` (*gauge*)<br>    Sets the time to wait on a lock before checking for deadlock. [Units converted to seconds.]
 - `pg_settings_debug_assertions` (*gauge*)<br>    Shows whether the running server has assertion checks enabled.
 - `pg_settings_debug_pretty_print` (*gauge*)<br>    Indents parse and plan tree displays.
 - `pg_settings_debug_print_parse` (*gauge*)<br>    Logs each query's parse tree.
 - `pg_settings_debug_print_plan` (*gauge*)<br>    Logs each query's execution plan.
 - `pg_settings_debug_print_rewritten` (*gauge*)<br>    Logs each query's rewritten parse tree.
 - `pg_settings_default_statistics_target` (*gauge*)<br>    Sets the default statistics target.
 - `pg_settings_default_transaction_deferrable` (*gauge*)<br>    Sets the default deferrable status of new transactions.
 - `pg_settings_default_transaction_read_only` (*gauge*)<br>    Sets the default read-only status of new transactions.
 - `pg_settings_default_with_oids` (*gauge*)<br>    Create new tables with OIDs by default.
 - `pg_settings_effective_cache_size_bytes` (*gauge*)<br>    Sets the planner's assumption about the size of the data cache. [Units converted to bytes.]
 - `pg_settings_effective_io_concurrency` (*gauge*)<br>    Number of simultaneous requests that can be handled efficiently by the disk subsystem.
 - `pg_settings_enable_bitmapscan` (*gauge*)<br>    Enables the planner's use of bitmap-scan plans.
 - `pg_settings_enable_hashagg` (*gauge*)<br>    Enables the planner's use of hashed aggregation plans.
 - `pg_settings_enable_hashjoin` (*gauge*)<br>    Enables the planner's use of hash join plans.
 - `pg_settings_enable_indexonlyscan` (*gauge*)<br>    Enables the planner's use of index-only-scan plans.
 - `pg_settings_enable_indexscan` (*gauge*)<br>    Enables the planner's use of index-scan plans.
 - `pg_settings_enable_material` (*gauge*)<br>    Enables the planner's use of materialization.
 - `pg_settings_enable_mergejoin` (*gauge*)<br>    Enables the planner's use of merge join plans.
 - `pg_settings_enable_nestloop` (*gauge*)<br>    Enables the planner's use of nested-loop join plans.
 - `pg_settings_enable_seqscan` (*gauge*)<br>    Enables the planner's use of sequential-scan plans.
 - `pg_settings_enable_sort` (*gauge*)<br>    Enables the planner's use of explicit sort steps.
 - `pg_settings_enable_tidscan` (*gauge*)<br>    Enables the planner's use of TID scan plans.
 - `pg_settings_escape_string_warning` (*gauge*)<br>    Warn about backslash escapes in ordinary string literals.
 - `pg_settings_exit_on_error` (*gauge*)<br>    Terminate session on any error.
 - `pg_settings_extra_float_digits` (*gauge*)<br>    Sets the number of digits displayed for floating-point values.
 - `pg_settings_from_collapse_limit` (*gauge*)<br>    Sets the FROM-list size beyond which subqueries are not collapsed.
 - `pg_settings_fsync` (*gauge*)<br>    Forces synchronization of updates to disk.
 - `pg_settings_full_page_writes` (*gauge*)<br>    Writes full pages to WAL when first modified after a checkpoint.
 - `pg_settings_geqo` (*gauge*)<br>    Enables genetic query optimization.
 - `pg_settings_geqo_effort` (*gauge*)<br>    GEQO: effort is used to set the default for other GEQO parameters.
 - `pg_settings_geqo_generations` (*gauge*)<br>    GEQO: number of iterations of the algorithm.
 - `pg_settings_geqo_pool_size` (*gauge*)<br>    GEQO: number of individuals in the population.
 - `pg_settings_geqo_seed` (*gauge*)<br>    GEQO: seed for random path selection.
 - `pg_settings_geqo_selection_bias` (*gauge*)<br>    GEQO: selective pressure within the population.
 - `pg_settings_geqo_threshold` (*gauge*)<br>    Sets the threshold of FROM items beyond which GEQO is used.
 - `pg_settings_gin_fuzzy_search_limit` (*gauge*)<br>    Sets the maximum allowed result for exact search by GIN.
 - `pg_settings_gin_pending_list_limit_bytes` (*gauge*)<br>    Sets the maximum size of the pending list for GIN index. [Units converted to bytes.]
 - `pg_settings_hot_standby` (*gauge*)<br>    Allows connections and queries during recovery.
 - `pg_settings_hot_standby_feedback` (*gauge*)<br>    Allows feedback from a hot standby to the primary that will avoid query conflicts.
 - `pg_settings_idle_in_transaction_session_timeout_seconds` (*gauge*)<br>    Sets the maximum allowed duration of any idling transaction. [Units converted to seconds.]
 - `pg_settings_ignore_checksum_failure` (*gauge*)<br>    Continues processing after a checksum failure.
 - `pg_settings_ignore_system_indexes` (*gauge*)<br>    Disables reading from system indexes.
 - `pg_settings_integer_datetimes` (*gauge*)<br>    Datetimes are integer based.
 - `pg_settings_join_collapse_limit` (*gauge*)<br>    Sets the FROM-list size beyond which JOIN constructs are not flattened.
 - `pg_settings_krb_caseins_users` (*gauge*)<br>    Sets whether Kerberos and GSSAPI user names should be treated as case-insensitive.
 - `pg_settings_lo_compat_privileges` (*gauge*)<br>    Enables backward compatibility mode for privilege checks on large objects.
 - `pg_settings_lock_timeout_seconds` (*gauge*)<br>    Sets the maximum allowed duration of any wait for a lock. [Units converted to seconds.]
 - `pg_settings_log_autovacuum_min_duration_seconds` (*gauge*)<br>    Sets the minimum execution time above which autovacuum actions will be logged. [Units converted to seconds.]
 - `pg_settings_log_checkpoints` (*gauge*)<br>    Logs each checkpoint.
 - `pg_settings_log_connections` (*gauge*)<br>    Logs each successful connection.
 - `pg_settings_log_disconnections` (*gauge*)<br>    Logs end of a session, including duration.
 - `pg_settings_log_duration` (*gauge*)<br>    Logs the duration of each completed SQL statement.
 - `pg_settings_log_executor_stats` (*gauge*)<br>    Writes executor performance statistics to the server log.
 - `pg_settings_log_file_mode` (*gauge*)<br>    Sets the file permissions for log files.
 - `pg_settings_log_hostname` (*gauge*)<br>    Logs the host name in the connection logs.
 - `pg_settings_log_lock_waits` (*gauge*)<br>    Logs long lock waits.
 - `pg_settings_log_min_duration_statement_seconds` (*gauge*)<br>    Sets the minimum execution time above which statements will be logged. [Units converted to seconds.]
 - `pg_settings_log_parser_stats` (*gauge*)<br>    Writes parser performance statistics to the server log.
 - `pg_settings_log_planner_stats` (*gauge*)<br>    Writes planner performance statistics to the server log.
 - `pg_settings_log_replication_commands` (*gauge*)<br>    Logs each replication command.
 - `pg_settings_log_rotation_age_seconds` (*gauge*)<br>    Automatic log file rotation will occur after N minutes. [Units converted to seconds.]
 - `pg_settings_log_rotation_size_bytes` (*gauge*)<br>    Automatic log file rotation will occur after N kilobytes. [Units converted to bytes.]
 - `pg_settings_log_statement_stats` (*gauge*)<br>    Writes cumulative performance statistics to the server log.
 - `pg_settings_log_temp_files_bytes` (*gauge*)<br>    Log the use of temporary files larger than this number of kilobytes. [Units converted to bytes.]
 - `pg_settings_log_truncate_on_rotation` (*gauge*)<br>    Truncate existing log files of same name during log rotation.
 - `pg_settings_logging_collector` (*gauge*)<br>    Start a subprocess to capture stderr output and/or csvlogs into log files.
 - `pg_settings_maintenance_work_mem_bytes` (*gauge*)<br>    Sets the maximum memory to be used for maintenance operations. [Units converted to bytes.]
 - `pg_settings_max_connections` (*gauge*)<br>    Sets the maximum number of concurrent connections.
 - `pg_settings_max_files_per_process` (*gauge*)<br>    Sets the maximum number of simultaneously open files for each server process.
 - `pg_settings_max_function_args` (*gauge*)<br>    Shows the maximum number of function arguments.
 - `pg_settings_max_identifier_length` (*gauge*)<br>    Shows the maximum identifier length.
 - `pg_settings_max_index_keys` (*gauge*)<br>    Shows the maximum number of index keys.
 - `pg_settings_max_locks_per_transaction` (*gauge*)<br>    Sets the maximum number of locks per transaction.
 - `pg_settings_max_parallel_workers_per_gather` (*gauge*)<br>    Sets the maximum number of parallel processes per executor node.
 - `pg_settings_max_pred_locks_per_transaction` (*gauge*)<br>    Sets the maximum number of predicate locks per transaction.
 - `pg_settings_max_prepared_transactions` (*gauge*)<br>    Sets the maximum number of simultaneously prepared transactions.
 - `pg_settings_max_replication_slots` (*gauge*)<br>    Sets the maximum number of simultaneously defined replication slots.
 - `pg_settings_max_stack_depth_bytes` (*gauge*)<br>    Sets the maximum stack depth, in kilobytes. [Units converted to bytes.]
 - `pg_settings_max_standby_archive_delay_seconds` (*gauge*)<br>    Sets the maximum delay before canceling queries when a hot standby server is processing archived WAL data. [Units converted to seconds.]
 - `pg_settings_max_standby_streaming_delay_seconds` (*gauge*)<br>    Sets the maximum delay before canceling queries when a hot standby server is processing streamed WAL data. [Units converted to seconds.]
 - `pg_settings_max_wal_senders` (*gauge*)<br>    Sets the maximum number of simultaneously running WAL sender processes.
 - `pg_settings_max_wal_size_bytes` (*gauge*)<br>    Sets the WAL size that triggers a checkpoint. [Units converted to bytes.]
 - `pg_settings_max_worker_processes` (*gauge*)<br>    Maximum number of concurrent worker processes.
 - `pg_settings_min_parallel_relation_size_bytes` (*gauge*)<br>    Sets the minimum size of relations to be considered for parallel scan. [Units converted to bytes.]
 - `pg_settings_min_wal_size_bytes` (*gauge*)<br>    Sets the minimum size to shrink the WAL to. [Units converted to bytes.]
 - `pg_settings_old_snapshot_threshold_seconds` (*gauge*)<br>    Time before a snapshot is too old to read pages changed after the snapshot was taken. [Units converted to seconds.]
 - `pg_settings_operator_precedence_warning` (*gauge*)<br>    Emit a warning for constructs that changed meaning since PostgreSQL 9.4.
 - `pg_settings_parallel_setup_cost` (*gauge*)<br>    Sets the planner's estimate of the cost of starting up worker processes for parallel query.
 - `pg_settings_parallel_tuple_cost` (*gauge*)<br>    Sets the planner's estimate of the cost of passing each tuple (row) from worker to master backend.
 - `pg_settings_password_encryption` (*gauge*)<br>    Encrypt passwords.
 - `pg_settings_port` (*gauge*)<br>    Sets the TCP port the server listens on.
 - `pg_settings_post_auth_delay_seconds` (*gauge*)<br>    Waits N seconds on connection startup after authentication. [Units converted to seconds.]
 - `pg_settings_pre_auth_delay_seconds` (*gauge*)<br>    Waits N seconds on connection startup before authentication. [Units converted to seconds.]
 - `pg_settings_quote_all_identifiers` (*gauge*)<br>    When generating SQL fragments, quote all identifiers.
 - `pg_settings_random_page_cost` (*gauge*)<br>    Sets the planner's estimate of the cost of a nonsequentially fetched disk page.
 - `pg_settings_replacement_sort_tuples` (*gauge*)<br>    Sets the maximum number of tuples to be sorted using replacement selection.
 - `pg_settings_restart_after_crash` (*gauge*)<br>    Reinitialize server after backend crash.
 - `pg_settings_row_security` (*gauge*)<br>    Enable row security.
 - `pg_settings_segment_size_bytes` (*gauge*)<br>    Shows the number of pages per disk file. [Units converted to bytes.]
 - `pg_settings_seq_page_cost` (*gauge*)<br>    Sets the planner's estimate of the cost of a sequentially fetched disk page.
 - `pg_settings_server_version_num` (*gauge*)<br>    Shows the server version as an integer.
 - `pg_settings_shared_buffers_bytes` (*gauge*)<br>    Sets the number of shared memory buffers used by the server. [Units converted to bytes.]
 - `pg_settings_sql_inheritance` (*gauge*)<br>    Causes subtables to be included by default in various commands.
 - `pg_settings_ssl` (*gauge*)<br>    Enables SSL connections.
 - `pg_settings_ssl_prefer_server_ciphers` (*gauge*)<br>    Give priority to server ciphersuite order.
 - `pg_settings_standard_conforming_strings` (*gauge*)<br>    Causes '...' strings to treat backslashes literally.
 - `pg_settings_statement_timeout_seconds` (*gauge*)<br>    Sets the maximum allowed duration of any statement. [Units converted to seconds.]
 - `pg_settings_superuser_reserved_connections` (*gauge*)<br>    Sets the number of connection slots reserved for superusers.
 - `pg_settings_synchronize_seqscans` (*gauge*)<br>    Enable synchronized sequential scans.
 - `pg_settings_syslog_sequence_numbers` (*gauge*)<br>    Add sequence number to syslog messages to avoid duplicate suppression.
 - `pg_settings_syslog_split_messages` (*gauge*)<br>    Split messages sent to syslog by lines and to fit into 1024 bytes.
 - `pg_settings_tcp_keepalives_count` (*gauge*)<br>    Maximum number of TCP keepalive retransmits.
 - `pg_settings_tcp_keepalives_idle_seconds` (*gauge*)<br>    Time between issuing TCP keepalives. [Units converted to seconds.]
 - `pg_settings_tcp_keepalives_interval_seconds` (*gauge*)<br>    Time between TCP keepalive retransmits. [Units converted to seconds.]
 - `pg_settings_temp_buffers_bytes` (*gauge*)<br>    Sets the maximum number of temporary buffers used by each session. [Units converted to bytes.]
 - `pg_settings_temp_file_limit_bytes` (*gauge*)<br>    Limits the total size of all temporary files used by each process. [Units converted to bytes.]
 - `pg_settings_trace_notify` (*gauge*)<br>    Generates debugging output for LISTEN and NOTIFY.
 - `pg_settings_trace_sort` (*gauge*)<br>    Emit information about resource usage in sorting.
 - `pg_settings_track_activities` (*gauge*)<br>    Collects information about executing commands.
 - `pg_settings_track_activity_query_size` (*gauge*)<br>    Sets the size reserved for pg_stat_activity.query, in bytes.
 - `pg_settings_track_commit_timestamp` (*gauge*)<br>    Collects transaction commit time.
 - `pg_settings_track_counts` (*gauge*)<br>    Collects statistics on database activity.
 - `pg_settings_track_io_timing` (*gauge*)<br>    Collects timing statistics for database I/O activity.
 - `pg_settings_transaction_deferrable` (*gauge*)<br>    Whether to defer a read-only serializable transaction until it can be executed with no possible serialization failures.
 - `pg_settings_transaction_read_only` (*gauge*)<br>    Sets the current transaction's read-only status.
 - `pg_settings_transform_null_equals` (*gauge*)<br>    Treats "expr=NULL" as "expr IS NULL".
 - `pg_settings_unix_socket_permissions` (*gauge*)<br>    Sets the access permissions of the Unix-domain socket.
 - `pg_settings_update_process_title` (*gauge*)<br>    Updates the process title to show the active SQL command.
 - `pg_settings_vacuum_cost_delay_seconds` (*gauge*)<br>    Vacuum cost delay in milliseconds. [Units converted to seconds.]
 - `pg_settings_vacuum_cost_limit` (*gauge*)<br>    Vacuum cost amount available before napping.
 - `pg_settings_vacuum_cost_page_dirty` (*gauge*)<br>    Vacuum cost for a page dirtied by vacuum.
 - `pg_settings_vacuum_cost_page_hit` (*gauge*)<br>    Vacuum cost for a page found in the buffer cache.
 - `pg_settings_vacuum_cost_page_miss` (*gauge*)<br>    Vacuum cost for a page not found in the buffer cache.
 - `pg_settings_vacuum_defer_cleanup_age` (*gauge*)<br>    Number of transactions by which VACUUM and HOT cleanup should be deferred, if any.
 - `pg_settings_vacuum_freeze_min_age` (*gauge*)<br>    Minimum age at which VACUUM should freeze a table row.
 - `pg_settings_vacuum_freeze_table_age` (*gauge*)<br>    Age at which VACUUM should scan whole table to freeze tuples.
 - `pg_settings_vacuum_multixact_freeze_min_age` (*gauge*)<br>    Minimum age at which VACUUM should freeze a MultiXactId in a table row.
 - `pg_settings_vacuum_multixact_freeze_table_age` (*gauge*)<br>    Multixact age at which VACUUM should scan whole table to freeze tuples.
 - `pg_settings_wal_block_size` (*gauge*)<br>    Shows the block size in the write ahead log.
 - `pg_settings_wal_buffers_bytes` (*gauge*)<br>    Sets the number of disk-page buffers in shared memory for WAL. [Units converted to bytes.]
 - `pg_settings_wal_compression` (*gauge*)<br>    Compresses full-page writes written in WAL file.
 - `pg_settings_wal_keep_segments` (*gauge*)<br>    Sets the number of WAL files held for standby servers.
 - `pg_settings_wal_log_hints` (*gauge*)<br>    Writes full pages to WAL when first modified after a checkpoint, even for a non-critical modifications.
 - `pg_settings_wal_receiver_status_interval_seconds` (*gauge*)<br>    Sets the maximum interval between WAL receiver status reports to the primary. [Units converted to seconds.]
 - `pg_settings_wal_receiver_timeout_seconds` (*gauge*)<br>    Sets the maximum wait time to receive data from the primary. [Units converted to seconds.]
 - `pg_settings_wal_retrieve_retry_interval_seconds` (*gauge*)<br>    Sets the time to wait before retrying to retrieve WAL after a failed attempt. [Units converted to seconds.]
 - `pg_settings_wal_segment_size_bytes` (*gauge*)<br>    Shows the number of pages per write ahead log segment. [Units converted to bytes.]
 - `pg_settings_wal_sender_timeout_seconds` (*gauge*)<br>    Sets the maximum time to wait for WAL replication. [Units converted to seconds.]
 - `pg_settings_wal_writer_delay_seconds` (*gauge*)<br>    Time between WAL flushes performed in the WAL writer. [Units converted to seconds.]
 - `pg_settings_wal_writer_flush_after_bytes` (*gauge*)<br>    Amount of WAL written out by WAL writer that triggers a flush. [Units converted to bytes.]
 - `pg_settings_work_mem_bytes` (*gauge*)<br>    Sets the maximum memory to be used for query workspaces. [Units converted to bytes.]
 - `pg_settings_zero_damaged_pages` (*gauge*)<br>    Continues processing past damaged page headers.
 - `pg_slow_queries` (*gauge*)<br>    Current number of slow queries
 - ***`pg_stat_activity_count`*** (*gauge*)<br>    Number of connections in this state
 - ***`pg_stat_activity_max_tx_duration`*** (*gauge*)<br>    Max duration in seconds any active transaction has been running
 - `pg_stat_bgwriter_buffers_alloc` (*cumulative*)<br>    Number of buffers allocated
 - `pg_stat_bgwriter_buffers_backend` (*cumulative*)<br>    Number of buffers written directly by a backend
 - `pg_stat_bgwriter_buffers_backend_fsync` (*cumulative*)<br>    Number of times a backend had to execute its own fsync call (normally the background writer handles those even when the backend does its own write)
 - `pg_stat_bgwriter_buffers_checkpoint` (*cumulative*)<br>    Number of buffers written during checkpoints
 - `pg_stat_bgwriter_buffers_clean` (*cumulative*)<br>    Number of buffers written by the background writer
 - `pg_stat_bgwriter_checkpoint_sync_time` (*cumulative*)<br>    Total amount of time that has been spent in the portion of checkpoint processing where files are synchronized to disk, in milliseconds
 - `pg_stat_bgwriter_checkpoint_write_time` (*cumulative*)<br>    Total amount of time that has been spent in the portion of checkpoint processing where files are written to disk, in milliseconds
 - `pg_stat_bgwriter_checkpoints_req` (*cumulative*)<br>    Number of requested checkpoints that have been performed
 - `pg_stat_bgwriter_checkpoints_timed` (*cumulative*)<br>    Number of scheduled checkpoints that have been performed
 - `pg_stat_bgwriter_maxwritten_clean` (*cumulative*)<br>    Number of times the background writer stopped a cleaning scan because it had written too many buffers
 - `pg_stat_bgwriter_stats_reset` (*cumulative*)<br>    Time at which these statistics were last reset
 - ***`pg_stat_database_blk_read_time`*** (*cumulative*)<br>    Time spent reading data file blocks by backends in this database, in milliseconds
 - ***`pg_stat_database_blk_write_time`*** (*cumulative*)<br>    Time spent writing data file blocks by backends in this database, in milliseconds
 - ***`pg_stat_database_blks_hit`*** (*cumulative*)<br>    Number of times disk blocks were found already in the buffer cache, so that a read was not necessary (this only includes hits in the PostgreSQL buffer cache, not the operating system's file system cache)
 - ***`pg_stat_database_blks_read`*** (*cumulative*)<br>    Number of disk blocks read in this database
 - `pg_stat_database_conflicts` (*cumulative*)<br>    Number of queries canceled due to conflicts with recovery in this database. (Conflicts occur only on standby servers; see pg_stat_database_conflicts for details.)
 - ***`pg_stat_database_conflicts_confl_bufferpin`*** (*cumulative*)<br>    Number of queries in this database that have been canceled due to pinned buffers
 - ***`pg_stat_database_conflicts_confl_deadlock`*** (*cumulative*)<br>    Number of queries in this database that have been canceled due to deadlocks
 - ***`pg_stat_database_conflicts_confl_lock`*** (*cumulative*)<br>    Number of queries in this database that have been canceled due to lock timeouts
 - ***`pg_stat_database_conflicts_confl_snapshot`*** (*cumulative*)<br>    Number of queries in this database that have been canceled due to old snapshots
 - ***`pg_stat_database_conflicts_confl_tablespace`*** (*cumulative*)<br>    Number of queries in this database that have been canceled due to dropped tablespaces
 - `pg_stat_database_deadlocks` (*cumulative*)<br>    Number of deadlocks detected in this database
 - ***`pg_stat_database_numbackends`*** (*gauge*)<br>    Number of backends currently connected to this database. This is the only column in this view that returns a value reflecting current state; all other columns return the accumulated values since the last reset.
 - `pg_stat_database_stats_reset` (*cumulative*)<br>    Time at which these statistics were last reset
 - ***`pg_stat_database_temp_bytes`*** (*cumulative*)<br>    Total amount of data written to temporary files by queries in this database. All temporary files are counted, regardless of why the temporary file was created, and regardless of the log_temp_files setting.
 - ***`pg_stat_database_temp_files`*** (*cumulative*)<br>    Number of temporary files created by queries in this database. All temporary files are counted, regardless of why the temporary file was created (e.g., sorting or hashing), and regardless of the log_temp_files setting.
 - ***`pg_stat_database_tup_deleted`*** (*cumulative*)<br>    Number of rows deleted by queries in this database
 - ***`pg_stat_database_tup_fetched`*** (*cumulative*)<br>    Number of rows fetched by queries in this database
 - ***`pg_stat_database_tup_inserted`*** (*cumulative*)<br>    Number of rows inserted by queries in this database
 - ***`pg_stat_database_tup_returned`*** (*cumulative*)<br>    Number of rows returned by queries in this database
 - ***`pg_stat_database_tup_updated`*** (*cumulative*)<br>    Number of rows updated by queries in this database
 - ***`pg_stat_database_xact_commit`*** (*cumulative*)<br>    Number of transactions in this database that have been committed
 - ***`pg_stat_database_xact_rollback`*** (*cumulative*)<br>    Number of transactions in this database that have been rolled back
 - `pg_static` (*gauge*)<br>    Version string as reported by postgres
 - `pg_stuck_idle_in_transaction_queries` (*gauge*)<br>    Current number of queries that are stuck being idle in transactions
 - ***`pg_total_relation_size_bytes`*** (*gauge*)<br>    Total disk space usage for the specified table and associated indexes
 - `pg_up` (*gauge*)<br>    Whether the last scrape of metrics from PostgreSQL was able to connect to the server (1 for yes, 0 for no).
 - `pg_vacuum_age_in_seconds` (*gauge*)<br>    The current maximum VACUUM query age in seconds
 - `pg_vacuum_analyze_age_in_seconds` (*gauge*)<br>    The current maximum VACUUM ANALYZE query age in seconds
 - `pg_vacuum_analyze_queries` (*gauge*)<br>    The current number of VACUUM ANALYZE queries
 - `pg_vacuum_queries` (*gauge*)<br>    The current number of VACUUM queries

### Non-default metrics (version 4.7.0+)

**The following information applies to the agent version 4.7.0+ that has
`enableBuiltInFiltering: true` set on the top level of the agent config.**

To emit metrics that are not _default_, you can add those metrics in the
generic monitor-level `extraMetrics` config option.  Metrics that are derived
from specific configuration options that do not appear in the above list of
metrics do not need to be added to `extraMetrics`.

To see a list of metrics that will be emitted you can run `agent-status
monitors` after configuring this monitor in a running agent instance.

### Legacy non-default metrics (version < 4.7.0)

**The following information only applies to agent version older than 4.7.0. If
you have a newer agent and have set `enableBuiltInFiltering: true` at the top
level of your agent config, see the section above. See upgrade instructions in
[Old-style whitelist filtering](../legacy-filtering.html#old-style-whitelist-filtering).**

If you have a reference to the `whitelist.json` in your agent's top-level
`metricsToExclude` config option, and you want to emit metrics that are not in
that whitelist, then you need to add an item to the top-level
`metricsToInclude` config option to override that whitelist (see [Inclusion
filtering](../legacy-filtering.html#inclusion-filtering).  Or you can just
copy the whitelist.json, modify it, and reference that in `metricsToExclude`.


