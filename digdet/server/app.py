# imports - third-party imports
from flask import Flask

# imports - module imports
from digdet.config.server import ServerConfig

app = Flask(__name__,
    template_folder = ServerConfig.Path.TEMPLATES,
    static_folder   = ServerConfig.Path.ASSETS,
)
