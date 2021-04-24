from .base import *


SECRET_KEY = ''

ALLOWED_HOSTS = ['www.127.0.0.1', '127.0.0.1'] 

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
