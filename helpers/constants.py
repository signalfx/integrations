# Skip certain dirs from github repo
dirs_to_skip = set(['example',
                    'signalfx-agent',
                    '.git',
                    'heka-filter-signalfx',
                    'telegraf',
                    'collectd-iostat',
                    'collectd-vmstat',
                    'collectd-tail-syslog',
                    'collectd',
                    'gitlab',
                    'customurl',
                    'aws-eks',
                    'metricproxy',
                    'splunk',
                    'aws-kinesis-analytics',
                    'cloud-metrics-sync'])

# Skip anything other than metric docs in docs dir
docs_to_skip = set(['readme.md', 'docs-temp.md'])
rtd_base_url = 'https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.'
