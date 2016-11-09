# flake8: noqa
from . import default_settings
from .web import blueprint
import logging

try: 
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())