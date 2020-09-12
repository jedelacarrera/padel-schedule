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

const opts = {
  lang: {
    locales: { es },
    current: 'es',
  },
  icons: {
    iconfont: 'mdi',
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
      },
    },
  },
}

export default new Vuetify(opts)
