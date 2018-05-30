'use strict';

let timeseries = dataset['Time Series (Daily)'];
let timeseries_dates = [];
let timeseries_close = [];
for (var i in timeseries){
  timeseries_dates.push(i);
  timeseries_close.push(parseFloat(timeseries[i]['4. close']));
}
// timeseries_close = timeseries_close.slice(0,10);
console.log(timeseries_close);

/* Add a basic data series with six labels and values */
let data = {
	labels: [timeseries_dates], //['1', '2', '3', '4', '5', '6'],
  series: [
    {
      data: timeseries_close //[1, 2, 3, 5, 8, 13]
    }
  ]
};

/* Set some base options (settings will override the default settings in Chartist.js *see default settings*). We are adding a basic label interpolation function for the xAxis labels. */
// let options = {
//   axisX: {
//     labelInterpolationFnc: function(value) {
//       return 'Calendar Week ' + value;
//     }
//   }
// };

/* Now we can specify multiple responsive settings that will override the base settings based on order and if the media queries match. In this example we are changing the visibility of dots and lines as well as use different label interpolations for space reasons. */
let responsiveOptions = [
  ['screen and (min-width: 641px) and (max-width: 1024px)', {
    showPoint: false,
    axisX: {
      labelInterpolationFnc: function(value) {
        return 'Week ' + value;
      }
    }
  }],
  ['screen and (max-width: 640px)', {
    showLine: false,
    axisX: {
      labelInterpolationFnc: function(value) {
        return 'W' + value;
      }
    }
  }]
];

/* Initialize the chart with the above settings */
new Chartist.Line('#av-chart', data, responsiveOptions);
