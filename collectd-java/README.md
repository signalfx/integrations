---
title: Java collectd Plugin
brief: Java plugin for collectd.
---

#![](https://github.com/signalfx/Integrations/blob/master/collectd-java/img/integrations_jmx.png) Java collectd Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From the [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Java):

The Java plugin embeds a Java virtual machine (JVM) into collectd and exposes the application programming interface (API) to Java programs. This allows to write own plugins in the popular language, which are then loaded and executed by the daemon without the need to start a new process and JVM every few seconds. Java classes written for the Java plugin are therefore more powerful and efficient than scripts executed by the Exec plugin.


The JavaDoc documentation of the API is available.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software  | Version        |
|-----------|----------------|
| collectd  | 4.7+ |

### INSTALLATION

This plugin is included with [SignalFx collectd](https://github.com/signalfx/Integrations/tree/master/collectd).

### CONFIGURATION

From the [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Java):

The Java plugin makes it possible to write extensions for collectd in Java. This section only discusses the syntax and semantic of the configuration options. For more in-depth information on the Java plugin, please read [collectd-java(5)](https://collectd.org/documentation/manpages/collectd-java.5.shtml).

Synopsis:

```
 <Plugin "java">
   JVMArg "-verbose:jni"
   JVMArg "-Djava.class.path=/opt/collectd/lib/collectd/bindings/java"
   LoadPlugin "org.collectd.java.Foobar"
   <Plugin "org.collectd.java.Foobar">
     # To be parsed by the plugin
   </Plugin>
 </Plugin>
```

Available configuration options:

**JVMArg _Argument_**

 Argument that is to be passed to the Java Virtual Machine (JVM). This works exactly the way the arguments to the java binary on the command line work. Execute `java--help` for details.

 Please note that all these options must appear before (i. e. above) any other options! When another option is found, the JVM will be started and later options will have to be ignored!

**LoadPlugin _JavaClass_**

 Instantiates a new JavaClass object. The constructor of this object very likely then registers one or more callback methods with the server.

 See collectd-java(5) for details.

 When the first such option is found, the virtual machine (JVM) is created. This means that all JVMArg options must appear before (i. e. above) all LoadPlugin options!

**Plugin _Name_**

 The entire block is passed to the Java plugin as an org.collectd.api.OConfigItem object.

 For this to work, the plugin has to register a configuration callback first, see collectd-java(5)/"config callback". This means, that the Plugin block must appear after the appropriate LoadPlugin block. Also note, that Name depends on the (Java) plugin registering the callback and is completely independent from the JavaClass argument passed to LoadPlugin.

### USAGE

The Java collectd plugin is the swiss army knife of collectd for Java applications. For specific useage details you can take a look at some of the common Java apps that are used with collectd:

* [cassandra](https://github.com/signalfx/Integrations/tree/master/collectd-cassandra)
* [kafka](https://github.com/signalfx/Integrations/tree/master/collectd-kafka)

### METRICS

The metrics for the Java collectd plugin will depend on what is generated and passed from the java application for which it is configured.

### LICENSE

License for this plugin can be found [in the header of the plugin](https://github.com/signalfx/collectd/blob/master/src/java.c)
