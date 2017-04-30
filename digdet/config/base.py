# imports - standard imports
import os
try:
    # Python 2
    from urlparse import urljoin
except ImportError:
    # Python 3
    from urllib.parse import urljoin

# imports - module imports
from digdet.util import pardir

class BaseConfig(object):
    NAME        = 'digdet'
    VERSION     = (0, 1, 0)
    ENVIRONMENT = 'development'

    class URL(object):
        BASE    = "/"
        DETECT  = "/api/detect"

    class Path(object):
        ROOT      = os.path.abspath(pardir(__file__, 2))
        TEMPLATES = os.path.join(ROOT, 'templates')
        ASSETS    = os.path.join(ROOT, 'assets')
