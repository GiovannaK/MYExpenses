// global settings

Chart.defaults.global.defaultFontFamily = 'Verdana';

// earnings in the current year
let earningsCurrentYear = document.querySelector('#earningsCurrentYear').getContext('2d');

let earningsCurrentYearDashboard = new Chart(earningsCurrentYear, {
    type: 'line',
    data: {
        labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 
        'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'dezembro'
        ],
        
        datasets: [{
            label: 'Ganhos',
            data:[
                3000, 2000, 5000, 6000, 5000, 7000, 1000, 4000, 2300, 
                10000, 5600, 13500            
            ],

            borderColor: 'rgba(64, 236, 64, 1)',
            fill: false,
            lineTension: 0,
        }],
    },
    options: {
        title:{
            display: true,
            text: 'Ganhos no perído de janeiro a dezembro do ano atual',
            fontSize: 20
        },
        maintainAspectRatio: false,
    }
});

// earnings in the current month

let earningsCurrentMonth = document.querySelector('#earningsCurrentMonth').getContext('2d');

let earningsCurrentMonthDashboard = new Chart(earningsCurrentMonth, {
    type: 'bar',
    data: {
        labels: [
            'Primeira semana', 'Segunda semana', 'Terceira semana', 'Quarta semana'
        ],
        
        datasets: [{
            label: 'Ganhos no mês atual',
            data:[
                3000, 2700, 5000, 6000,           
            ],

            backgroundColor: [
                'rgba(255, 153, 0, 0.61)',
                'rgba(0, 132, 255, 0.637)',
                'rgba(64, 236, 64, 0.534)',
                'rgba(255, 0, 0, 0.507)',
                
            ]
        }],
    },
    options: {
        title:{
            display: true,
            text: 'Ganhos da primeira a quarta semana do mês atual',
            fontSize: 20
        },
        maintainAspectRatio: false,
    }
});

//earnings per category

let earningsCategory = document.querySelector('#earningsCategory').getContext('2d');

let earningsCategoryDashboard = new Chart(earningsCategory, {
    type: 'doughnut',
    data: {
        labels: [
            'Salário', 'Investimentos', 'Freelance', 'Imóveis'
        ],
        
        datasets: [{
            label: 'Ganhos por categoria',
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
            text: 'Ganhos por categoria no mês atual',
            fontSize: 20
        },
        maintainAspectRatio: false,
    }
});

// earnings in the last 5 months

let earningsLastFiveMonths = document.querySelector('#earningsLastFiveMonths').getContext('2d');

let earningslastFiveMonthsDashboard = new Chart(earningsLastFiveMonths, {
    type: 'bar',
    data: {
        labels: [
            '2016', '2017', '2018', '2019', '2020'
        ],
        
        datasets: [{
            label: 'Ganhos por ano',
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
            text: 'Total de ganhos por ano nos últimos cinco anos',
            fontSize: 20
        },
        maintainAspectRatio: false,
    }
});
