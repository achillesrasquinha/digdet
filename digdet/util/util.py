# imports - standard imports
import os
import io
import collections
import base64

# imports - third-party imports
from PIL import Image
import cv2

class Version(object):
	def __init__(self, major = 0, minor = 0, patch = 0):
		self.major = int(major)
		self.minor = int(minor)
		self.patch = int(patch)

	def __str__(self):
		string = '.'.join([self.major, self.minor, self.patch])

		return string

def get_version_str(version):
	string = '.'.join(map(str, version))

	return string

def assign_if_none(obj, value):
	if obj is None:
		obj = value

	return obj

def pardir(path, up = 1):
    for i in range(up):
        path = os.path.dirname(path)

    return path

def autodict():
	dict_ = collections.defaultdict(autodict)

	return dict_

def uuid_to_str(uuid):
	string = str(uuid)
	string = string.replace('-', '')

	return string

def b64_to_image(b64str):	
	decode = base64.b64decode(b64str)
	bytes_ = io.BytesIO(decode)

	image  = Image.open(bytes_)

	return image

def get_cv_version():
	version = cv2.__version__
	splits  = version.split('.')

	version = Version(splits[0], splits[1], splits[2])

	return version

def area_rect(rect):
	x, y, w, h = rect

	return w * h
