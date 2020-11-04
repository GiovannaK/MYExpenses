// charts js -> current year dashboard

let yearDash = document.querySelector('#yearDash').getContext('2d');


// global settings

Chart.defaults.global.defaultFontFamily = 'Verdana';
//Chart.defaults.global.defaultFontSize = 18;

let yearExpenseChart = new Chart(yearDash, {
    type: 'line',
    data: {
        labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 
        'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'dezembro'
        ],
        
        datasets: [{
            label: 'Gastos',
            data:[
                3000, 2000, 5000, 6000, 5000, 7000, 1000, 4000, 2300, 
                10000, 5600, 13500            
            ],

            borderColor: 'rgba(255, 0, 0, 0.507)',
            fill: false,
            lineTension: 0,
        }],
    },
    options: {
        title:{
            display: true,
            text: 'Gastos no perído de janeiro a dezembro do ano atual',
            fontSize: 20
        },
        maintainAspectRatio: false,
    }
});

// current month dashboard

let currentMonthDash = document.querySelector('#currentMonthDash').getContext('2d')

let currentMonthExpenseChart = new Chart(currentMonthDash, {
    type: 'bar',
    data: {
        labels: [
            'Primeira semana', 'Segunda semana', 'Terceira semana', 'Quarta semana'
        ],
        
        datasets: [{
            label: 'Gastos no mês atual',
            data:[
                3000, 2700, 5000, 6000,           
            ],

            backgroundColor: [
                'rgba(0, 132, 255, 0.637)',
                'rgba(255, 153, 0, 0.61)',
                'rgba(255, 0, 0, 0.507)',
                'rgba(64, 236, 64, 0.534)'
            ]
        }],
    },
    options: {
        title:{
            display: true,
            text: 'Gastos da primeira a quarta semana do mês atual',
            fontSize: 20
        },
        maintainAspectRatio: false,
    }
});

// expenses per category

let category = document.querySelector('#category').getContext('2d');

let expensesPerCategoryDashboard = new Chart(category, {
    type: 'doughnut',
    data: {
        labels: [
            'Alimentação', 'Saúde', 'Educação', 'Serviços de assinatura'
        ],
        
        datasets: [{
            label: 'Gastos por categoria',
            data:[
                3000, 2700, 5000, 6000,           
            ],

            backgroundColor: [
                'rgba(0, 132, 255, 0.637)',
                'rgba(255, 153, 0, 0.61)',
                'rgba(255, 0, 0, 0.507)',
                'rgba(64, 236, 64, 0.534)'
            ]
            
        }],
    },
    options: {
        title:{
            display: true,
            text: 'Gastos por categoria no mês atual',
            fontSize: 20
        },
        maintainAspectRatio: false,
    }
});

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