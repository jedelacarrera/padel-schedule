import Vue from 'vue'
import Vuetify from 'vuetify'
import { mount, createLocalVue } from '@vue/test-utils'
import PricesTab from '@/components/PricesTab.vue'

Vue.use(Vuetify)
const localVue = createLocalVue()

describe('PricesTab', () => {
  const vuetify = new Vuetify()
  const wrapper = mount(PricesTab, {
    localVue,
    vuetify,
  })

  it('Check PricesTab', () => {
    expect(wrapper.text()).toContain('Santuario')
    expect(wrapper.text()).toContain('Padel Break')
    expect(wrapper.text()).toContain('Bull Padel')
    expect(wrapper.text()).toContain('Conecta')
    expect(wrapper.text()).toContain('Padel Oriente')
    expect(wrapper.text()).toContain('Alto Padel')
    expect(wrapper.text()).toContain('Más Padel')
    expect(wrapper.text()).toContain('Club Rinconada')
  })
})
