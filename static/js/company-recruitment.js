const pointer = document.querySelector(".pointer")
const activeNav = document.querySelector(".recruitments-nav .active")
const pausedNav = document.querySelector(".recruitments-nav .paused")

activeNav.addEventListener("click", ()=>{
    parentElement = activeNav.parentElement

    middlePosition = parentElement.offsetLeft + (activeNav.offsetWidth/2)
    pointer.style.left = middlePosition
})

pausedNav.addEventListener("click", ()=>{
    parentElement = pausedNav.parentElement

    middlePosition = parentElement.offsetLeft + (pausedNav.offsetWidth/2)
    pointer.style.left = middlePosition
})