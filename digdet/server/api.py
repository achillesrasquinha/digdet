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

    imgstr   = request.form.get('image', None)
    if imgstr is None:
        response.set_error(Response.ERROR.UNPROCESSABLE_ENTITY)
    else:
        glyph   = request.form.getlist('glyph[]', ["la"])
        image   = b64_to_image(imgstr)

        regions = digdet.detect(image, glyph)

        response.set_data(regions)

    dict_    = response.todict()
    json_    = jsonify(dict_)

    return json_, response.code

@app.route(ServerConfig.URL.GLYPH)
def glyph():
    path  = os.path.join(ServerConfig.Path.DATA, 'glyph.json')

    with open(path, 'r') as f:
        data = json.load(f)

    json_ = jsonify(data)

    return json_
