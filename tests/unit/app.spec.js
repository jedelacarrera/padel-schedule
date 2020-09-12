import Vue from 'vue'
import Vuetify from 'vuetify'
import { mount, createLocalVue } from '@vue/test-utils'
import App from '@/App.vue'

Vue.use(Vuetify)
const localVue = createLocalVue()

describe('App', () => {
  const vuetify = new Vuetify()
  const wrapper = mount(App, {
    localVue,
    vuetify,
  })

  it('Check App', () => {
    expect(wrapper.findAll('img').length).toBe(1)
    expect(wrapper.text()).toContain('Find the padel courts')
  })
})
