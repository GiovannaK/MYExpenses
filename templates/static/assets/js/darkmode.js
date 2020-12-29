//dark mode
let darkMode = localStorage.getItem('darkMode');
	
const checkbox = document.querySelector('.checkbox');

const activateDarkMode = () => {
	document.querySelector('#dark-style').href = staticDarkThemePath + "/dark.css";
	localStorage.setItem("darkMode", "active");
};

const deactivateDarkMode = () => {
	document.querySelector('#dark-style').href = static + "/main.css"
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