# This is the default settings module for a new django project.
# Based on the DAJNGO_RUNTIME_ENV, we choose which version of
# settings to use - by default the choice is between dev and prod

import os

env = os.getenv("DJANGO_RUNTIME_ENV")

if env == "dev":
	from .dev import *
elif env == "prod":
	from .prod import *
