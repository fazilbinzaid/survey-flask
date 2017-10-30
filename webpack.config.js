const webpack = require('webpack');
const path = require('path');
const Uglify = require('uglifyjs-webpack-plugin');

const APP_DIR = path.resolve(__dirname);
const BUILD_DIR = path.resolve(__dirname, 'src/assets/dist');

module.exports = {
	entry: APP_DIR + '/index.js',

	output: {
		path: BUILD_DIR,
		filename: 'bundle.js',
	},

	module: {
		loaders: [
			{
				test: /\.js?$/,
				loader: 'babel-loader',
				include: ['node_modules', 'src/assets/js'],
				query: {
					presets: ['env']
				}
			}, {
				test: /\.css?$/,
				loader: ['style-loader', 'css-loader']
			}, {
				test: /\.(eot|svg|ttf|woff|woff2)$/,
				loader: 'file-loader',
			}
		]
	},

	plugins: [
		new Uglify()
	]
}
