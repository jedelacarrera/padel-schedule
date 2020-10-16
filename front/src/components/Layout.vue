<template>
  <div>
    <v-tabs v-model="tab" grow>
      <v-tab class="bg-black">Canchas</v-tab>
      <v-tab class="bg-black">Clubes</v-tab>
    </v-tabs>

    <schedule-tab v-show="tab === 0" />
    <prices-tab v-show="tab !== 0" />
  </div>
</template>

<script>
import ScheduleTab from '@/components/ScheduleTab'
import PricesTab from '@/components/PricesTab'

export default {
  components: {
    ScheduleTab,
    PricesTab,
  },
  data() {
    return {
      tab: 0,
    }
  },
}
</script>

<style>
/* Helper classes */
.bg-black {
  background-color: #000 !important;
  color: #fff !important;
  font-size: 18px !important;
  font-weight: bold !important;
}
.v-tabs-slider-wrapper {
  height: 6px !important;
}
</style>
