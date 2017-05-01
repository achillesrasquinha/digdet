# imports - standard imports
import os
import json

# imports - compatibility imports
from flask import request, jsonify

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

    dict_    = response.todict()
    json_    = jsonify(dict_)

    return json_

@app.route(ServerConfig.URL.LANG)
def lang():
    path  = os.path.join(ServerConfig.Path.DATA, 'lang.json')

    with open(path, 'r') as f:
        data = json.load(f)

    json_ = jsonify(data)

    return json_
