<template>
  <div>
    <div class="align-center justify-center d-flex">
      <table class="courts-table">
        <tr>
          <th v-for="(court, index) in courts" :key="index" class="header">
            <div>
              <h5>{{ court.provider }}</h5>
              <p>({{ court.name }})</p>
            </div>
          </th>
        </tr>
        <tr v-for="time in commonTimes" :key="time">
          <td
            v-for="(elem, index) in getElementsFromTime(time)"
            :key="index"
            :rowspan="elem.rowspan"
            :class="'item item-' + elem.type"
          >
            {{ elem.initial_time }} - {{ elem.end_time }}
          </td>
        </tr>
      </table>
    </div>
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
    commonTimes() {
      const commonTimes = [this.initialTime]
      while (commonTimes[commonTimes.length - 1] + 0.5 < this.endTime) {
        commonTimes.push(commonTimes[commonTimes.length - 1] + 0.5)
      }
      return commonTimes
    },
    courts() {
      return this.providers.reduce(
        (courts, provider) => courts.concat(provider.courts),
        []
      )
    },
    initialTime() {
      return this.providers.reduce(
        (min, value) =>
          value.initial_time_float < min ? value.initial_time_float : min,
        12
      )
    },
    endTime() {
      return this.providers.reduce(
        (max, value) =>
          value.end_time_float > max ? value.end_time_float : max,
        20
      )
    },
  },
  methods: {
    getElementsFromTime(time) {
      const elements = this.courts.map(court =>
        this.getElementFromCourtAndTime(court, time)
      )
      console.log(
        time,
        elements.map(elem => (elem ? elem.type + elem.rowspan : elem))
      )
      return elements.filter(elem => elem !== false)
    },
    getElementFromCourtAndTime(court, time) {
      let value = { rowspan: 1, type: 'AVAILABLE' }
      court.bookings.forEach(booking => {
        if (booking.initial_time_float === time) {
          value = {
            ...booking,
            type: 'BOOKING',
            rowspan: booking.total_time / 30,
          }
        } else if (
          booking.initial_time_float < time &&
          time < booking.end_time_float
        ) {
          value = false
        }
      })
      if (value && value.type === 'BOOKING') return value
      if (value === false) return false

      court.fixed_times.forEach(fixedTime => {
        if (fixedTime.initial_time_float === time) {
          value = {
            ...fixedTime,
            type: 'FIXED_TIME',
            rowspan: fixedTime.total_time / 30,
          }
        } else if (
          fixedTime.initial_time_float < time &&
          time < fixedTime.end_time_float
        ) {
          value = false
        }
      })
      if (value && value.type === 'AVAILABLE' && court.fixed_times.length) {
        return {
          initial_time: '',
          end_time: '',
          type: 'INVALID',
          rowspan: 1,
        }
      }
      return value
    },
  },
}
</script>
<style>
.courts-table {
  border-collapse: collapse;
  margin-bottom: 50px;
}

.courts-table th {
  border: 0;
  background-color: #000000;
  color: #fff;
  font-weight: normal;
}

.courts-table th p {
  margin: 0;
  font-size: 11px;
}

.courts-table td {
  border: 1px solid #f2f2f2;
}

.item {
  font-size: 14px;
  padding-left: 10px;
  padding-right: 10px;
}
.item-INVALID {
  background-color: #f2f2f2;
}

td.item-BOOKING {
  background-color: #f56464;
  color: #fff;
  border: 1px solid #dd5a5a;
}

.item-AVAILABLE,
.item-FIXED_TIME {
  background-color: #ffffff;
}
</style>
