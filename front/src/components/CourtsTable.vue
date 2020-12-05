<template>
  <div>
    <div class="overflow-x">
      <table class="courts-table">
        <tr>
          <th
            v-for="(provider, index) in tableHeaders"
            class="border-left"
            :key="index"
            :colspan="provider.courts.length"
            @click="select({ provider: provider.id, type: 'HEADER' })"
          >
            <h5>{{ provider.name }}</h5>
          </th>
        </tr>
        <tr>
          <th
            v-for="(court, index) in courtsHeaders"
            :key="index"
            :class="court.border"
            @click="select({ provider: court.provider, type: 'HEADER' })"
          >
            <p>{{ court.name }}</p>
          </th>
        </tr>
        <tr v-for="time in commonTimes" :key="time">
          <td
            v-for="(elem, index) in getElementsFromTime(time)"
            :key="elem.provider + index.toString() + elem.initial_time"
            :rowspan="elem.rowspan"
            :class="`item item-${elem.type} item-${colors}-${elem.provider} item-${colors}-${elem.courtNumber}`"
            @click="select(elem)"
          >
            {{ elem.initial_time }}
            {{ elem.end_time ? '-' : '' }}
            {{ elem.end_time }}
          </td>
        </tr>
      </table>
    </div>
    <booking-modal
      :item="selectedItem"
      :date="date"
      v-if="selectedItem"
      @cancel="selectedItem = null"
    />
  </div>
</template>

<script>
import BookingModal from '@/components/BookingModal'

const INVALID_OPTION = {
  initial_time: '',
  end_time: '',
  type: 'INVALID',
  rowspan: 1,
}

export default {
  props: {
    providers: {
      type: Array,
      default: () => [],
    },
    date: {
      type: String,
      default: '',
    },
  },
  components: {
    BookingModal,
  },
  data() {
    return {
      selectedItem: null,
      colors: localStorage.getItem('colors') ? 'active' : '',
    }
  },
  computed: {
    tableHeaders() {
      return this.providers.filter(provider => provider.courts.length > 0)
    },
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
        [],
      )
    },
    courtsHeaders() {
      const headers = []
      this.providers.forEach(provider => {
        provider.courts.forEach((court, index) => {
          headers.push({
            name: court.name,
            border: index === 0 ? 'border-left' : '',
            provider: provider.id,
          })
        })
      })
      return headers
    },
    initialTime() {
      return this.providers.reduce(
        (min, value) =>
          value.initial_time_float < min ? value.initial_time_float : min,
        12,
      )
    },
    endTime() {
      return this.providers.reduce(
        (max, value) =>
          value.end_time_float > max ? value.end_time_float : max,
        20,
      )
    },
  },
  methods: {
    select(item) {
      console.log(item)
      if (!['AVAILABLE', 'FIXED_TIME', 'HEADER'].includes(item.type)) return
      this.selectedItem = item
    },
    getElementsFromTime(time) {
      const elements = this.courts.map(court =>
        this.getElementFromCourtAndTime(court, time),
      )
      return elements.filter(elem => elem !== false)
    },
    getElementFromCourtAndTime(court, time) {
      if (time < court.initial_time_float) return INVALID_OPTION
      if (time >= court.end_time_float) return INVALID_OPTION

      const halfHour = time % 1 > 0
      let value = {
        courtNumber: court.name.trim().slice(-1),
        rowspan: 1,
        type: 'AVAILABLE',
        initial_time: halfHour ? `${time - 0.5}:30` : `${time}:00`,
        end_time: halfHour ? `${time + 0.5}:00` : `${time}:30`,
        name: court.name,
        resource: court.id,
        hour: halfHour ? `${time - 0.5}:30` : `${time}:00`,
        provider: court.provider,
      }
      court.bookings.forEach(booking => {
        if (booking.initial_time_float === time) {
          value = {
            ...value,
            ...booking,
            type: 'BOOKING',
            rowspan: booking.total_time / 30,
            name: court.name,
            resource: court.id,
            provider: court.provider,
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
            ...value,
            ...fixedTime,
            type: 'FIXED_TIME',
            rowspan: fixedTime.total_time / 30,
            name: court.name,
            resource: court.id,
            hour: fixedTime.id,
            provider: court.provider,
          }
        } else if (
          fixedTime.initial_time_float < time &&
          time < fixedTime.end_time_float
        ) {
          value = false
        }
      })
      if (value && value.type === 'FIXED_TIME') {
        court.bookings.forEach(booking => {
          if (
            value.initial_time_float < booking.initial_time_float &&
            booking.initial_time_float < value.end_time_float
          ) {
            value.end_time = booking.initial_time
            value.end_time_float = booking.initial_time_float
            value.total_time =
              (value.end_time_float - value.initial_time_float) * 60
            value.rowspan = value.total_time / 30
          }
        })
      }
      if (value && value.type === 'AVAILABLE' && court.fixed_times.length) {
        return INVALID_OPTION
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
  padding-left: 5px;
  padding-right: 5px;
  border: 0;
  background-color: #000000;
  color: #fff;
  font-weight: normal;
  cursor: pointer;
}

th.border-left {
  border-left: solid 1px white;
}

.courts-table th p {
  margin: 0;
  font-size: 11px;
}

.courts-table td {
  border: 1px solid #f2f2f2;
}

.item {
  font-size: 10px;
  padding-left: 2px;
  padding-right: 2px;
  white-space: nowrap;
}
.item-INVALID {
  background-color: #f2f2f2;
}

td.item-BOOKING {
  background-color: #f56464;
  color: #fff;
  border: 1px solid #dd5a5a;
}

.item-FIXED_TIME {
  background-color: #ffffff;
  cursor: pointer;
}

.item-AVAILABLE {
  background-color: #ffffff;
  cursor: pointer;
}

.item-active-padeloriente {
  background-color: green;
  color: #fff;
}

.item-active-santuario {
  background-color: lightgreen;
}

.item-active-maspadel {
  background-color: lightblue;
}
.item-active-rinconada {
  background-color: purple;
  color: #fff;
}

.item-active-bullpadel {
  background-color: #179be5;
}

.item-active-conecta {
  background-color: yellow;
}

.item-active-altopadel {
  background-color: orange;
}

.item-active-padelbreak {
  background-color: #a78b67;
}

.item-active-1 {
  opacity: 1;
}

.item-active-2 {
  opacity: 0.93;
}

.item-active-2 {
  opacity: 0.86;
}

.item-active-3 {
  opacity: 0.79;
}

.item-active-4 {
  opacity: 0.72;
}

.item-active-5 {
  opacity: 0.65;
}

.item-active-6 {
  opacity: 0.58;
}

div.overflow-x {
  overflow-x: auto;
}
</style>
