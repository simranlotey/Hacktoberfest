const loginbox = document.querySelector('.login-box');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const navbtnlog = document.querySelector('#login-button')
const closebutton=document.querySelector('.close');

registerLink.addEventListener('click',()=>{
    loginbox.classList.add('active');
})
loginLink.addEventListener('click',()=>{
    loginbox.classList.remove('active');
})

navbtnlog.addEventListener('click',()=>{
    loginbox.classList.add('active-popup');
})

closebutton.addEventListener('click',()=>{
    loginbox.classList.remove('active-popup');
})