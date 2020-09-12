import '@mdi/font/css/materialdesignicons.css'
import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import es from 'vuetify/es5/locale/es'
import { Ripple } from 'vuetify/lib/directives'

Vue.use(Vuetify, {
  directives: {
    Ripple,
  },
})

export default new Vuetify({
  lang: {
    locales: { es },
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
      dark: {
        primary: '#0074B5',
        background: '#F9F9F9',
        red: '#EA4436',
      },
    },
  },
})
