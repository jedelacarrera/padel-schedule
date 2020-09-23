<template>
  <div>
    <v-row>
      <v-col class="mx-4">
        <h1 class="schedule-title">
          Encuentra tu cancha!
        </h1>
        <h2 class="schedule-title">
          Canchas de padel en el sector oriente
        </h2>
      </v-col>
      <v-col class="py-0">
        <v-date-picker
          no-title
          v-model="pickedDate"
          first-day-of-week="1"
          :min="minDate"
          :max="maxDate"
        />
      </v-col>
      <v-col class="justify-start align-start ml-4">
        <v-checkbox v-model="conecta" label="Conecta" class="py-0 my-0 mt-4" />
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
      </v-col>
    </v-row>
    <courts-table :providers="responses" />
  </div>
</template>

<script>
import CourtsTable from '@/components/CourtsTable'
const apiURL = 'https://padel-api-54td4ousva-uc.a.run.app/get_schedule'
// const apiURL = 'http://localhost:8000/get_schedule'
const currentDate = new Date()
const twoWeeksAhead = new Date()
twoWeeksAhead.setDate(twoWeeksAhead.getDate() + 14)

export default {
  data() {
    return {
      pickedDate: currentDate.toISOString().slice(0, 10),
      responses: [],
      minDate: currentDate.toISOString(),
      maxDate: twoWeeksAhead.toISOString(),
      conecta: true,
      padelbreak: true,
      santuario: true,
      bullpadel: true,
      padeloriente: true,
    }
  },
  components: {
    CourtsTable,
  },
  methods: {
    async fetchProvider(provider, date) {
      try {
        const response = await fetch(`${apiURL}/${provider}/${date}`)
        const data = await response.json()
        this.responses.push(data)
      } catch (error) {
        console.log(error)
      }
    },
    retrieveProviders(value) {
      this.responses = []
      if (this.conecta) this.fetchProvider('conecta', value)
      if (this.padelbreak) this.fetchProvider('padelbreak', value)
      if (this.santuario) this.fetchProvider('santuario', value)
      if (this.bullpadel) this.fetchProvider('bullpadel', value)
      if (this.padeloriente) this.fetchProvider('padeloriente', value)
    },
  },
  created() {
    this.retrieveProviders(currentDate.toISOString().slice(0, 10))
  },
  watch: {
    pickedDate: function(value) {
      this.retrieveProviders(value)
    },
  },
}
</script>
