try:
    from .local_settings import *

    print("Settings imported from local_settings")
except ImportError:
    print("Settings not imported")
