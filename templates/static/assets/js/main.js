document.addEventListener('DOMContentLoaded', () => {
    // Navbar
    let elems = document.querySelectorAll('.sidenav');
    let instances = M.Sidenav.init(elems, {});

    // colapsible sidenav
    const collapsible = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsible, {});

    //  float btn
    const floatBtn = document.querySelectorAll('.fixed-action-btn');
    M.FloatingActionButton.init(floatBtn, {});

    // select form
    const select = document.querySelectorAll('select');
    M.FormSelect.init(select, {});

    //tabs
    const tabs = document.querySelectorAll('.tabs');
    M.Tabs.init(tabs, {});
    
    // parallax
    const parallax = document.querySelectorAll('.parallax');
    M.Parallax.init(parallax, {});
  
	// slide

	const slider = document.querySelectorAll('.slider');
	M.Slider.init(slider, {
		height: 600,
		indicators: false,
	}); 
    
    //tooltips
	const tooltips = document.querySelectorAll('.tooltipped');
    
    M.Tooltip.init(tooltips, {});
	//scrollspy
	const scrollspy = document.querySelectorAll('.scrollspy');
    M.ScrollSpy.init(scrollspy, {});

    //datepicker 

    const datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        i18n: {
            months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
            monthsShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
            weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo'],
            weekdaysShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
            weekdaysAbbrev: ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'],
            today: 'Hoje',
            clear: 'Limpar',
            cancel: 'Sair',
            done: 'Confirmar',
            labelMonthNext: 'Próximo mês',
            labelMonthPrev: 'Mês anterior',
            labelMonthSelect: 'Selecione um mês',
            labelYearSelect: 'Selecione um ano',
            selectMonths: true,
            selectYears:30,
        },
        yearRange: 30,
        format: 'dd/mm/yyyy'
    });
    
    // selected currency

    let obj = document.querySelector('select[name=currency]')

    if(obj){
        const selectedCurrency = () => {
            for(i=0; i < obj.options.length; i++){
                if(obj.options[i].value == 18){
                    obj.selectedIndex = i;
                }
            }
        }
        
        selectedCurrency();
    }
    
  
});

