const Box = document.querySelector('.Box');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');


 

registerLink.addEventListener('click',()=>{
    Box.classList.add('active');    
})

loginLink.addEventListener('click',()=>{
    Box.classList.remove('active');    
})

btnPopup.addEventListener('click',()=>{
    Box.classList.add('active-popup');    
})

iconClose.addEventListener('click',()=>{
    Box.classList.remove('active-popup');    
})
