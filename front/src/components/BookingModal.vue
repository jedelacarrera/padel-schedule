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
          <h2>{{ providerElem.name }}</h2>
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
      <div class="mt-2" v-if="item.resource">
        <h3>{{ response.title }}</h3>
        <v-row>
          <v-col cols="4">
            <img
              :src="`imgs/${item.provider}.png`"
              height="100"
              :style="{
                'background-color': providerElem.background,
                padding: '5px',
              }"
              v-if="providerElem.background"
            />
            <img v-else height="100" :src="`imgs/${item.provider}.png`" />
          </v-col>
          <v-col cols="8">
            <div v-for="option in response.options" :key="option.token">
              <v-btn
                small
                rounded
                color="#6abd11"
                class="mb-1"
                @click="goToToken(option.token)"
                >{{ option.description }}</v-btn
              >
            </div>
            <h4 v-if="response.options.length === 0 && !loading">
              No hay horarios disponibles
            </h4>
            <v-btn
              small
              rounded
              class="pa-4 text-decoration-none"
              color="#6abd11"
              @click="goToProvider"
            >
              Ver horarios <br />
              en página web
            </v-btn>
          </v-col>
        </v-row>
      </div>
      <v-btn v-else @click="goToProvider">Ver horarios en página web</v-btn>
      <v-row
        v-if="providerElem.terms && response.options.length > 0"
        class="pl-4"
      >
        <v-col cols="1" class="text-end">
          <v-checkbox v-model="checked" readonly class="mt-0" />
        </v-col>
        <v-col cols="11" class="text-start mt-1">
          Acepto
          <a class="px-1" :href="providerElem.terms" target="_blank">
            términos y condiciones
          </a>
          del club
        </v-col>
      </v-row>
    </v-card>
  </v-dialog>
</template>

<script>
import providers from '@/providers'
import { getAvailability, getFixedTimeInfo } from '@/apiUrls'

export default {
  props: {
    item: {
      type: Object,
      default: () => ({
        providerId: '',
        type: '',
        resource: '',
        hour: '',
      }),
    },
    date: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      loading: true,
      checked: true,
      response: {
        image_url: '',
        options: [],
        title: '',
      },
    }
  },
  computed: {
    providerElem() {
      return (
        providers[this.item.provider] || { url: '', address: '', prices: [] }
      )
    },
    url() {
      return this.item.type === 'FIXED_TIME'
        ? getFixedTimeInfo
        : getAvailability
    },
  },
  async created() {
    if (!this.item.resource) return
    const suffix = `${this.item.provider}/${this.item.resource}/${this.date}/${this.item.hour}`
    const response = await fetch(`${this.url}/${suffix}`)
    this.response = await response.json()
    this.loading = false
  },
  methods: {
    cancel() {
      this.$emit('cancel')
    },
    goToProvider() {
      window.open(this.providerElem.url + 'Booking/Grid.aspx')
    },
    goToToken(token) {
      window.open(`${this.providerElem.url}booking/info.aspx?token=${token}`)
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
