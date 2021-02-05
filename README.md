# SignalFx Integrations

Each directory in this repository specifies a different integration with Splunk Infrastructure Monitoring.
At a minimum, each directory must have the files README.md and meta.yaml. If the integration is associated with
a fixed set of metrics, add the file metrics.yaml. The following sections describe these files in more detail.

If you add a new integration, in meta.yaml set `useLegacyBuild: false`. Never use the legacy build for new integrations.

## Writing YAML multi-line text

By default, YAML text appears on a single line. Consider the following text:

`description: While you may see this metric in your organization, it is for Infrastructure Monitoring internal use only.`

The YAML processor displays the line as is, with a newline (`\n`) after the word "only".

To control wrapping or to use Markdown syntax in YAML text, add one of the following
characters after the YAML field name and colon delimiter. For example, use the
delimiter for a multi-line `description`:

```
description: >
    While you may see this metric in your organization,
    it is for Infrastructure Monitoring internal use only.
```

* `>` - For a block of text, this character strips out line breaks within the block and
        adds a single break at the end of the block.
* `|` - For a block of text, this character preserves line breaks and implements
        Markdown.
* Use `＞－` or `│－` if you don't want a blank line after the text block.

For more information, do an Internet search for "YAML multi-line".

## Meta.yaml

Each integration directory must have the file meta.yaml, which provides basic metadata
for the integration. Use the following fields:


| field name     | description                                                                                                          |
|:---------------|:---------------------------------------------------------------------------------------------------------------------|
| display\_name  | name that will display in the integration tile                                                                       |
| description    | short description of integration                                                                                     |
| project_url    | URL of 'metadata' directory. For example, `(https://github.com/signalfx/integrations/tree/master/<integration-foo>)` |
| code           | URL of code repository                                                                                               |
| featured       | flag 'true' to put integration in "Top Integrations" section but 'false' otherwise                                   |
| logo\_large    | URL of 300x300 pixel logo image                                                                                      |
| logo\_small    | URL of 150x150 pixel logo image                                                                                      |
| feature        | optional line to specify the feature associated with the integration                                                 |
| useLegacyBuild | If set to `false`, the Jinja (new) build templating system will be used                                              |


Example 1:

```
display_name: "AppDynamics Metrics Integration"
description: "AppDynamics metrics integration"
project_url: "https://github.com/signalfx/integrations/tree/master/appdynamics"
code: "https://github.com/signalfx/appd-integration"
featured: false
logo_large: "/images/repos/appdynamics/img/integrations_appdynamics%402x.png"
logo_small: "/images/repos/appdynamics/img/integrations_appdynamics.png"
feature: "<feature_name>"
```

Example 2:

```
browse_categories:
- Database
code: https://aws.amazon.com/rds/
data_signature: namespace:"AWS/RDS"
description: Monitor Amazon Relational Database Service (RDS) using SignalFx and AWS CloudWatch.
display_name: Amazon RDS
featured: false
in_app_categories:
- AWSservicesMonitored
logo_large: integration_awsrds.png
logo_small: integration_awsrds.png
project_url: https://github.com/signalfx/integrations/tree/master/aws-rds
useLegacyBuild: true
```

## metrics.yaml

To help users make sense of incoming data, add or edit metrics.yaml to describe each
metric and dimension that the integration emits, including the following:

* Metric name: For example, `sf.org.limit.hosts`
* Type: "counter", "gauge", or "cumulative_counter". For example, `type: gauge`
* Description of what it measures: For example,

```
  description: |
    Your contract specifies this limit for the number of MTS you can create per
    per minute. If you exceed this rate, Infrastructure Monitoring stops creating MTS.
```

## Sample dashboard(s)

To help users start with your integration, include a dashboard that users can import into their monitoring solution.
Infrastructure Monitoring provides extended trial accounts for plugin developers that you can use to develop your
dashboard. <a target="_blank" href="mailto:community@signalfx.com">Contact Infrastructure Monitoring to learn more</a>.

## New Template System

