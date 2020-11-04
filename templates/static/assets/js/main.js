

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
    
      //modal

    const modals = document.querySelector('.modal');
    M.Modal.init(modals, {});
  
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

	//dark mode
    let darkMode = localStorage.getItem('darkMode');
	
	const checkbox = document.querySelector('.checkbox');
	const main = document.querySelector('main');
	const header = document.querySelector('header');
	const body = document.querySelector('body');
	const footer = document.querySelector('footer');
	

	const activateDarkMode = () => {
		body.classList.add('dark');
		main.classList.add('dark');
		header.classList.add('dark');
		footer.classList.add('dark');

		localStorage.setItem("darkMode", "active");
	};
	
	const deactivateDarkMode = () => {
		main.classList.remove('dark');
		header.classList.remove('dark');
		footer.classList.remove('dark');
		body.classList.remove('dark');

		localStorage.setItem("darkMode", null);
	}

	if(darkMode === 'active'){
		activateDarkMode();
	}
	
	checkbox.addEventListener('change', () => {
		darkMode = localStorage.getItem('darkMode');
		if(darkMode !== "active"){
			activateDarkMode();
		}else{
			deactivateDarkMode();
		}	
		
	});
    
    //  msg
    const message = document.querySelector('.msg');
    const closeBtn = document.querySelector('.close-btn');

    closeBtn.addEventListener('click', () => {
        message.style.display="none";
    });

    
});


















