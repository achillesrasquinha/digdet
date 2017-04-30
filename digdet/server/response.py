# imports - standard imports
import json
import uuid

# imports - module imports
from digdet.config.server import ServerConfig
from digdet.util import (
	get_version_str,
	assign_if_none,
	autodict,
	uuid_to_str
)

class Response(object):
	class STATUS(object):
		SUCCESS = 'success'
		FAILURE = 'fail'
		ERROR   = 'error'

	class ERROR(object):
		BAD_REQUEST          = { 'code': 400, 'message': 'Bad Request' }
		UNPROCESSABLE_ENTITY = { 'code': 422, 'message': 'Unprocessable Entity' }

	def __init__(self, status = None, data = None, error = None):
		self.uuid    = uuid.uuid4()
		self.version = get_version_str(ServerConfig.VERSION)
		self.status  = assign_if_none(status, Response.STATUS.SUCCESS)
		self.data    = data
		self.error   = error

	def set_error(self, error):
		self.status  = Response.STATUS.ERROR
		self.error   = error

	def set_data(self, data):
		self.data    = data

	def todict(self):
		dict_ = autodict()

		dict_['id']      = uuid_to_str(self.uuid)
		dict_['version'] = self.version
		dict_['status']  = self.status

		if self.data:
			dict_['data']  = self.data

		if self.error:
			dict_['error'] = self.error

		return dict_

	def toJSON(self):
		dict_ = self.todict()
		json_ = json.dumps(dict_)

		return json_
