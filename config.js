var path           = require('path')

var Config         = { };

Config.ENVIRONMENT = process.env.NODE_ENV

Config.Path        = { };
Config.Path.ROOT   = __dirname;
Config.Path.BASE   = path.join(Config.Path.ROOT, 'digdet')
Config.Path.APP    = path.join(Config.Path.BASE, 'client/app');
Config.Path.ASSETS = path.join(Config.Path.BASE, 'assets')

module.exports     = Config;
