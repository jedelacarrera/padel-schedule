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
      scss: {
        prependData: `@import "@/assets/styles.scss";`,
      },
    },
    extract: false,
  },
  pluginOptions: {
    webpackBundleAnalyzer: {
      openAnalyzer: false,
    },
  },
}
