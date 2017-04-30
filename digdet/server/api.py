# imports - compatibility imports
from flask import request

# imports - module imports
from digdet.config.server import ServerConfig
from digdet.server.app import app
from digdet.server.response import Response
from digdet.util import b64_to_image

import digdet

@app.route(ServerConfig.URL.DETECT, methods = ['POST'])
def detect():
    response = Response()

    b64str   = request.form['image']
    image    = b64_to_image(b64str)

    regions  = digdet.detect(image)

    response.set_data(regions)

    json_    = response.toJSON()

    return json_
