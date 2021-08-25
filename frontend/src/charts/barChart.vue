<template>
  <div>
    <div id="hello-world"></div>
    <div id="bar-chart-header"></div>
    <div id="bar-chart"></div>
    <img src="CIN-2021.png" />
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "barChart",
  props: ["season"],
  methods: {
    update() {
      let newSeason = this.season;
      console.log(newSeason);

      const singleGameHeight = 20;
      const singleDayMilisecondsTimer = 250;
      const xIndex = [30, 100, 170, 240, 310];

      let scaleFactor = 1;

      var svg = d3
        .select("#bar-chart")
        .append("svg")
        .attr("width", 400 * scaleFactor)
        .attr("height", 500 * scaleFactor);

      //Add ticks to y axis
      for (let i = 0; i < 20; i++) {
        svg
          .append("text")
          .attr("transform", "translate(10," + i * singleGameHeight + ")")
          .style("text-anchor", "middle")
          .text("-" + i.toString());
      }

      var header = d3.select("#bar-chart-header");

      //for each team, for each day

      var redsLogo = svg
        .append("svg:image")
        .attr("xlink:href", "CIN-2021.png")
        .attr("x", xIndex[0] * scaleFactor + 10)
        .attr("y", 0)
        .attr("width", 40)
        .attr("height", 40);

      var brewersLogo = svg
        .append("svg:image")
        .attr("xlink:href", "MIL-2021.png")
        .attr("x", xIndex[1] * scaleFactor + 10)
        .attr("y", 0)
        .attr("width", 40)
        .attr("height", 40);

      var cubsLogo = svg
        .append("svg:image")
        .attr("xlink:href", "CHC-2021.png")
        .attr("x", xIndex[2] * scaleFactor + 10)
        .attr("y", 0)
        .attr("width", 40)
        .attr("height", 40);

      var cardinalsLogo = svg
        .append("svg:image")
        .attr("xlink:href", "STL-2021.png")
        .attr("x", xIndex[3] * scaleFactor + 10)
        .attr("y", 0)
        .attr("width", 40)
        .attr("height", 40);

      var piratesLogo = svg
        .append("svg:image")
        .attr("xlink:href", "PIT-2021.png")
        .attr("x", xIndex[4] * scaleFactor + 10)
        .attr("y", 0)
        .attr("width", 40)
        .attr("height", 40);

      var reds = svg
        .append("rect")
        .attr("fill", "#ee174f")
        .attr("stroke", "white")
        .attr("x", xIndex[0] * scaleFactor)
        .attr("y", 0 * scaleFactor)
        .attr("height", 0 * scaleFactor)
        .attr("width", 60 * scaleFactor);

      var brewers = svg
        .append("rect")
        .attr("fill", "#10274b")
        .attr("stroke", "#d8ad33")
        .attr("x", xIndex[1] * scaleFactor)
        .attr("y", 0 * scaleFactor)
        .attr("height", 0 * scaleFactor)
        .attr("width", 60 * scaleFactor);

      var cubs = svg
        .append("rect")
        .attr("fill", "#002f6c")
        .attr("stroke", "#c8102e")
        .attr("x", xIndex[2] * scaleFactor)
        .attr("y", 0 * scaleFactor)
        .attr("height", 0 * scaleFactor)
        .attr("width", 60 * scaleFactor);

      var cardinals = svg
        .append("rect")
        .attr("fill", "#d41244")
        .attr("stroke", "#162d5c")
        .attr("x", xIndex[3] * scaleFactor)
        .attr("y", 0 * scaleFactor)
        .attr("height", 0 * scaleFactor)
        .attr("width", 60 * scaleFactor);

      var pirates = svg
        .append("rect")
        .attr("fill", "#ffc82e")
        .attr("stroke", "black")
        .attr("x", xIndex[4] * scaleFactor)
        .attr("y", 0 * scaleFactor)
        .attr("height", 0 * scaleFactor)
        .attr("width", 60 * scaleFactor);

      let teamStandings = [
        { team: "CIN", games_back: 0 },
        { team: "MIL", games_back: 0 },
        { team: "CHC", games_back: 0 },
        { team: "STL", games_back: 0 },
        { team: "PIT", games_back: 0 },
      ];
      for (let i = 0; i < newSeason.length; i++) {
        teamStandings.forEach((team, index, array) => {
          let gamesBack = newSeason[i][team.team].games_back;
          team.games_back = gamesBack;
          array[index] = team;
        });
        teamStandings = teamStandings.sort(function (a, b) {
          return a.games_back - b.games_back;
        });

        let cinStanding = teamStandings
          .map(function (e) {
            return e.team;
          })
          .indexOf("CIN");
        let milStanding = teamStandings
          .map(function (e) {
            return e.team;
          })
          .indexOf("MIL");
        let chcStanding = teamStandings
          .map(function (e) {
            return e.team;
          })
          .indexOf("CHC");
        let stlStanding = teamStandings
          .map(function (e) {
            return e.team;
          })
          .indexOf("STL");
        let pitStanding = teamStandings
          .map(function (e) {
            return e.team;
          })
          .indexOf("PIT");

        header
          .transition()
          .delay(singleDayMilisecondsTimer * i)
          .text(newSeason[i].date["day"].toString());

        reds
          .transition()
          .ease(d3.easeLinear)
          .duration(singleDayMilisecondsTimer)
          .delay(singleDayMilisecondsTimer * i)
          .attr("x", xIndex[cinStanding])
          .attr("height", newSeason[i].CIN.games_back * singleGameHeight);
        redsLogo
          .transition()
          .ease(d3.easeLinear)
          .duration(singleDayMilisecondsTimer)
          .delay(singleDayMilisecondsTimer * i)
          .attr("x", xIndex[cinStanding] + 10)
          .attr("y", newSeason[i].CIN.games_back * singleGameHeight);

        brewers
          .transition()
          .ease(d3.easeLinear)
          .duration(singleDayMilisecondsTimer)
          .delay(singleDayMilisecondsTimer * i)
          .attr("x", xIndex[milStanding])
          .attr("height", newSeason[i].MIL.games_back * singleGameHeight);
        brewersLogo
          .transition()
          .ease(d3.easeLinear)
          .duration(singleDayMilisecondsTimer)
          .delay(singleDayMilisecondsTimer * i)
          .attr("x", xIndex[milStanding] + 10)
          .attr("y", newSeason[i].MIL.games_back * singleGameHeight);

        cardinals
          .transition()
          .ease(d3.easeLinear)
          .duration(singleDayMilisecondsTimer)
          .delay(singleDayMilisecondsTimer * i)
          .attr("x", xIndex[stlStanding])
          .attr("height", newSeason[i].STL.games_back * singleGameHeight);
        cardinalsLogo
          .transition()
          .ease(d3.easeLinear)
          .duration(singleDayMilisecondsTimer)
          .delay(singleDayMilisecondsTimer * i)
          .attr("x", xIndex[stlStanding] + 10)
          .attr("y", newSeason[i].STL.games_back * singleGameHeight);

        cubs
          .transition()
          .ease(d3.easeLinear)
          .duration(singleDayMilisecondsTimer)
          .delay(singleDayMilisecondsTimer * i)
          .attr("x", xIndex[chcStanding])
          .attr("height", newSeason[i].CHC.games_back * singleGameHeight);
        cubsLogo
          .transition()
          .ease(d3.easeLinear)
          .duration(singleDayMilisecondsTimer)
          .delay(singleDayMilisecondsTimer * i)
          .attr("x", xIndex[chcStanding] + 10)
          .attr("y", newSeason[i].CHC.games_back * singleGameHeight);

        pirates
          .transition()
          .ease(d3.easeLinear)
          .duration(singleDayMilisecondsTimer)
          .delay(singleDayMilisecondsTimer * i)
          .attr("x", xIndex[pitStanding])
          .attr("height", newSeason[i].PIT.games_back * singleGameHeight);
        piratesLogo
          .transition()
          .ease(d3.easeLinear)
          .duration(singleDayMilisecondsTimer)
          .delay(singleDayMilisecondsTimer * i)
          .attr("x", xIndex[pitStanding] + 10)
          .attr("y", newSeason[i].PIT.games_back * singleGameHeight);
      }
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
