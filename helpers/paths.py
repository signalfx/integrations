import os
from pathlib import Path

BASE_DIR = (Path(__file__).parent / "..").resolve()
INTEGRATIONS_PATH = BASE_DIR
if os.environ.get("INTEGRATIONS_REPO"):
    INTEGRATIONS_PATH = Path(os.environ["INTEGRATIONS_REPO"])

INTEGRATIONS_AGENT_DOC_PATH = INTEGRATIONS_PATH / "signalfx-agent/agent_docs"

PRODUCT_DOCS_PATH = (BASE_DIR / "../product-docs").resolve()
if os.environ.get("PRODUCT_DOCS_REPO"):
    PRODUCT_DOCS_PATH = Path(os.environ["PRODUCT_DOCS_REPO"])

OUTPUT_AGENT_DOC_PATH = PRODUCT_DOCS_PATH / "integrations/agent/"
OUTPUT_IMAGE_PATH = PRODUCT_DOCS_PATH / "_images/images-integrations/integrations-reference"
OUTPUT_DOC_PATH = PRODUCT_DOCS_PATH / "integrations/integrations-reference"
