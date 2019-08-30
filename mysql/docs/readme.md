---
title: MySQL Metrics
brief: Metrics collected from MySQL Server.
---
### MySQL Metrics

Use the `mysql` collectd plugin to collect metrics about MySQL Server.  Configure and enable it as documented in [collectd plugin manual](https://collectd.org/wiki/index.php/Plugin:MySQL).

The metrics reported by collectd generally come from `show status` command in MySQL command prompt. The [MySQL official documentation](https://dev.mysql.com/doc/refman/5.0/en/server-status-variables.html) is an excellent resource for MySQL metrics.

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  3.6 or later  |
