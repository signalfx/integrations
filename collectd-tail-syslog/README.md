---
title: Tail collectd Plugin
brief: Tail plugin for collectd.
---

# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_collectd.png) Tail collectd Plugin

_This is a directory consolidate all the metadata associated with the Tail collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/tail.c)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From the [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Tail):

The Tail plugin can be used to “tail” log files, i. e. follow them as tail -F does. Each line is given to one or more “matches” which test if the line is relevant for any statistics using a [POSIX extended regular expression](http://en.wikipedia.org/wiki/Regular_expression). So you could, for example, count the number of failed login attempts via SSH by using the following regular expression with the `/var/log/auth.log` logfile:

```
\<sshd[^:]*: Invalid user [^ ]+ from\>
```

But counting lines that match is only the simplest application of this plugin. Take, for example, a daemon that writes the current number of users to a file periodically. You could collect this information with a regular expression like this:

```
There are currently (\d+) users
```

As you can see the actual number of users is stored in the first "sub match". This value can then be used by collectd as a gauge value.

And there's even more: Per default, Exim logs the size of each email in its logfile. You can match this size and add all the values up. So you'll end up with a typical octet-counter which you can use with the ipt_bytes type, for example. Such a regular expression would look like this:

```
\<S=(\d+)\>
```

This plugin is a generic plugin, i.e. it cannot work without configuration, because there is no reasonable default behavior. Please read the Plugin tail section of the collectd.conf(5) manual page for an in-depth description of the plugin's configuration.

##### “Following” files
To “follow” files, the Tail plugin does the following each interval:

1. Read and handle each line of an already opened file descriptor until the end of the file is reached.
1. Check if the file has been truncated. If so, seek to the beginning of the file and start processing the file from there.
1. Retrieve the inode number associated with the file name that should be followed. This number is compared to the inode of the currently open file descriptor.
1. If the inodes differ, the originally opened file has been moved or replaced. The file descriptor is closed and the file name is (re)opened.
1. If no file had been open in step 1 (usually only true on the first iteration), open the file name, seek to the end but do not handle any lines.

To understand what's going on completely, you need to have a basic understanding of UNIX file systems. Especially: An inode is a number that determines the position of data on the disk (or whatever storage medium is in use). It's similar to an IP address, for example. A file name is basically a human readable name for an inode, similar to a domain name. A file descriptor is the representation of an opened file to a running program. To complete the analogy, it's similar to a TCP connection.

Once a file is opened (a file descriptor has been created), changes to the file name no longer affect the the running program directly. The file name can be removed or renamed, but since it is only an alias for an inode, the running program won't notice. By the way: This is why you have to notify some daemons when “rotating” the log file. [collectd's LogFile plugin](https://collectd.org/wiki/index.php/Plugin:LogFile) doesn't keep the file descriptor open, though. (Analogy: Once a TCP connection is established, changes to the DNS won't be noticed.)

Because changes to the file name aren't noticed automatically, the inode currently open is compared to the (newly looked up) inode the file name points to. If they differ, the file name now points to a new piece of data on the disk. We then assume that the file has been rotated, open the new file name and start reading from the beginning. (Analogy: Re-resolve the host name and compare IP addresses.)

Last but not least: In the previous interval, we have read to the end of the file. If the file has been shortened in the meantime, our file descriptor will now point to an undefined void somewhere after the file. We'll assume that the file has been truncated to length zero. Some daemons do this rather than change the file name and create a new file with the old name. The Tail plugin will therefore start processing this file from the beginning.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd |  4.4+  |

### INSTALLATION

Installation and initial configuration options are available as part of the [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd). 


### CONFIGURATION

From [collectd wiki](https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_tail):

> The tail plugin follows logfiles, just like tail(1) does, parses each line and dispatches found values. What is matched can be configured by the user using (extended) regular expressions, as described in regex(7).
> ```
  <Plugin "tail">
    <File "/var/log/exim4/mainlog">
      Instance "exim"
      Interval 60
      <Match>
        Regex "S=([1-9][0-9]*)"
        DSType "CounterAdd"
        Type "ipt_bytes"
        Instance "total"
      </Match>
      <Match>
        Regex "\\<R=local_user\\>"
        ExcludeRegex "\\<R=local_user\\>.*mail_spool defer"
        DSType "CounterInc"
        Type "counter"
        Instance "local_user"
      </Match>
    </File>
  </Plugin>
```

> The config consists of one or more **_File_** blocks, each of which configures one logfile to parse. Within each **_File_** block, there are one or more **_Match_** blocks, which configure a regular expression to search for.

> The Instance option in the **_File_** block may be used to set the plugin instance. So in the above example the plugin name tail-foo would be used. This plugin instance is for all **_Match_** blocks that follow it, until the next **_Instance_** option. This way you can extract several plugin instances from one logfile, handy when parsing syslog and the like.

> The **_Interval_** option allows you to define the length of time between reads. If this is not set, the default Interval will be used.

> Each **_Match_** block has the following options to describe how the match should be performed:

| Configuration Option | Type | Definition |
|----------------------|------|------------|
|Regex| regex|Sets the regular expression to use for matching against a line. The first subexpression has to match something that can be turned into a number by strtoll(3) or strtod(3), depending on the value of CounterAdd, see below. Because extended regular expressions are used, you do not need to use backslashes for subexpressions! If in doubt, please consult regex(7). Due to collectd's config parsing you need to escape backslashes, though. So if you want to match literal parentheses you need to do the following:<ui><li>`Regex "SPAM \\(Score: (-?[0-9]+\\.[0-9]+)\\)"`</li></ui>|
|ExcludeRegex| regex| Sets an optional regular expression to use for excluding lines from the match. An example which excludes all connections from localhost from the match:<ui><li>`ExcludeRegex "127\\.0\\.0\\.1"`</li></ui>|
|DSType |Type|Sets how the values are cumulated. Type is one of:<ui><li>`GaugeAverage`: Calculate the average.</li><li>`GaugeMin`: Use the smallest number only.<?li><li>`GaugeMax`: Use the greatest number only.</li><li>`GaugeLast`: Use the last number found.</li><li>`CounterSet`</li><li>`DeriveSet`</li><li>`AbsoluteSet`: The matched number is a counter. Simply sets the internal counter to this value. Variants exist for `COUNTER`, `DERIVE`, and `ABSOLUTE` data sources.</li><li>`GaugeAdd`</li><li>`CounterAdd`</li><li>`DeriveAdd`: Add the matched value to the internal counter. In case of `DeriveAdd`, the matched number may be negative, which will effectively subtract from the internal counter.</li><li>`GaugeInc`</li><li>`CounterInc`</li><li>`DeriveInc`: Increase the internal counter by one. These DSType are the only ones that do not use the matched subexpression, but simply count the number of matched lines. Thus, you may use a regular expression without submatch in this case. </li></ui>As you'd expect the _Gauge_ types interpret the submatch as a floating point number, using _strtod(3)_. The Counter* and AbsoluteSet types interpret the submatch as an unsigned integer using _strtoull(3)_. The _Derive_ types interpret the submatch as a signed integer using _strtoll(3)_. CounterInc and DeriveInc do not use the submatch at all and it may be omitted in this case.|
|Type |Type|Sets the type used to dispatch this value. Detailed information about types and their configuration can be found in types.db(5).|
|Instance |TypeInstance|This optional setting sets the type instance to use.|

### USAGE

>This section contains information about how best to monitor the software in question, using the data from this plugin. In this section, the plugin author shares experience and expertise with the software to be monitored, for the benefit of users of the plugin. This section includes:
>
>- Important conditions to watch out for in the software
>- Common failure modes, and the values of metrics that will allow the user to spot them
>- Chart images demonstrating each important condition or failure mode

This plugin is an example that emits values on its own, and does not connect to software. It emits a repeating sine wave in the metric gauge.sine. The metric should look like this:

![Example chart showing gauge.sine](http://fixme)

The following conditions may be cause for concern:

*You see a straight line instead of a curve.*

This may indicate a period of missing data points. In the example chart shown above, some data points are missing between 16:40 and 16:41, and SignalFx is interpolating a straight line through the gap.

### METRICS

>This section refers to the metrics documentation found in the `/docs` subdirectory. See [`/docs/README.md`](././docs/readme.md) for formatting instructions.

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

License for this plugin can be found [in the header of the plugin](https://github.com/signalfx/collectd/blob/master/src/tail.c)
