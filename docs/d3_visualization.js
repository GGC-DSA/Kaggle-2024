const width = 416;
const height = 250;
const marginTop = 20;
const marginRight = 20;
const marginBottom = 30;
const marginLeft = 40;

// Select the graph container
var graphContainer = d3.select("#essay-length-graph");
console.log(graphContainer);

// Load data
// d3.json("../datasets/Official/test.json", function (data) {
//   dataViz(data);
// });

const response = fetch('https://raw.githubusercontent.com/GGC-DSA/Kaggle-2024/main/datasets/External/essay_lengths.json', {
      method: 'GET',
    })
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
      })
      .then(data => {

        console.log(data)
        dataViz(data)

      })
      .catch(error => console.error('There has been a problem with your fetch operation:', error));

function dataViz(data) {
  var lengths = [];
  for (const i in data) {
    lengths.push(data[i])
  };
  console.log(lengths);

  // Set the parameters for the histogram
  var histogram = d3.histogram()
    .thresholds(20); // then the numbers of bins

  var bins = histogram(lengths);

  const x = d3.scaleLinear()
    .domain([bins[0].x0, bins[bins.length - 1].x1])
    .range([marginLeft, width - marginRight]);

  // Declare the y (vertical position) scale
  const y = d3.scaleLinear()
    .domain([0, d3.max(bins, (d) => d.length)])
    .range([height - marginBottom, marginTop]);

  // Add a rect for each bin
  graphContainer.append("g")
    .attr("fill", "steelblue")
    .selectAll()
    .data(bins)
    .enter()
    .append('rect')
    .attr("x", (d) => x(d.x0) + 1)
    .attr("width", (d) => x(d.x1) - x(d.x0) - 1)
    .attr("y", (d) => y(d.length))
    .attr("height", (d) => y(0) - y(d.length));

  // Add the x-axis and label
  graphContainer.append("g")
    .attr("transform", `translate(0,${height - marginBottom})`)
    .call(d3.axisBottom(x).ticks(width / 80).tickSizeOuter(0))
    .call((g) => g.append("text")
      .attr("x", width - 2)
      .attr("y", marginBottom - 4)
      .attr("fill", "currentColor")
      .attr("text-anchor", "end")
      .text("Words per Essay"));

  // Add the y-axis and label, and remove the domain line
  graphContainer.append("g")
    .attr("transform", `translate(${marginLeft},0)`)
    .call(d3.axisLeft(y).ticks(height / 40))
    .call((g) => g.select(".domain").remove())
    .call((g) => g.append("text")
      .attr("x", -marginLeft + 2)
      .attr("y", 10)
      .attr("fill", "currentColor")
      .attr("text-anchor", "start")
      .text("Frequency of Length"));
}
