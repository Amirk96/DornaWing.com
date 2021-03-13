from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = '-*8^toybn#ywd$1j2(t+_94zcd6yl3so7notow7orjr#(h7=)+'


DEBUG = True

try:
    from .local import *
except ImportError:
    pass