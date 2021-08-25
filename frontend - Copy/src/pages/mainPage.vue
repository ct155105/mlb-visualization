<template>
  <div id="main-page">
    <h1>2021 NL Central</h1>
    <!-- <bar-chart /> -->
  </div>
</template>

<script>
// import barChart from '@/charts/barChart.vue'
import api from '@/apiService.js'

export default {
  name: 'App',
  components: {
    // barChart
  },
  methods: {
      getSeason(year){
          return api.getSeason(year).then((data) => {
              return data
          })
      }
  }
}
</script>