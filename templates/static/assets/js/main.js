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

	
});





















