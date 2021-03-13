from .base import *


SECRET_KEY = '-*8^toybn#ywd$1j2(t+_94zcd6yl3so7notow7orjr#(h7=)+'

ALLOWED_HOSTS = ['www.127.0.0.1', '127.0.0.1'] 

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