To help Infrastructure Monitoring teams and other contributors
control the text generated from this repo, including text in the integration tiles in the user interface
and text in the user documentation, the build system is based entirely on
that is based entirely on [Jinja templates](https://jinja.palletsprojects.com/en/2.11.x/templates/).

To enable the new template functionality for your particular integration, set `useLegacyBuild: false`
in your meta.yaml file.

The Jinja template for an integration is the file README.md.jinja in the integration directory.
The build process uses only that file.

The build process deserializes all *.yaml files in the integration directory and makes them available
to the template context as a variable. For example, metrics.yaml is available as `metrics` in the template.

Include the following line at the top of the file README.md.jinja:

`{% import "macros.jinja" as macros %}`

This macro statement imports the macro helpers defined in the Jinja system.
To learn more about Jinja macros, see the Jinja documentation section
[Macros](https://jinja.palletsprojects.com/en/2.11.x/templates/#macros).

To apply a Jinja template to an existing integration:

1. Create the file README.md.jinja in the integration directory. You can
   either create it from scratch or copy and rename a legacy README.md file.
2. Ensure that README.md.jinja has the content that you want to describe, because it's
   the single source for integration tiles in the user interface and user documentation.
3. Verify that README.md.jinja file starts with the line
   `{% import macros.jinja as macros %}`.
4. In the file meta.yaml file for the integration, set `useLegacyBuild: false` so that the build process uses
   the Jinja template by default.
5. Delete the file README.md if it exists.

If possible, include all steps of the template application process in a single commit or pull request to your
development branch. If you have `useLegacyBuild: true`, the build process ignores README.md.jinja or generates
unexpected results. Similarly, if you have README.md.jinja and README.md in the same directory, your pull requests might
generate file conflicts, because the build process merges all *.md files in your directory.

### Tile Tabs

To control tabs in the integration tiles in the user interface, use second-level headers (specified by "##" in the first two columns
of the header text) in `README.md.jinja`. The build process interprets a second-level header
as the title of a tab, and all the content between the header and the next second-level header (or end of file)
is displayed in the tab.

You can use first-level headers ("#") for text you want to display in user documentation. Otherwise,
text that's outside a second-level section in `README.md.jinja` doesn't display in the integration tiles in the
user interface.

### Differentiate between tile content and documentation content

To control where content appears, use [Jinja conditional statements](https://jinja.palletsprojects.com/en/2.11.x/templates/#if)
and the `target` macro variable. To build integration tiles for the user interface, use
`target: tile`. To build user documentation, use `target: docs`.

Build scripts write the output for `target: tile` to the `integrations` repository, while build scripts for `target: docs` write
output to the `product-docs` repository. For example, the "if" statements in the following example write  their content to the
`integrations` repository but not the `product-docs` repository.

Conditional statements must be paired. Close the `if` statement with an `endif` statement:

**Conditional text example**

```
{% if target ﹦﹦ "tile" -%}

### Built-in dashboards

* **Apache Web Servers**: Overview of data from all Apache webserver instances.

[<img src='./img/dashboard_apache_webservers.png' width=200px>](./img/dashboard_apache_webservers.png)

* **Apache Web Server**: Focus on a single Apache webserver instance.

[<img src='./img/dashboard_apache_webserver.png' width=200px>](./img/dashboard_apache_webserver.png)

{%- endif %}
```

## Test Tiles locally

The integration tiles used in the user interface come from a Javascript module that uses
the content in the `integrations` repository. To build the module, use the `./build` script in
the root of the repository, as follows:

1. Verify that you have Python 3 installed on your machine.
2. In your terminal application, navigate to the root of the `integrations` repository.
3. Run the following command:

   `pip3 install --user -r ./requirements.txt`

4. Run the following command:

   `./build`

If the build completes successfully, it displays a command that you can run to
serve the JS module and associated images using a local HTTP server.

You can then run the user interface with the following content in the
`local.config.js` file in the root of the SignalView repository:

```javascript
module.exports = {
    integrationsDocsUrl: "http://localhost:3005/"
}
```

Run your local SignalView instance to preview the latest build of this repository.