---
title: GenericJMX Plugin
brief: GenericJMX plugin for collectd.
---


# GenericJMX Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:GenericJMX):

The GenericJMX plugin reads Managed Beans (MBeans) from an MBeanServer using JMX. The plugin is written in Java and requires the [Java plugin](https://github.com/signalfx/Integrations/tree/master/collectd-java) to function.

The Java Management Extensions (JMX) is a generic framework to provide and query various management information. The interface is used by the Java Virtual Machine (JVM) to provide information about the memory used, threads and so on. These basic performance values can therefore be collected for every Java process without any support in the Java process itself.

Advanced Java processes can use the JMX interface to provide performance information themselves. The Apache Tomcat application server, for example, provides information on the number of requests processed, the number of bytes sent, processing time, and thread counts.

### REQUIREMENTS AND DEPENDENCIES

- collectd 4.8+
- Java 2.6+

### INSTALLATION

Follow these steps to install this plugin:

1. Download this repository to your local machine.
2. Download the sample configuration file from signalfx-integrations/helloworld/.
3. Modify the sample configuration file to contain values that make sense for your environment, as described [below](#configuration).
4. Add the following line to collectd.conf, replacing the path with the path to the sample configuration file you downloaded in step 2:

  ```
  include '/path/to/10-configfile.conf'
  ```
5. Restart collectd.

### CONFIGURATION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:GenericJMX):

The configuration of the GenericJMX plugin consists of two blocks:
* _MBean blocks_ that define a mapping of MBean attributes to the “types” used by collectd
* _Connection blocks_ which define the parameters needed to connect to an MBeanServer and what data to collect.

The configuration of the SNMP plugin is similar in nature, in case you know it.

**MBean blocks**

_MBean blocks_ specify what data is retrieved from MBeans and how that data is mapped on the collectd data types. The block requires one string argument, a name. This name is used in the _Connection blocks_ (see below) to refer to a specific MBean block. Therefore, the names must be unique.
The following options are recognized within MBean blocks:

* **ObjectName _pattern_**
 Sets the pattern which is used to retrieve MBeans from the MBeanServer. If more than one MBean is returned you should use the InstanceFrom option (see below) to make the [identifiers](https://collectd.org/wiki/index.php/Identifier) unique.

 See also: [ObjectName](http://java.sun.com/javase/6/docs/api/javax/management/ObjectName.html).
* **InstancePrefix _prefix_**

 Prefixes the generated plugin instance with prefix. (optional)
* **InstanceFrom _property_**

 The object names used by JMX to identify MBeans include so called “properties” which are basically key-value-pairs. If the given object name is not unique and multiple MBeans are returned, the values of those properties usually differ. You can use this option to build the plugin instance from the appropriate property values. This option is optional and may be repeated to generate the plugin instance from multiple property values.
* **`<value />` blocks**

 The value blocks map one or more attributes of an MBean to a [value list](https://collectd.org/wiki/index.php/Value_list) in _collectd_. There must be at least one Value block within each MBean block.

* **Type _type_**

 Sets the data set used within collectd to handle the values of the MBean attribute.
* **InstancePrefix _prefix_**

 Works like the option of the same name directly beneath the MBean block, but sets the type instance instead. (optional)
* **InstanceFrom _prefix_**

 Works like the option of the same name directly beneath the MBean block, but sets the type instance instead. (optional)
* **Table true|false**

 Set this to true if the returned attribute is a _composite_ type. If set to true, the keys within the composite type is appended to the type instance.
* **Attribute _path_**

 Sets the name of the attribute from which to read the value. You can access the keys of composite types by using a dot to concatenate the key name to the attribute name. For example: “attrib0.key42”. If Table is set to true path must point to a composite type, otherwise it must point to a numeric type.

**Connection blocks**

 Connection blocks specify how to connect to an MBeanServer and what data to retrieve. The following configuration options are available:
* **Host _name_**

 Host name used when dispatching the values to collectd. See [naming schema](https://collectd.org/wiki/index.php/Naming_schema) for details. The option sets this field only, it is not used to connect to anything and doesn't need to be a real, resolvable name.
* **ServiceURL _URL_**

 Specifies how the MBeanServer can be reached. Any string accepted by the JMXServiceURL is valid.
 See also: [JMXServiceURL](http://java.sun.com/javase/6/docs/api/javax/management/remote/JMXServiceURL.html)
* **User _name_**

 Use name to authenticate to the server. If not configured, “monitorRole” will be used.
* **Password _password_**

 Use password to authenticate to the server. If not given, unauthenticated access is used.
* **InstancePrefix _prefix_**

 Prefixes the generated plugin instance with prefix. If a second InstancePrefix is specified in a referenced MBean block, the prefix specified in the Connection block will appear at the beginning of the plugin instance, the prefix specified in the MBean block will be appended to it. (optional, since version 5.0)
* **Collect _mbean_ _ _block_ _ _name_**

 Configures which of the _MBean_ blocks to use with this connection. May be repeated to collect multiple _MBeans_ from this server.

### USAGE



### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This plugin is released under the MIT license. See [header in plugin](https://github.com/collectd/collectd/blob/master/bindings/java/org/collectd/java/GenericJMX.java) for more details.
