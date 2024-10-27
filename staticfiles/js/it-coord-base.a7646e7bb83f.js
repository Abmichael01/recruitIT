const search = document.querySelector(".search-box")
const rows = document.querySelectorAll(".rows")

if (search && rows){
    search.addEventListener("input", ()=>{
        searchInput = search.value.toLowerCase()
        if(searchInput!= ""){
            rows.forEach((row)=>{
                var text
                rowChildren = Array.from(row.children)
    
                rowChildren.forEach(child=>{
                    if(child.classList.contains("data")){
                        text += child.textContent.toLowerCase()
                    }
                })
    
                
                if(text.includes(searchInput)){
                    row.style.display = "table-row"
                }else{
                    row.style.display = "none"
                }
            })
        }else{
            rows.forEach((row)=>{
                row.style.display = "table-row"
            })
        }
    })
}