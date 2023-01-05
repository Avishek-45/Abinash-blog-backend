import os
from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

if DEBUG == 'True':
    from .local import *
else:
    from .production import *