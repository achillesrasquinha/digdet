var path       = require('path');
var webpack    = require('webpack');
var Config     = require('./config');
var debug      = Config.ENVIRONMENT == 'development';

module.exports = {
  entry: [
    path.join(Config.Path.APP, 'Client.js'),
    path.join(Config.Path.BASE, 'client', 'scripts.js')
  ],
  output: {
    path: path.join(Config.Path.ASSETS, 'js'),
    filename: 'bundle.min.js'
  },
  plugins: debug ? [ ] : [
    new webpack.optimize.UglifyJsPlugin()
  ],
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loaders: ['babel-loader']
      }
    ]
  }
};
