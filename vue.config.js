const configureWebpack = {
  output: {
    globalObject: 'this',
  },
  plugins: [],
}

export default {
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
