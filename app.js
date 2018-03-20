// Define SVG area dimensions
var svgWidth = 850;
var svgHeight = 400;

// Define the chart's margins as an object
var margin = {top: 20, right: 40, bottom: 100, left: 100};

// Define dimensions of the chart area
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Select body, append SVG area to it, and set the dimensions
var svg = d3
  .select(".chart")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth)
  // Append a group to the SVG area and shift ('translate') it to the right and to the bottom
  .append("g")
  .attr("transform", "translate(" + margin.left + ", " + margin.top + ")");

// Append an SVG group
var chart = svg.append("g");

// Append a div to the bodyj to create tooltips, assign it a class
d3.select(".chart")
  .append("div").attr("class", "tooltip").style("opacity", 0);

// Retrieve data from the CSV file and execute everything below
d3.csv("data2.csv", function(err, hData) {
  if (err) throw err;

  hData.forEach(function(data) {
    data.avgPopulation = +data.avgPopulation;
    data.avgHHIncome = +data.avgHHIncome;
    data.avgPovCt = +data.avgPovCt;
    data.proprietary = +data.proprietary; 
    data.government = +data.government;
    data.nonProfit = +data.nonProfit;
    });

//Create scale functions
  var xLinearScale = d3.scaleLinear().range([0, width]);
  var yLinearScale = d3.scaleLinear().range([height, 0]);

//Create axis functions
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

//Define current x and y axis
var currentAxisLabelX = "avgPopulation";
var currentAxisLabelY = "proprietary";

//Set up xvalue and yvalue
  var xMin;
  var xMax;
  var yMax;

function findMinAndMax(xcolumn) {
  xMin = d3.min(hData, function(data){return +data[xcolumn]*0.8;});
  xMax = d3.max(hData, function(data){return +data[xcolumn]*1.1;});
  yMax = d3.max(hData,function(data){return +data[currentAxisLabelY]*1.1;})
}

  findMinAndMax(currentAxisLabelX);
  xLinearScale.domain([xMin, xMax]) ;console.log(xMin, xMax, yMax)

function findMinAndMaxY(ycolumn) {
  yMax = d3.max(hData,function(data){return +data[currentAxisLabelY]*1.1;}) }

  findMinAndMaxY(currentAxisLabelY);
  yLinearScale.domain([0,yMax])   ;

// Initialize tooltip
var toolTip = d3.tip().attr("class", "tooltip")
    // Define position
  .offset([80, -60])
  .html(function(data){
      var stateName = data.state;
      var yinfo = +data[currentAxisLabelY];
      var xinfo = +data[currentAxisLabelX];
      if ((currentAxisLabelX === "avgPopulation") && (currentAxisLabelY==="proprietary")) 
        {return stateName + "<br> Avg Population: " + xinfo +
         "<br> + Number of Proprietary Ownership: " + yinfo;}
      else if ((currentAxisLabelX === "avgPopulation") && (currentAxisLabelY==="government")) 
        {return stateName + "<br> Avg Population: " + xinfo +
         "<br> + Number of Government Ownership: " + yinfo;}
      else if ((currentAxisLabelX === "avgPopulation") && (currentAxisLabelY==="nonProfit")) 
        {return stateName + "<br> Avg Population: " + xinfo +
         "<br> + Number of Non Profit Ownership: " + yinfo;}

      else if (currentAxisLabelX === "avgHHIncome"&& currentAxisLabelY==="proprietary") 
        {return stateName + "<br> Avg Household Income: " + xinfo +
         "<br> + Number of Proprietary Ownership: " + yinfo;}
      else if (currentAxisLabelX === "avgHHIncome"&& currentAxisLabelY==="government") 
        {return stateName + "<br> Avg Household Income: " + xinfo +
         "<br> + Number of Government Ownership: " + yinfo;}
      else if (currentAxisLabelX === "avgHHIncome"&& currentAxisLabelY==="nonProfit") 
        {return stateName + "<br> Avg Household Income: " + xinfo +
         "<br> + Number of Non Profit Ownership: " + yinfo;}

      else if (currentAxisLabelX === "avgPovCt"&& currentAxisLabelY==="proprietary") 
        {return stateName + "<br> Avg Poverty Count: " + xinfo +
         "<br> + Number of Proprietary Ownership: " + yinfo;}
      else if (currentAxisLabelX === "avgPovCt"&& currentAxisLabelY==="government") 
        {return stateName + "<br> Avg Poverty Count: " + xinfo +
         "<br> + Number of Government Ownership: " + yinfo;}
      else if (currentAxisLabelX === "avgPovCt"&& currentAxisLabelY==="nonProfit") 
        {return stateName + "<br> Avg Poverty Count: " + xinfo +
         "<br> + Number of Non Profit Ownership: " + yinfo;}
         });
console.log(currentAxisLabelX, currentAxisLabelY);
// Create tooltip
chart.call(toolTip); 
chart.selectAll("circle")
  .data(hData)
  .enter().append("circle")
  .attr("cx",function(data, index)
    {return xLinearScale(+data[currentAxisLabelX]);})
  .attr("cy",function(data, index)
    {return yLinearScale(+data[currentAxisLabelY]);})
  .attr("r", "15")
  .attr("fill", "purple")
  .on("click", function(data){toolTip.show(data);})
  .on("mouseout", function(data, index){toolTip.hide(data);});
 

//Define data for text
var texts = svg.selectAll("text")
  .data(hData)
  .enter().append("text");
var textlabel = texts
  .attr("x",function(data){return xLinearScale(+data[currentAxisLabelX]);})
  .attr("y",function(data){return yLinearScale(+data[currentAxisLabelY]);})
  .text(function(data){return data.abbr})
  .attr("fill","gold")
  .attr("font-size", "9");

//Display y-axis
chart.append("g")
  .attr("class", "y-axis").call(leftAxis);
chart
  .append("text")
  .attr("transform","rotate(-90)")
  .attr("y", 0-margin.left + 10)
  .attr("x", 0- height/2)
  .attr("dy", "1em")
  .attr("class","y-axis-text activey")
  .attr("y-axis-name","proprietary")
  .text("Number of Proprietary Ownership");   
chart
  .append("text")
  .attr("transform","rotate(-90)")
  .attr("y", 0-margin.left + 30)
  .attr("x", 0- height/2)
  .attr("dy", "1em")
  .attr("class","y-axis-text inactivey")
  .attr("y-axis-name","government")
  .text("Number of Government Ownership");
chart
  .append("text")
  .attr("transform","rotate(-90)")
  .attr("y", 0-margin.left + 50)
  .attr("x", 0- height/2)
  .attr("dy", "1em")
  .attr("class","y-axis-text inactivey")
  .attr("y-axis-name","nonProfit")
  .text("Number of Non Profit Ownership");

//Display x-axis

 chart.append("g")
  .attr("transform", "translate(0," + height + ")")
  .attr("class", "x-axis")
  .call(bottomAxis);
 chart
  .append("text")
  .attr("transform", 
    "translate(" + width / 2 + "," + (height + margin.top + 20) + ")")
  //Active x-axis label
  .attr("class", "axis-text active")
  .attr("data-axis-name","avgPopulation")
  .text("Average Population");
  //Inactive x-axis label
chart.append("text")
  .attr("transform",
    "translate(" + width / 2 + "," + (height + margin.top + 45) + ")")
  .attr("class", "axis-text inactive")
  .attr("data-axis-name", "avgHHIncome")
  .text("Average Household Income");
chart.append("text")
  .attr("transform",
      "translate(" + width / 2 + "," + (height + margin.top + 70) + ")")
  .attr("class", "axis-text inactive")
  .attr("data-axis-name", "avgPovCt")
  .text("Average Poverty Count");

  // Change an axis's status from inactive to active when clicked (if it was inactive)
  // Change the status of all active axes to inactive otherwise
  //Display text in bubble


  function labelChange(clickedAxis) {
    d3.selectAll(".axis-text")
      .filter(".active")
      .classed("active", false)
      .classed("inactive", true);
  clickedAxis.classed("inactive",false).classed("active", true); }

  d3.selectAll(".axis-text").on("click", function()
  {var clickedSelection = d3.select(this);
  
  var isClickedSelectionInactive = clickedSelection.classed("inactive");
  
  var clickedAxis =clickedSelection.attr("data-axis-name");

  if (isClickedSelectionInactive)
    {currentAxisLabelX = clickedAxis;
        console.log(["current axis: ", clickedAxis],
                    ["current x axis: ",currentAxisLabelX],
                    ["current y axis: ",currentAxisLabelY]);
      
      findMinAndMax(currentAxisLabelX);
      xLinearScale.domain([xMin,xMax]);
      texts
      .attr("x",function(data){return xLinearScale(+data[currentAxisLabelX]);})
      .attr("y",function(data){return yLinearScale(+data[currentAxisLabelY]);})
    
    svg.select(".x-axis").transition().duration(1800).call(bottomAxis);
 
    d3.selectAll("circle").each(function() 
        {d3.select(this).transition().attr("cx", function(data) 
          {return xLinearScale(+data[currentAxisLabelX]);})
          .duration(1800);
        });
    labelChange(clickedSelection);}});

  function labelChangeY(clickedAxisY) {
    d3.selectAll(".y-axis-text")
      .filter(".activey")
      .classed("activey", false)
      .classed("inactivey", true);
  clickedAxisY.classed("inactivey",false).classed("activey", true); }

  d3.selectAll(".y-axis-text").on("click", function()
  {var clickedSelectionY = d3.select(this); 
  
  var isClickedSelectionInactiveY = clickedSelectionY.classed("inactivey");
  
  var clickedAxisY =clickedSelectionY.attr("y-axis-name");

  if (isClickedSelectionInactiveY)
   {currentAxisLabelY = clickedAxisY;
      console.log(["current axis: ", clickedAxisY],
                  ["current x axis: ",currentAxisLabelX],
                  ["current y axis: ",currentAxisLabelY]);
      
      findMinAndMaxY(currentAxisLabelY);
      yLinearScale.domain([0,yMax]);
      texts
      .attr("x",function(data){return xLinearScale(+data[currentAxisLabelX]);})
      .attr("y",function(data){return yLinearScale(+data[currentAxisLabelY]);})
    
    svg.select(".y-axis").transition().duration(1800).call(leftAxis);
 
    d3.selectAll("circle").each(function() 
        {d3.select(this).transition().attr("cy", function(data) 
          {return yLinearScale(+data[currentAxisLabelY]);})
          .duration(1800);
        });
    labelChangeY(clickedSelectionY);}});
});