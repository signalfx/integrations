# SignalFx Integrations

Each directory in this repo represents a different integration with SignalFx.
At a bare minimum each integration directory needs a `README.md` and a
`meta.yaml` (see below).  If the integration has a fixed set of metrics that
are associated with it, you should also have a `metrics.yaml` file.

For any **new integrations**, you should set `useLegacyBuild: false` in the
`meta.yaml` (never use the legacy build for new stuff).

## Meta.yaml

Each integration requires a `meta.yaml` file that provides basic metadata
describing the integration.  The fields in the meta.yaml file are:

| field name | description |
|------------|-------------|
| display\_name | name that will display in the integration tile|
| description | short description of integration |
| project\_url | URL of 'metadata' directory (`https://github.com/signalfx/integrations/tree/master/[integration-foo]`)|
| code | URL of code repository |
| featured | flag 'true' to put integration in "Top Integrations" section but 'false' otherwise |
| logo\_large | URL of 300x300 pixel logo image |
| logo\_small | URL of 150x150 pixel logo image |
| feature | optional line to specify the feature associated with the integration |
| useLegacyBuild | If set to `false`, the Jinja (new) build templating system will be used |


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

To help users make sense of their new data, provide documentation of each
metric and dimension that the integration emits, including name, type (counter,
gauge, or cumulative counter) and description of what it measures.

This should go in the file called `metrics.yaml` in the integration directory.

## Sample dashboard(s)

Include a dashboard for your users to import into their monitoring solution, so that they can get instant value out of running your integration. SignalFx provides extended trial accounts for plugin developers that you can use to develop your dashboard. <a target="_blank" href="mailto:community@signalfx.com">Contact us to learn more</a>.

## New Template System

To make it easier to control the docs generated from this repo (the integration
tiles in app and on the product docs site), there is now a new build system
that is based entirely on [Jinja templates](https://jinja.palletsprojects.com/en/2.11.x/templates/)
for maximum control by the documentation team and other contributors.

For new template functionality to be enabled for a particular integration, the `useLegacyBuild` flag
in the integration's `meta.yaml` file must be set to `false`.

The Jinja template for each integration is the `README.md.jinja` file in that
integration directory.  That file must be present and named exactly that.  No
other markdown files in the directory will be considered by the build process.

All `*.yaml` files in the integration directory will be deserialized and made
available in the context of the template as a variable with the base name of
the yaml file.  For example, `metrics.yaml` is available as `metrics` in the
template.

All rendered templates will have the [macro
helpers](https://jinja.palletsprojects.com/en/2.11.x/templates/#macros) defined
in `macros.jinja` available for use.  The template just needs to have the line 
`{% import "macros.jinja" as macros %}` somewhere towards the top.

To apply the Jinja template to an existing integration:
1. Create a README.md.jinja file in the directory for that integration.
2. Ensure that the README.md.jinja file has the content about the integration that you intend to document, because it will be 
the single source for both tiles and product-docs repos. Automated scripts render the template for `tile` in the Integrations repository and `docs` in the product docs repository.
3. Verify that the README.md.jinja file includes the line 
`{% import "macros.jinja" as macros %}` above your original content.
4. In the meta.yaml file for the integration, set the 'useLegacyBuild' flag to 'false' so that a build with the Jinja template
becomes default behavior.

It may be convenient to include all steps of the template application process in a single commit to whatever branch you
are using for development, so as to reduce the possibility of lag between what you intend and what is actually built. If the 'useLegacyBuild' flag is set to 'true', then the build process ignores your jinja file or generates unexpected results.

### Tile Tabs
The tabs in the integration tiles in the web app (SignalView) are determined by
the presence of `##` (second) level headers in the `README.md.jinja` template.
Any header at that level will be a tab and all content under it until the next
second level header (or the end of the file) will be under that tab.  You
should not use first level headers (`#`) except when sending the docs to
product-docs.  Anything not inside a `##` header in the `README.md.jinja` file
will be ignored by SignalView when rendering the tiles.

### Differentiating between tiles and docs
To differentiate content based on where the docs are being rendered for, you
can use [conditional statements in
Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/#if) along with
the `target` variable. For Web App Tile builds, the template will have a
context variable `target` with a value of `tile`. For product docs builds, the
`target` variable will be equal to `docs`.


## Local Testing of Tiles

The web app tiles are sourced from a Javascript module that is generated from
the content in this repo.  That module is built with the `./build` script in
the root of this repo.  To run this script, first ensure you have Python 3
installed on your machine.  Then run:

`pip3 install --user -r ./requirements.txt`

from the root of this repo. Then run:

`./build`

If all completes successfully, you will receive a command that you can run to
serve this JS module and associated images via a local HTTP server.  You can
then run SignalView (the web app) with the following content in the
`local.config.js` file in the root of the SignalView repo:

```js
module.exports = {
    integrationsDocsUrl: "http://localhost:3005/",
}
```

Then you can access the local SignalView instance and preview the latest build
of this repo.
