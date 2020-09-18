<template>
  <div>
    <v-date-picker v-model="pickedDate" />
    <div>{{ names }}. {{ initialTime }} - {{ finalTime }}</div>
    <div>
      {{ responses }}
    </div>
  </div>
</template>

<script>
const apiURL = 'https://padel-api-54td4ousva-uc.a.run.app/get_schedule'
export default {
  data() {
    return {
      pickedDate: '',
      responses: [],
    }
  },
  computed: {
    names() {
      const names = this.responses.map(response => response.Nombre).join(', ')
      return 'Clubes: ' + names
    },
    initialTime() {
      let time = 12
      this.responses.forEach(response => {
        if (response.StrHoraInicio) {
          const responseInitialTime = parseInt(
            response.StrHoraInicio.slice(0, 2)
          )
          if (responseInitialTime < time) {
            time = responseInitialTime
          }
        }
      })
      return time
    },
    finalTime() {
      let time = 20
      this.responses.forEach(response => {
        if (response.StrHoraFin) {
          const responseFinalTime = parseInt(response.StrHoraFin.slice(0, 2))
          if (responseFinalTime > time) {
            time = responseFinalTime
          }
        }
      })
      return time
    },
  },
  methods: {
    async fetchProvider(provider, date) {
      const response = await fetch(`${apiURL}/${provider}/${date}`)
      const text = await response.json()
      if (text.d) {
        this.responses.push(text.d)
      }
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
