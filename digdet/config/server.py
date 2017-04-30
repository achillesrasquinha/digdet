# imports - standard imports
import os

# imports - module imports
from digdet.config.base import BaseConfig

class ServerConfig(BaseConfig):
    HOST = '0.0.0.0'
    PORT = os.getenv('PORT', 5000)

    class URL(BaseConfig.URL):
        pass
