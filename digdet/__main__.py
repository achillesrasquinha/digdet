# imports - module imports
from digdet.config.server import ServerConfig
from digdet.server.app import app

if __name__ == '__main__':
    host  = ServerConfig.HOST
    port  = ServerConfig.PORT
    debug = ServerConfig.ENVIRONMENT == 'development'

    app.run(host = host, port = port, debug = debug)
