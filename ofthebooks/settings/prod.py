# Prod Settings

import os
import dj_database_url

from .common import *

ALLOWED_HOSTS = ['*']

DATABASES = {
	'default': dj_database_url.config()
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
