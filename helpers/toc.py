toc_sam = [
    # {
    #     'name': 'header',
    #     'content': 'README.md',
    #     'fingerprints': {
    #         'starter': None,
    #         'stopper': '### '
    #     }
    # },
    {
        "name": "description",
        "content": "SMART_AGENT_MONITOR.md",
        "fingerprints": {"starter": "## Description", "stopper": "## "},
    },
    {
        "name": "requirements and dependencies",
        "content": "README.md",
        "fingerprints": {"starter": "### REQUIREMENTS AND DEPENDENCIES", "stopper": "### "},
    },
    {
        "name": "installation",
        "content": "SMART_AGENT_MONITOR.md",
        "fingerprints": {
            "starter": "### INSTALLATION",
            "stopper": "<!--- GENERATED BY gomplate from scripts/docs/monitor-page.md.tmpl --->",
        },
    },
    {
        "name": "configuration",
        "content": "SMART_AGENT_MONITOR.md",
        "fingerprints": {"starter": "## Configuration", "stopper": "## "},
    },
    {"name": "usage", "content": "README.md", "fingerprints": {"starter": "### USAGE", "stopper": "### "}},
    {
        "name": "metrics",
        "content": "SMART_AGENT_MONITOR.md",
        "fingerprints": {"starter": "## Metrics", "stopper": "## "},
    },
]

toc_non_sam = [
    # {
    #     'name': 'header',
    #     'content': 'README.md',
    #     'fingerprints': {
    #         'starter': None,
    #         'stopper': '### DESCRIPTION'
    #     }
    # },
    {"name": "description", "content": "README.md", "fingerprints": {"starter": "### DESCRIPTION", "stopper": "### "}},
    {
        "name": "requirements and dependencies",
        "content": "README.md",
        "fingerprints": {"starter": "### REQUIREMENTS AND DEPENDENCIES", "stopper": "### "},
    },
    {
        "name": "installation",
        "content": "README.md",
        "fingerprints": {"starter": "### INSTALLATION", "stopper": "### "},
    },
    {
        "name": "configuration",
        "content": "README.md",
        "fingerprints": {"starter": "### CONFIGURATION", "stopper": "### "},
    },
    {"name": "usage", "content": "README.md", "fingerprints": {"starter": "### USAGE", "stopper": "### "}},
    {"name": "metrics", "content": "README.md", "fingerprints": {"starter": "### METRICS", "stopper": "### "}},
]