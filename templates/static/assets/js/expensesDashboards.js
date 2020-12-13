// charts js -> current year dashboard




// global settings

Chart.defaults.global.defaultFontFamily = 'Verdana';
//Chart.defaults.global.defaultFontSize = 18;






// expenses in the last 5 years

let lastFiveMonths = document.querySelector('#lastFiveMonths').getContext('2d');

let expenseslastFiveMonthsDashboard = new Chart(lastFiveMonths, {
    type: 'bar',
    data: {
        labels: [
            '2016', '2017', '2018', '2019', '2020'
        ],
        
        datasets: [{
            label: 'Gastos por ano',
            data:[
                3000, 2700, 5000, 6000, 3000          
            ],

            backgroundColor: [
                'rgba(255, 153, 0, 0.61)',
                'rgba(255, 0, 0, 0.507)',
                'rgba(64, 236, 64, 0.534)', 
                'rgba(0, 132, 255, 0.637)',
                'green'
            ] 
        }],
    },
    options: {
        title:{
            display: true,
            text: 'Total de gastos por ano nos últimos cinco anos',
            fontSize: 20
        },
        maintainAspectRatio: false,
    }
});