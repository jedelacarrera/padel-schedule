<template>
  <v-dialog
    width="800"
    persistent
    content-class="rounded-card"
    @click:outside="cancel"
    :value="true"
  >
    <v-card class="pa-4">
      <v-row no-gutters>
        <v-col cols="11">
          <h2>{{ provider }}</h2>
        </v-col>
        <v-col cols="1" class="d-flex justify-end align-start">
          <v-icon @click="cancel">mdi-close</v-icon>
        </v-col>
      </v-row>
      <div class="d-flex flex-column align-start pa-4">
        <li v-for="(item, index) in providerElem.prices" :key="index">
          <span>{{ item.time }}:</span> {{ item.price }}
        </li>
        <li class="py-3"><span>Dirección:</span> {{ providerElem.address }}</li>
      </div>
      <v-btn>
        <a :href="providerElem.url" target="_blank">Ir a reservar</a>
      </v-btn>
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
    providerElem() {
      return providers[this.provider] || { url: '', address: '', prices: [] }
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
