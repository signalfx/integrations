# Skip certain dirs from github repo
DIRS_TO_SKIP = set(
    [
        "example",
        "signalfx-agent",
        ".git",
        "heka-filter-signalfx",
        "telegraf",
        "collectd-iostat",
        "java",
        "collectd-vmstat",
        "collectd-tail-syslog",
        "collectd",
        "gitlab",
        "customurl",
        "aws-eks",
        "metricproxy",
        "splunk",
        "aws-kinesis-analytics",
        "cloud-metrics-sync",
    ]
)

# Skip anything other than metric docs in docs dir
DOCS_TO_SKIP = set(["readme.md", "docs-temp.md"])
RTD_BASE_URL = "https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations."

MONITOR_DOC_BASE_URL = "https://docs.signalfx.com/en/latest/integrations/agent/monitors/"
