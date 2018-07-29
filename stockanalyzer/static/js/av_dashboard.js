'use strict';

let timeseries = dataset['Time Series (Daily)'];
let timeseries_dates = [];
let timeseries_close = [];
for (var i in timeseries){
  timeseries_dates.push(i);
  timeseries_close.push(parseFloat(timeseries[i]['4. close']));
}

/* Add a basic data series with six labels and values */
let data = {
	labels: ['1', '2'], //[timeseries_dates],
  series: [
    {
      data: timeseries_close
    }
  ]
};

/* Set some base options (settings will override the default settings in Chartist.js *see default settings*). We are adding a basic label interpolation function for the xAxis labels. */
let options = {
  // axisX: {
  //   labelInterpolationFnc: function(value) {
  //     return 'Calendar Week ' + value;
  //   }
  // },
  height: '600px',
  width: '800px'
};

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
new Chartist.Line('#av-chart', data, options, responsiveOptions);

// var chart = new Chartist.Line('#av-timeseries', {
//   series: [
//     {
//       name: 'series-1',
//       data: [
//         {x: new Date(143134652600), y: 53},
//         {x: new Date(143234652600), y: 40},
//         {x: new Date(143340052600), y: 45},
//         {x: new Date(143366652600), y: 40},
//         {x: new Date(143410652600), y: 20},
//         {x: new Date(143508652600), y: 32},
//         {x: new Date(143569652600), y: 18},
//         {x: new Date(143579652600), y: 11}
//       ]
//     },
//     {
//       name: 'series-2',
//       data: [
//         {x: new Date(143134652600), y: 53},
//         {x: new Date(143234652600), y: 35},
//         {x: new Date(143334652600), y: 30},
//         {x: new Date(143384652600), y: 30},
//         {x: new Date(143568652600), y: 10}
//       ]
//     }
//   ]
// }, {
//   axisX: {
//     type: Chartist.FixedScaleAxis,
//     divisor: 5,
//     labelInterpolationFnc: function(value) {
//       return moment(value).format('MMM D');
//     }
//   }
// });
