const statesFilterForm = document.querySelector(".filter-form")
const statesFilter = statesFilterForm.querySelector("select")

statesFilter.addEventListener("input", ()=>{
    statesFilterForm.submit()
})