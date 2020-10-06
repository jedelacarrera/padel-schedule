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
        <v-btn><a :href="providers[provider].url">Ir a la página web</a></v-btn>
      </v-col>
    </v-row>
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
