<template>
  <div>
    <v-row justify="space-around">
      <v-date-picker
        no-title
        v-model="pickedDate"
        first-day-of-week="1"
        :min="minDate"
        :max="maxDate"
      />
    </v-row>
    <div>{{ names }}</div>
    <courts-table :providers="responses" />
  </div>
</template>

<script>
import CourtsTable from '@/components/CourtsTable'
const apiURL = 'https://padel-api-54td4ousva-uc.a.run.app/get_schedule'
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
    }
  },
  components: {
    CourtsTable,
  },
  computed: {
    names() {
      const names = this.responses.map(response => response.name).join(', ')
      return 'Clubes: ' + names
    },
  },
  methods: {
    async fetchProvider(provider, date) {
      const response = await fetch(`${apiURL}/${provider}/${date}`)
      const data = await response.json()
      console.log(data)
      this.responses.push(data)
    },
  },
  watch: {
    pickedDate: function(value) {
      this.responses = []
      this.fetchProvider('conecta', value)
    },
  },
}
</script>
