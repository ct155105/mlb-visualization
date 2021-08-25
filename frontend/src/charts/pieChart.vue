<template>
  <div>
    <div id="pie-chart-header"></div>
    <div id="pie-chart"></div>
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "pieChart",
  methods: {
    update() {
      let teams = {
        Reds: {
          wins: [1, 1, 2, 3, 4],
          losses: [0, 1, 1, 1, 1],
          gamesBack: [0, 1, 0, 0, 0],
        },
        Brewers: {
          wins: [1, 2, 2, 3, 3],
          losses: [0, 0, 1, 2, 3],
          gamesBack: [0, 0, 0, 1, 2],
        },
      };

      const singleGameHeight = 20;
      const singleDayMilisecondsTimer = 1000;

      var svg = d3
        .select("#bar-chart")
        .append("svg")
        .attr("width", 500)
        .attr("height", 500);

      
      var header = d3
        .select("#bar-chart-header")

      //for each team, for each day

      var reds = svg
        .append("rect")
        .attr("fill", "red")
        .attr("stroke", "#777777")
        .attr("x", 100)
        .attr("y", 0)
        .attr("height", 0)
        .attr("width", 10);

      var brewers = svg
        .append("rect")
        .attr("fill", "blue")
        .attr("x", 120)
        .attr("y", 0)
        .attr("height", 0)
        .attr("width", 10);

      for (let i = 0; i < teams.Reds.wins.length; i++) {
        header
          .transition()
          .delay(singleDayMilisecondsTimer * i)
          .text(i.toString())
        reds
          .transition()
          .ease(d3.easeLinear)
          .duration(singleDayMilisecondsTimer)
          .delay(singleDayMilisecondsTimer * i)
          .attr("height", teams.Reds.wins[i] * singleGameHeight);
        brewers
          .transition()
          .ease(d3.easeLinear)
          .duration(singleDayMilisecondsTimer)
          .delay(singleDayMilisecondsTimer * i)
          .attr("height", teams.Brewers.wins[i] * singleGameHeight);
      }

      //

      // bar2
      //   .transition()
      //   .ease(d3.easeLinear)
      //   .duration(2000)
      //   .delay(2000)
      //   .attr("height", 100);
    },
  },
  mounted() {
    this.update();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
