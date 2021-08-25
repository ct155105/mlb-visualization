<template>
  <div id="main-page">
    <h1>2021 NL Central</h1>
    <div v-if="season">
      <bar-chart :season="season" />
    </div>
  </div>
</template>

<script>
import barChart from "@/charts/barChart.vue";
import api from "@/apiService.js";

export default {
  name: "App",
  components: {
    barChart,
  },
  data() {
    return {
      season: null,
    };
  },
  methods: {
    getSeason(year) {
      return api.getSeason(year).then((data) => {
        return data;
      });
    },
  },
  created() {
    this.getSeason(2021).then((data) => {
      console.log(data);
      this.season = data;
    });
  },
};
</script>