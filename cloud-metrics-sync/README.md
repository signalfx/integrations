### Requirements
* Python 3.7+
* GCP credentials (if syncing GCP metrics)

### Installing
It's recommended to install in a [pyenv](https://github.com/pyenv/pyenv) and/or [virtualenv](https://virtualenv.pypa.io/)
environment.

```sh
pip install -r requirements.txt
```

### Running
If syncing GCP metrics you will need to set environment variables:

```sh
export GOOGLE_APPLICATION_CREDENTIALS=<credentials file>
export GCP_PROJECT_ID=<project id>
```

The project id doesn't appear to matter as long as it's valid and works with the credentials file.

See help for available options:

```sh
python -m cloudsync -h
```

### Updating

To add additional namespaces/services to sync add an entry to `DOCS` variable in the appropriate service file:

* [AWS](aws.py)
* [GCP](gcp.py)
* [Azure](azure.py)

Then run `python -m cloudsync -p <platform> sync` and commit the updated files.
