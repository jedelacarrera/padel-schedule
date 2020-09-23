<template>
  <div>
    <v-tabs v-model="tab" grow>
      <v-tab v-for="item in items" :key="item" class="bg-black">
        {{ item }}
      </v-tab>
    </v-tabs>

    <schedule-tab v-if="tab === 0" />
    <prices-tab v-else />
  </div>
</template>

<script>
import ScheduleTab from '@/components/tabs/ScheduleTab'
import PricesTab from '@/components/tabs/PricesTab'

export default {
  components: {
    ScheduleTab,
    PricesTab,
  },
  data() {
    return {
      tab: null,
      items: ['Canchas', 'Clubes'],
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
</style>
