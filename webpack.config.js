var path       = require('path');
var webpack    = require('webpack');
var Config     = require('./config');

module.exports = {
  entry: [
    path.join(Config.Path.APP, 'Client.js'),
    path.join(Config.Path.ASSETS, 'js', 'scripts.js')
  ],
  output: {
    path: path.join(Config.Path.ASSETS, 'js'),
    filename: 'bundle.min.js'
  },
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
