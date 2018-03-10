try:
    from .local_settings import *

except ImportError:
    print("Settings not imported")
