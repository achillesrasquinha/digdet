# imports - standard imports
import os
import json

# imports - third-party imports
from keras.models import model_from_json

# imports - module imports
from digdet.config.app import AppConfig

MNIST = 'mnist'

def load(name = MNIST):
    path  = os.path.join(AppConfig.Path.MODELS, name)

    with open(os.path.join(path, 'model.json')) as f:
        buffer_ = f.read()

    model = model_from_json(buffer_)
    model.load_weights(os.path.join(path, 'model.h5'))

    with open(os.path.join(path, 'config.json')) as f:
        config  = json.load(f)

    model.compile(**config)

    return model
