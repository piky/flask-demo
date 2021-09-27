import os
import logging as log

# Log settings
LOG_LEVEL = os.environ.get("LOG_LEVEL", "warning").upper()

log.basicConfig(level=LOG_LEVEL)

# Database authentication settings
DB_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")
