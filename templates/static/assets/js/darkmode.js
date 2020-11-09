 /* //dark mode
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
    
});   */