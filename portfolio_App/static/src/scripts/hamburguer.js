const hamburger = document.getElementById('hamburger')
const navbarList = document.getElementById('navbar-list')

hamburger.addEventListener('click', () => {
    navbarList.classList.toggle('active');
})

document.addEventListener('click', (event) => {
    if(!navbarList.contains(event.target) && !hamburger.contains(event.target)){
        navbarList.classList.remove('active')
    }
})