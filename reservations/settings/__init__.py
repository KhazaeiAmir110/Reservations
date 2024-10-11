"""
try to activate local settings. if it failed, we
load the production environment.
"""

try:
    from reservations.settings.local import *
except ImportError:
    from reservations.settings.production import *
