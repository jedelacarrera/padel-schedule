import '@mdi/font/css/materialdesignicons.css'
import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

export default new Vuetify({
  lang: {
    current: 'es',
  },
  icons: {
    iconfont: 'mdi',
    value: {},
  },
  theme: {
    options: {
      customProperties: true,
      variations: false,
    },
    dark: false,
    themes: {
      light: {
        primary: '#0074B5',
        background: '#F9F9F9',
        red: '#EA4436',
      },
    },
  },
})
