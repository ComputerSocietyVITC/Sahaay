const path = require('path');

module.exports = {
  entry: path.resolve(__dirname, 'source', 'index.js'),
  output: {
    path: path.resolve(__dirname, 'static/frontend'),
    filename: 'main.js'
  },
  
  module: {
    rules: [
      {
        test: /\.(jsx|js)$/,
        include: path.resolve(__dirname, 'source'),
        exclude: /node_modules/,
        use: [{
          loader: 'babel-loader',
          options: {
            presets: [
              ['@babel/preset-env', {
                "targets": "defaults" 
              }],
              '@babel/preset-react'
            ]
          }
        }],
      
      }
    ],
  }
}
