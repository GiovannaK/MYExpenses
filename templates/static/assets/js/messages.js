//  msg
const message = document.querySelector('.msg');
const closeBtn = document.querySelector('.close-msg');

closeBtn.addEventListener('click', closeMsg);

function closeMsg(){
    message.style.display = 'none';
}
