<template>
  <div class="px-4">
    <v-row>
      <v-col
        v-for="provider in Object.keys(providers)"
        :cols="$vuetify.breakpoint.xs ? '12' : '6'"
        :key="provider"
        class="my-4"
      >
        <h2>{{ provider }}</h2>
        <div class="d-flex flex-column align-start pa-4">
          <li v-for="(item, index) in providers[provider].prices" :key="index">
            <span>{{ item.time }}:</span> {{ item.price }}
          </li>
          <li class="py-3">
            <span>Dirección:</span> {{ providers[provider].address }}
          </li>
        </div>
        <v-btn>
          <a :href="providers[provider].url" target="_blank">
            Ir a la página web
          </a>
        </v-btn>
      </v-col>
    </v-row>
    <iframe
      src="https://www.google.com/maps/d/embed?mid=1nm40WLmTCSSi0acdP7c0ZSQtweCGF8RL&ll=-33.36931928384845%2C-70.59007279073512&z=12"
      width="100%"
      height="600"
    />
  </div>
</template>

<script>
import providers from '@/providers'

export default {
  data() {
    return {
      providers,
    }
  },
}
</script>
