<template>
  <div>
    {{ initialTime }} {{ endTime }}
    <table>
      <tr>
        <th v-for="(court, index) in courts" :key="index">{{ court.name }}</th>
        <th>Hola</th>
        <th>Como</th>
        <th>Estas</th>
      </tr>
      <tr>
        <td v-for="(court, index) in courts" :key="index">{{ court.name }}</td>
        <td colspan="2" rowspan="2">Bien</td>
        <td>Bien</td>
      </tr>
      <tr>
        <td v-for="(court, index) in courts" :key="index" rowspan="2">
          {{ court.name }}
        </td>
        <td>Bien</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    providers: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {}
  },
  computed: {
    courts() {
      return this.providers.reduce(
        (courts, provider) => courts.concat(provider.courts),
        []
      )
    },
    initialTime() {
      return this.providers.reduce(
        (min, value) => (value.initial_time < min ? value.initial_time : min),
        '12:00'
      )
    },
    endTime() {
      return this.providers.reduce(
        (max, value) => (value.end_time > max ? value.end_time : max),
        '20:00'
      )
    },
  },
}
</script>
