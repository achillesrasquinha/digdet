# imports - third-party imports
from flask import render_template

# imports - module imports
from digdet.config.server import ServerConfig
from digdet.server.app import app

@app.route(ServerConfig.URL.BASE)
def index():
    template = render_template('pages/index.html')

    return template
