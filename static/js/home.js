const statesFilterForm = document.querySelector(".filter-form")


if (statesFilterForm){
    const statesFilter = statesFilterForm.querySelector("select")
    statesFilter.addEventListener("input", ()=>{
        statesFilterForm.submit()
    })
}