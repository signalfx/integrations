## Conviva Monitor Metric Parameters and Metrics

Metric Parameters are conviva monitor metricParameter configuration values. Metrics are the metrics that get reported to SignalFx

|Metric Parameters|Metrics|Description|
|----------------|------|-----------|
|attempts|conviva.<br/>attempts|Attempts time-series|
|avg_bitrate|conviva.<br/>avg_bitrate|Average bitrate time-series|
|concurrent_plays|conviva.<br/>concurrent_plays|Concurrent plays time-series|
|connection_induced<br/>_rebuffering_ratio|conviva.<br/>connection_induced<br/>_rebuffering_ratio|Connection induced rebuffering ratio simple-series|
|connection_induced<br/>_rebuffering_ratio<br/>_timeseries|conviva.<br/>connection_induced<br/>_rebuffering_ratio<br/>_timeseries|Connection induced rebuffering ratio time-series|
|duration_connection<br/>_induced_rebuffering<br/>_ratio_distribution|conviva.<br/>duration_connection<br/>_induced_rebuffering<br/>_ratio_distribution|Duration vs. connection induced rebuffering ratio distribution label-series|
|exits_before<br/>_video_star|conviva.<br/>exits_before<br/>_video_start|Exits before video start time-series|
|ended_plays|conviva.<br/>ended_plays|Ended plays simple-series|
|ended_plays<br/>_timeseries|conviva.<br/>ended_plays<br/>_timeseries|Ended plays time-series|
|plays|conviva.<br/>plays|Plays time-series|
|play_bitrate<br/>_distribution|conviva.<br/>play_bitrate<br/>_distribution|Play bitrate distribution label-series|
|play_buffering<br/>_ratio_distribution|conviva.<br/>play_buffering<br/>_ratio_distribution|Play buffering ratio distribution label-series|
|play_connection<br/>_induced_rebuffering<br/>_ratio_distribution|conviva.<br/>play_connection<br/>_induced_rebuffering<br/>_ratio_distribution|Play connection induced rebuffering ratio distribution label-series|
|quality_summary|conviva.<br/>quality_summary|Quality summary label-series|
|rebuffered_plays|conviva.<br/>rebuffered_plays|Rebuffered plays time-series|
|rebuffering_ratio|conviva.<br/>rebuffering_ratio|Rebuffering ratio time-series|
|top_assets_15_mins|conviva.<br/>top_assets_15_mins|Top assets over last 15 minutes simple-table|
|top_assets_summary|conviva.<br/>top_assets_summary|Top assets summary label-series|
|video_playback<br/>_failures|conviva.<br/>video_playback<br/>_failures|Video playback failures simple-series|
|video_playback<br/>_failures_timeseries|conviva.<br/>video_playback<br/>_failures_timeseries|Video playback failures time-series|
|video_playback<br/>_failures_distribution|conviva.<br/>video_playback<br/>_failures_distribution|Video playback failures distribution label-series|
|video_restart<br/>_time|conviva.<br/>video_restart<br/>_time|Video restart time simple-series|
|video_restart<br/>_time_timeseries|conviva.<br/>video_restart<br/>_time_timeseries|Video restart time time-series|
|video_restart<br/>_time_distribution|conviva.<br/>video_restart_time<br/>_distribution|Video restart time distribution label-series|
|video_start<br/>_failures|conviva.<br/>video_start<br/>_failures|Video start failures time-series|
|video_start<br/>_failures_errornames|conviva.<br/>video_start<br/>_failures_errornames|Video start failures by error names simple-table|
|video_startup_time|conviva.<br/>video_startup_time|Video startup time label-series|
|quality_metriclens|conviva.<br/>quality_metriclens.<br/>total_attempts|Attempts|
||conviva.<br/>quality_metriclens.<br/>video_start<br/>_failures_percent|Video Start Failures(VSF) (%)|
||conviva.<br/>quality_metriclens.<br/>exits_before<br/>_video_start<br/>_percent|Exits Before Video Starts (EBVS) (%)|
||conviva.<br/>quality_metriclens.<br/>plays_percent|Plays (%)|
||conviva.<br/>quality_metriclens.<br/>video_startup<br/>_time_sec|Video Startup Time (sec)|
||conviva.<br/>quality_metriclens.<br/>rebuffering_ratio<br/>_percent|Rebuffering Ratio (%)|
||conviva.<br/>quality_metriclens.<br/>average_bitrate<br/>_kbps|Average Bitrate (bps). This metric can be returned in kbps with the ab_units=kbps parameter. Unless this parameter is specified, average bitrate is bps.|
||conviva.<br/>quality_metriclens.<br/>video_playback<br/>_failures_percent|Video Playback Failures (%)|
||conviva.<br/>quality_metriclens.<br/>ended_plays|Ended Plays|
||conviva.<br/>quality_metriclens.<br/>connection_induced<br/>_rebuffering_ratio<br/>_percent|Connection Induced ReBuffering Ratio (%)|
||conviva.<br/>quality_metriclens.<br/>video_restart_time|Video Restart Time|
|audience_metriclens|conviva.<br/>audience_metriclens.<br/>concurrent_plays|Concurrent Plays|
||conviva.<br/>audience_metriclens.<br/>plays|Plays|
||conviva.<br/>audience_metriclens.<br/>ended_plays|Ended Plays|
