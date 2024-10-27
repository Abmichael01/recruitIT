// search functionality

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



// delete student
const  deleteStudentButts = document.querySelectorAll(".student-delete")

if(deleteStudentButts){
    deleteStudentButts.forEach(deleteStudentButt=>{
        deleteStudentButt.addEventListener("click", ()=>{
            
            const confirmDelete = confirm("Are you sure you want to delete this student's account")

            if(confirmDelete){
                const student_id = deleteStudentButt.dataset.id
                const formData = new FormData()
                formData.append("student_id", student_id)
                fetch("/ubit/delete-student", {
                    body: formData,
                    method: "POST",
                })
                .then(response=>response.json())
                .then(data=>{
                    if(data.deleted){
                        location.reload()
                    }
                })
            }
            
        })
    })
}


// delete company
const  deleteCompanyButts = document.querySelectorAll(".company-delete")

if(deleteCompanyButts){
    deleteCompanyButts.forEach(deleteCompanyButt=>{
        deleteCompanyButt.addEventListener("click", ()=>{
            
            const confirmDelete = confirm("Are you sure you want to delete this company's account")

            if(confirmDelete){
                const company_id = deleteCompanyButt.dataset.id
                const formData = new FormData()
                formData.append("company_id", company_id)
                fetch("/ubit/delete-company", {
                    body: formData,
                    method: "POST",
                })
                .then(response=>response.json())
                .then(data=>{
                    if(data.deleted){
                        location.reload()
                    }
                })
            }
            
        })
    })
}

// delete application
const  deleteApplicationButts = document.querySelectorAll(".application-delete")

if(deleteApplicationButts){
    deleteApplicationButts.forEach(deleteApplicationButt=>{
        deleteApplicationButt.addEventListener("click", ()=>{
            
            const confirmDelete = confirm("Are you sure you want to delete this application")

            if(confirmDelete){
                const application_id = deleteApplicationButt.dataset.id
                const formData = new FormData()
                formData.append("application_id", application_id)
                fetch("/cancel-application", {
                    body: formData,
                    method: "POST",
                })
               .then(response=>response.json())
               .then(data=>{
                    if(data.canceled){
                        location.reload()
                    }
                })
            }
            
        })
    })
}

// delete recruitment

const  deleteRecruitmentButts = document.querySelectorAll(".recruitment-delete")

if(deleteRecruitmentButts){
    deleteRecruitmentButts.forEach(deleteRecruitmentButt=>{
        deleteRecruitmentButt.addEventListener("click", ()=>{
            
            const confirmDelete = confirm("Are you sure you want to delete this recruitment")

            if(confirmDelete){
                const recruitment_id = deleteRecruitmentButt.dataset.id
                const formData = new FormData()
                formData.append("recruitment_id", recruitment_id)
                fetch("/delete-recruitment", {
                    body: formData,
                    method: "POST",
                })
               .then(response=>response.json())
               .then(data=>{
                    if(data.deleted){
                        location.reload()
                    }
                })
            }
            
        })
    })
}


