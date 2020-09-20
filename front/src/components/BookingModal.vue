<template>
  <v-dialog
    width="800"
    persistent
    content-class="rounded-card"
    @click:outside="cancel"
    :value="true"
  >
    <v-card class="pa-4">
      <h2>{{ provider }}</h2>
      <div class="d-flex flex-column align-start pa-4">
        <li v-for="(item, index) in prices" :key="index">
          <span>{{ item.time }}:</span> {{ item.price }}
        </li>
      </div>
      <v-btn><a :href="url">Ir a reservar</a></v-btn>
    </v-card>
  </v-dialog>
</template>

<script>
import providers from '@/providers'

export default {
  props: {
    provider: {
      type: String,
      default: '',
    },
  },
  computed: {
    url() {
      console.log('Provider', this.provider)
      console.log('Providers', providers)
      const provider = providers[this.provider] || {}
      return provider.url
    },
    prices() {
      const provider = providers[this.provider] || {}
      return provider.prices || []
    },
  },
  methods: {
    cancel() {
      this.$emit('cancel')
    },
  },
}
</script>
<style>
li span {
  font-weight: bold;
  padding-right: 10px;
}
</style>
