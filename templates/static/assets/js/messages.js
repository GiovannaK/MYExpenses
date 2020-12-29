//  msg

document.addEventListener('DOMContentLoaded', () => {
    const message = document.querySelector('.msg');
    const closeBtn = document.querySelector('.close-msg');

    if(message){
        const closeMsg = () => {
            message.style.display = 'none';
        }
        
        const executeCloseMsg = () => {
            closeBtn.addEventListener('click', closeMsg);
        }        

        executeCloseMsg();
    }
    
});



