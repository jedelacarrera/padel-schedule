<template>
  <div>
    <v-row>
      <v-col class="mx-4" order="1">
        <h1 class="schedule-title py-2">¡Encuentra tu cancha!</h1>
        <h2 class="schedule-title py-2">
          Canchas de padel en el sector oriente de Santiago
        </h2>
      </v-col>
      <v-col class="pt-0 pb-2" :order="$vuetify.breakpoint.xs ? '3' : '2'">
        <v-date-picker
          no-title
          v-model="pickedDate"
          first-day-of-week="1"
          :min="minDate"
          :max="maxDate"
        />
      </v-col>
      <v-col
        class="justify-start align-start ml-4 pb-0"
        :order="$vuetify.breakpoint.xs ? '2' : '3'"
      >
        <v-checkbox v-model="conecta" label="Conecta" class="py-0 my-0" />
        <v-checkbox
          v-model="padelbreak"
          label="Padel Break"
          class="py-0 my-0"
        />
        <v-checkbox v-model="santuario" label="Santuario" class="py-0 my-0" />
        <v-checkbox v-model="bullpadel" label="Bull Padel" class="py-0 my-0" />
        <v-checkbox
          v-model="padeloriente"
          label="Padel oriente"
          class="py-0 my-0"
        />
        <v-checkbox v-model="altopadel" label="Alto padel" class="py-0 my-0" />
        <v-checkbox v-model="maspadel" label="Más Padel" class="py-0 my-0" />
        <v-checkbox
          v-model="rinconada"
          label="Club Rinconada"
          class="py-0 my-0"
        />
      </v-col>
    </v-row>
    <courts-table :providers="responses" />
  </div>
</template>

<script>
import CourtsTable from '@/components/CourtsTable'
const apiURL = 'https://padel-api-54td4ousva-uc.a.run.app/get_schedule'
// const apiURL = 'http://localhost:8000/get_schedule'
const currentDate = new Date().toISOString().slice(0, 10)
const twoWeeksAhead = new Date()
twoWeeksAhead.setDate(twoWeeksAhead.getDate() + 14)

const DEFAULT_RESPONSES = JSON.stringify({
  conecta: { courts: [] },
  padelbreak: { courts: [] },
  santuario: { courts: [] },
  bullpadel: { courts: [] },
  padeloriente: { courts: [] },
  altopadel: { courts: [] },
  maspadel: { courts: [] },
  rinconada: { courts: [] },
})

export default {
  data() {
    return {
      pickedDate: currentDate,
      responsesDict: JSON.parse(DEFAULT_RESPONSES),
      minDate: currentDate,
      maxDate: twoWeeksAhead.toISOString(),
      conecta: true,
      padelbreak: true,
      santuario: true,
      bullpadel: true,
      padeloriente: true,
      altopadel: true,
      maspadel: true,
      rinconada: true,
    }
  },
  components: {
    CourtsTable,
  },
  computed: {
    responses() {
      const responses = []
      if (this.conecta) responses.push(this.responsesDict.conecta)
      if (this.padelbreak) responses.push(this.responsesDict.padelbreak)
      if (this.santuario) responses.push(this.responsesDict.santuario)
      if (this.bullpadel) responses.push(this.responsesDict.bullpadel)
      if (this.padeloriente) responses.push(this.responsesDict.padeloriente)
      if (this.altopadel) responses.push(this.responsesDict.altopadel)
      if (this.maspadel) responses.push(this.responsesDict.maspadel)
      if (this.rinconada) responses.push(this.responsesDict.rinconada)
      return responses
    },
  },
  methods: {
    async fetchProvider(provider, date) {
      try {
        const response = await fetch(`${apiURL}/${provider}/${date}`)
        const data = await response.json()
        if (date === this.pickedDate) {
          this.responsesDict[provider] = data
        }
      } catch (error) {
        console.log(error)
        this.responsesDict[provider] = { courts: [] }
      }
    },
    retrieveProviders(value) {
      this.responsesDict = JSON.parse(DEFAULT_RESPONSES)

      this.fetchProvider('conecta', value)
      this.fetchProvider('padelbreak', value)
      this.fetchProvider('santuario', value)
      this.fetchProvider('bullpadel', value)
      this.fetchProvider('padeloriente', value)
      this.fetchProvider('altopadel', value)
      this.fetchProvider('maspadel', value)
      this.fetchProvider('rinconada', value)
    },
  },
  created() {
    this.retrieveProviders(currentDate)
  },
  watch: {
    pickedDate: function (value) {
      this.retrieveProviders(value)
    },
  },
}
</script>
<style>
div.v-messages {
  min-height: 5px;
}
</style>
