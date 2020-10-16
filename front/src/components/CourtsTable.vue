<template>
  <div>
    <div class="overflow-x">
      <table class="courts-table">
        <tr>
          <th
            v-for="(provider, index) in providers"
            :key="index"
            :colspan="provider.courts.length"
            class="border-left"
            @click="select({ provider: provider.name, type: 'HEADER' })"
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
            :key="index"
            :rowspan="elem.rowspan"
            :class="'item item-' + elem.type"
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
      :provider="selectedItem.provider"
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
  },
  components: {
    BookingModal,
  },
  data() {
    return {
      selectedItem: null,
    }
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
    courtsHeaders() {
      const headers = []
      this.providers.forEach(provider => {
        provider.courts.forEach((court, index) => {
          headers.push({
            name: court.name,
            border: index === 0 ? 'border-left' : '',
            provider: provider.name,
          })
        })
      })
      return headers
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
    select(item) {
      if (!['AVAILABLE', 'FIXED_TIME', 'HEADER'].includes(item.type)) return
      this.selectedItem = item
    },
    getElementsFromTime(time) {
      const elements = this.courts.map(court =>
        this.getElementFromCourtAndTime(court, time)
      )
      return elements.filter(elem => elem !== false)
    },
    getElementFromCourtAndTime(court, time) {
      if (time < court.initial_time_float) return INVALID_OPTION
      if (time >= court.end_time_float) return INVALID_OPTION

      const halfHour = time % 1 > 0
      let value = {
        rowspan: 1,
        type: 'AVAILABLE',
        initial_time: halfHour ? `${time - 0.5}:30` : `${time}:00`,
        end_time: halfHour ? `${time + 0.5}:00` : `${time}:30`,
        name: court.name,
        provider: court.provider,
      }
      court.bookings.forEach(booking => {
        if (booking.initial_time_float === time) {
          value = {
            ...booking,
            type: 'BOOKING',
            rowspan: booking.total_time / 30,
            name: court.name,
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
            ...fixedTime,
            type: 'FIXED_TIME',
            rowspan: fixedTime.total_time / 30,
            name: court.name,
            provider: court.provider,
          }
        } else if (
          fixedTime.initial_time_float < time &&
          time < fixedTime.end_time_float
        ) {
          value = false
        }
      })
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
}

.item-AVAILABLE {
  background-color: #ffffff;
}
div.overflow-x {
  overflow-x: auto;
}
</style>
