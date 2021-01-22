
live = False
beta = False

try:
    from .local import *
except ImportError:
    live = True

if live and beta:
    from .beta import *
elif live:
    from .production import *