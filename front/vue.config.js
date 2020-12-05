const configureWebpack = {
  output: {
    globalObject: 'this',
  },
  plugins: [],
}

module.exports = {
  configureWebpack,
  transpileDependencies: ['vuetify'],
  css: {
    loaderOptions: {
      scss: {},
    },
    extract: false,
  },
  pluginOptions: {
    webpackBundleAnalyzer: {
      openAnalyzer: false,
    },
  },
}
