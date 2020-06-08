# ![](./img/integration_googlebigquery.png) Google BigQuery

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

## DESCRIPTION

To monitor Google BigQuery, integrate SignalFx with [Google Cloud Platform](https://docs.signalfx.com/en/latest/integrations/google-cloud-platform.html#connect-to-gcp).

## FEATURES

### Built-in Dashboards

- **BigQuery Overview** - Overview of project-level metrics for Google BigQuery.

  [<img src='./img/google_bigquery.png' width=200px>](./img/google_bigquery.png)


## INSTALLATION

To access this integration, [connect to Google Cloud Platform](https://docs.signalfx.com/en/latest/integrations/google-cloud-platform.html#connect-to-gcp).

## USAGE

### Interpreting Built-in Dashboards

**BigQuery Overview**

- **Queries Count** - Number of inflight queries.

- **Queries Trend** - Shows the trend of number of inflight queries.

- **Scanned Bytes / min** - Number of bytes scanned per minute.

- **Average Execution Time** - Distribution of queries execution times in seconds.

- **Slots Allocated versus Slots Available** - Number of BigQuery slots currently allocated for the project versus total number of BigQuery slots available for the project.

- **Scanned Bytes Billed per minute** - Amount of scanned bytes billed per minute.

- **Top Uploaded Bytes Billed per Table** - Tables with top 5 uploaded bytes billed per minute.

- **Top Stored Bytes per Table** - Tables with top 5 stored bytes.

- **Top Uploaded Bytes per Table** - Tables with top 5 uploaded bytes.

- **Table Count** - Total number of tables in the project.

- **Rows Uploaded / min per Table** - List number of rows uploaded per min aggregated by table.

## METRICS

For more information about the metrics emitted by Google BigQuery, visit the service's metric page at <a target="_blank" href="https://cloud.google.com/monitoring/api/metrics#gcp-bigquery">https://cloud.google.com/monitoring/api/metrics#gcp-bigquery</a>

#### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
