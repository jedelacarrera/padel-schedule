<template>
  <v-card color="basil">
    <v-card-title class="text-center justify-center py-6">
      <h1 class="font-weight-bold display-3 basil--text">
        Encuentra tu cancha de padel!
      </h1>
    </v-card-title>

    <v-tabs v-model="tab" background-color="transparent" color="basil" grow>
      <v-tab v-for="item in items" :key="item">
        {{ item }}
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item>
        <schedule-tab />
      </v-tab-item>
      <v-tab-item>
        <prices-tab />
      </v-tab-item>
      <v-tab-item>
        <prices-tab />
      </v-tab-item>
    </v-tabs-items>
  </v-card>
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
      items: ['Canchas', 'Tarifas', 'Ubicaciones'],
    }
  },
}
</script>

<style>
/* Helper classes */
.basil {
  background-color: #fffbe6 !important;
}
.basil--text {
  color: #356859 !important;
}
</style>
