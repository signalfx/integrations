# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_collectd.png) Tail collectd Plugin

Metadata associated with the Tail collectd plugin can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-tail-syslog">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/tail.c">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

### DESCRIPTION

From the <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:Tail">collectd wiki</a>:

The Tail plugin can be used to “tail” log files, i. e. follow them as tail -F does. Each line is given to one or more “matches” which test if the line is relevant for any statistics using a <a target="_blank" href="http://en.wikipedia.org/wiki/Regular_expression">POSIX extended regular expression</a>. So you could, for example, count the number of failed login attempts via SSH by using the following regular expression with the `/var/log/auth.log` logfile:

```
\<sshd[^:]*: Invalid user [^ ]+ from\>
```

But counting lines that match is only the simplest application of this plugin. Take, for example, a daemon that writes the current number of users to a file periodically. You could collect this information with a regular expression like this:

```
There are currently (\d+) users
```

As you can see the actual number of users is stored in the first "sub match". This value can then be used by collectd as a gauge value.

And there's even more: Per default, Exim logs the size of each email in its logfile. You can match this size and add all the values up. So you'll end up with a typical octet-counter which you can use with the ipt\_bytes type, for example. Such a regular expression would look like this:

```
\<S=(\d+)\>
```

This plugin is a generic plugin, i.e. it cannot work without configuration, because there is no reasonable default behavior. Please read the Plugin tail section of the collectd.conf(5) manual page for an in-depth description of the plugin's configuration.

##### “Following” files
To “follow” files, the Tail plugin does the following each interval:

1. Read and handle each line of an already opened file descriptor until the end of the file is reached.
2. Check if the file has been truncated. If so, seek to the beginning of the file and start processing the file from there.
3. Retrieve the inode number associated with the file name that should be followed. This number is compared to the inode of the currently open file descriptor.
4. If the inodes differ, the originally opened file has been moved or replaced. The file descriptor is closed and the file name is (re)opened.
5. If no file had been open in step 1 (usually only true on the first iteration), open the file name, seek to the end but do not handle any lines.

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

This plugin is automatically bundled with the <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd">SignalFx collectd agent</a>, but it is not enabled by default.


### CONFIGURATION

Please see the <a target="_blank" href="https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_tail">collectd wiki</a> for information on how to configure this plugin.

Additionally, some sample configurations can be found <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:Tail/Config">here</a>.

### CAVEATS

This plugin was created by the collectd community to satisfy “modest” log tailing use cases that typically involve monitoring at most a small handful of logs for matches with up to a couple dozen regular expressions in each log. (See <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:Tail/Config">here</a> for several examples). Its creators haven’t specifically noted any caveats related to its usage or performance, possibly due to the difficulty in doing so given the number of variables involved. It is reasonable to expect that at some point this plugin will have difficulty scaling under typical regex configuration once the number of logs it is tasked with monitoring increases into double digits, especially if the logs are very active.

### LICENSE

License for this plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/tail.c">in the header of the plugin</a>.
