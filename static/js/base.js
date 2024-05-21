// navbar
const search = document.querySelector(".search")
const cancelSearch = document.querySelector(".cancel-search")

search.addEventListener("input", ()=>{
    searchInput = search.value
    if(searchInput != ""){
        cancelSearch.style.display = "inline-block"
    }else{
        cancelSearch.style.display = "none"
    }
})

cancelSearch.addEventListener("click", ()=>{
    search.value = ""
    cancelSearch.style.display = "none"
})

const userLink = document.querySelector(".user-link-main")
const dropdown = document.querySelector(".dropdown")
const arrowDown = document.querySelector(".arrow-down")
userLink.addEventListener("click", ()=>{
    dropdown.classList.toggle("dropdown-active")
    arrowDown.classList.toggle("rotate-arrow")
})

document.addEventListener("click", (event) => {
    if (!userLink.contains(event.target) && !dropdown.contains(event.target)) {
        dropdown.classList.remove("dropdown-active")
        arrowDown.classList.remove("rotate-arrow")
    }
});


const notificationLink = document.querySelector(".notification-link")
const unseenCount = notificationLink.querySelector("span")
setInterval(()=>{
    fetch("/get-unseen-notifications",)
    .then(response=>response.json())
    .then(data=>{
        if(data.unseen_count != 0){
            unseenCount.style.display = "block"
            unseenCount.textContent = data.unseen_count
        }
    })
}, 1000)









// recruitment
const recruitments = document.querySelectorAll(".recruitment")
recruitments.forEach(recruitment=>{
    // options
    const optionsIcon = recruitment.querySelector(".options-menu")
    const options = recruitment.querySelector(".options")
    optionsIcon.addEventListener("click", ()=>{
        options.classList.toggle("options-active")
    })

    document.addEventListener("click", (event) => {
        if (!options.contains(event.target) && !optionsIcon.contains(event.target)) {
            // Clicked outside of the options menu and options icon, close the menu
            options.classList.add("options-active");
        }
    });

    // copy recruitment link
    const copyRecruitmentLinkButts = recruitment.querySelectorAll(".copy-recruitment-link-butt")
    copyRecruitmentLinkButts.forEach(copyRecruitmentLinkButt=>{
        copyRecruitmentLinkButt.addEventListener("click", ()=>{
            baseUrl = window.location.origin
            link = baseUrl + copyRecruitmentLinkButt.dataset.url
            navigator.clipboard.writeText(link)
            
            const copyButtText = copyRecruitmentLinkButt.querySelector("span")
            copyButtText.textContent = "Link Copied!"
            setTimeout(()=>{
                copyButtText.textContent = "Copy Link"
            }, 5000)
        })
    })


    // show less company bio 
    const companyBio = recruitment.querySelector(".company-bio")

    if (companyBio.textContent.length >= 50){
        companyBio.textContent = companyBio.textContent.substring(0, 50) + "..."
    }


    // description show less and show more
    const recruitmentDescription = recruitment.querySelector(".description")
    
    var description = recruitmentDescription.textContent.trim()

    if (description.length > 200){
        recruitmentDescription.textContent = recruitmentDescription.textContent.substring(0, 200) + "..."
    }
    

    const seeMore = recruitment.querySelector(".see-more")
    if (description.length <= 200){
        seeMore.style.display = "none"
    }else{
        seeMore.addEventListener("click", ()=>{
        
            if(seeMore.textContent == "See more..."){
                recruitmentDescription.textContent = description
                seeMore.textContent = "See less"
            }else{
                recruitmentDescription.textContent = description.substring(0, 200) + "..."
                seeMore.textContent = "See more..."
                // recruitment.scrollIntoView()
            }
        })
    }

    


    // delete recruitment
    const deleteRecruitmentButt = recruitment.querySelector(".delete-recruitment")

    if (deleteRecruitmentButt){
        deleteRecruitmentButt.addEventListener("click", ()=>{
            confirmDelete = confirm("Are you sure you want to delete this recruitment?")
    
            if(confirmDelete){
                const recruitment_id = deleteRecruitmentButt.dataset.id
    
                formData = new FormData()
                formData.append("recruitment_id", recruitment_id)
    
                fetch("/delete-recruitment", {
                    body: formData,
                    method: "POST",
                })
                .then(res=>res.json())
                .then(data=>{
                    if(data.deleted){
                        location.reload()
                    }
                })
            }  
        })
    }

})










// post recruitment
const addRecruitmentButt = document.querySelector(".add-recruitment-butt")
const addRecruitmentCont = document.querySelector(".add-recruitment-cont")
const addRecruitmentCancelButt = document.querySelector(".add-recruitment .cancel-butt")

if(addRecruitmentButt){
    addRecruitmentButt.addEventListener("click", ()=>{
        addRecruitmentCont.style.display = "flex"
    })
}

addRecruitmentCancelButt.addEventListener("click", ()=>{
    addRecruitmentCont.style.display = "none"
    var title = document.querySelector(".add-recruitment .title");
    var description = document.querySelector(".add-recruitment .description");
    var image = document.querySelector(".add-recruitment .image");
    var seats = document.querySelector(".add-recruitment .seats");

    title.value = ""
    description.value = ""
    seats.value = ""
    image.value = ""
})


const addRecruitPic = document.querySelector(".add-recruitment .image-input-cont img")
const addRecruitPicInput = document.querySelector(".add-recruitment #add-image-input")
const imgUrl = addRecruitPicInput.dir

addRecruitPicInput.addEventListener("input", ()=>{
    if (addRecruitPicInput.files && addRecruitPicInput.files[0]){

        var reader = new FileReader()

        reader.onload =  function (e) {
            var imgUrl = e.target.result

            addRecruitPic.src = imgUrl
            addRecruitPic.style.display = "block"
        }
        reader.readAsDataURL(addRecruitPicInput.files[0])
    }
})


const addRecruitment = document.querySelector(".add")
const addNotProcessing = document.querySelector(".add .not_pro")
const addProcessing = document.querySelector(".add .pro")
const addRecruitmentForm = document.querySelector(".add-recruitment")
const formError = document.querySelector(".add-recruitment .info") 


addRecruitment.addEventListener("click", (event)=>{
    event.preventDefault()

    const title = document.querySelector(".add-recruitment .title").value;
    const description = document.querySelector(".add-recruitment .description").value;
    const image = document.querySelector(".add-recruitment .image").files[0];
    const seats = document.querySelector(".add-recruitment .seats").value;

    const formData = new FormData();
    formData.append("title", title);
    formData.append("description", description);
    formData.append("image", image);
    formData.append("seats", seats);

    addNotProcessing.style.display = "none"
    addProcessing.style.display = "block"
    
    addRecruitment.style.cursor = "not-allowed"
    
    fetch("/add-recruitment", {
        body: formData,
        method: "POST",
    }).then(res=>res.json()).then(data=>{
        addNotProcessing.style.display = "block"
        addProcessing.style.display = "none"
        if(data.input_error){
            formError.textContent = data.input_error
            formError.style.display = "block"
            addRecruitmentForm.scrollTop = 0
            addRecruitment.style.cursor = "pointer"
        }else{
            location.reload()
        }
    })
    .catch(error=>{
        console.log(error)
    })
})




const saveRecruitmentButts = document.querySelectorAll(".save-recruitment-butt")

if (saveRecruitmentButts){
    saveRecruitmentButts.forEach(saveRecruitmentButt=>{
        saveRecruitmentButt.addEventListener("click",()=>{
            r_id = saveRecruitmentButt.dataset.id
            const formData = new FormData()
            formData.append("recruitment_id", r_id)
            const saveButtText = saveRecruitmentButt.querySelector("span")
    
            fetch("/save-recruitment", {
                body: formData,
                method: "POST",
            })
            .then(res=>res.json())
            .then(data=>{
                if(data.status){
                    saveButtText.textContent = data.status
                    console.log("working")
                }
            })
        })
    })
}
















// application
const applicationButts = document.querySelectorAll(".application-butt")
const applicationCont = document.querySelector(".application-cont")
const applicationCancelButt = document.querySelector(".application .cancel-butt")
var recruitmentId

if(applicationButts){
    applicationButts.forEach(applicationButt=>{
        applicationButt.addEventListener("click", ()=>{

            applicationCont.style.display = "flex"
            recruitmentId = applicationButt.dataset.id
        })
    })
}


applicationCancelButt.addEventListener("click", ()=>{
    applicationCont.style.display = "none"
    // var title = document.querySelector(".add-recruitment .title");
    // var description = document.querySelector(".add-recruitment .description");
    // var image = document.querySelector(".add-recruitment .image");
    // var seats = document.querySelector(".add-recruitment .seats");

    // title.value = ""
    // description.value = ""
    // seats.value = ""
    // image.value = ""
})


const letterLabel = document.querySelector(".application .doc-input-cont label")
const letterP = document.querySelector(".application .doc-input-cont p")
const letterInput = document.querySelector(".application #add-doc-input")
const letterUrl = letterInput.dir

letterInput.addEventListener("input", ()=>{
    letterP.textContent = letterInput.files[0].name
    letterLabel.textContent = "Edit IT letter"

})


const applyButt = document.querySelector(".apply-butt")
const applyNotProcessing = document.querySelector(".apply-butt .not_pro")
const applyProcessing = document.querySelector(".apply-butt .pro")
const applicationForm = document.querySelector(".application")
const applicationError = document.querySelector(".application .info") 



applyButt.addEventListener("click", (event)=>{
    event.preventDefault()

    const recruitment_id = recruitmentId
    const name = document.querySelector(".application .name").value;
    const matricNo = document.querySelector(".application .matric-no").value;
    const letter = document.querySelector(".application .letter").files[0];
    const email = document.querySelector(".application .email").value;

    const formData = new FormData();
    formData.append("recruitment_id", recruitment_id);
    formData.append("name", name);
    formData.append("matric-no", matricNo);
    formData.append("letter", letter);
    formData.append("email", email);

    applyNotProcessing.style.display = "none"
    applyProcessing.style.display = "block"
    
    applyButt.style.cursor = "not-allowed"
    
    fetch("/apply", {
        body: formData,
        method: "POST",
    }).then(res=>res.json()).then(data=>{
        console.table(data)
        applyNotProcessing.style.display = "block"
        applyProcessing.style.display = "none"
        if(data.input_error){
            applicationError.textContent = data.input_error
            applicationError.style.display = "block"
            applicationForm.scrollTop = 0
            applyButt.style.cursor = "pointer"
        }
        else{
            location.reload()
        }
        
    })
    .catch(error=>{
        console.log(error)
    })
})










// approve application
const approveApplicationButts = document.querySelectorAll(".approve-application-butt")
const approveApplicationCont = document.querySelector(".approve-application-cont")
const approveApplicationCancelButt = document.querySelector(".approve-application .cancel-butt")
const approveloading = document.querySelector(".approve-application .loading")
var applicationId
var applicantEmail
 
if(approveApplicationButts){
    approveApplicationButts.forEach(approveApplicationButt=>{
        approveApplicationButt.addEventListener("click", ()=>{

            approveApplicationCont.style.display = "flex"
            applicationId = approveApplicationButt.dataset.id

            const formData = new FormData();
            formData.append("application_id", applicationId)

            fetch('/get-application-info',{
                body: formData,
                method: "POST",
            })
            .then(res=>res.json())
            .then(data=>{
                applicantEmail = data.applicant_email
                console.log(applicantEmail)
                approveloading.style.display = "none"

                const applicant_email = document.querySelector(".approve-application .applicant-email");

                applicant_email.value = applicantEmail
            })
        })
    })
}

approveApplicationCancelButt.addEventListener("click", ()=>{
    approveApplicationCont.style.display = "none"
    // var description = document.querySelector(".add-recruitment .description");

    // description.value = ""
})


const approveButt = document.querySelector(".approve-butt")
const approveNotProcessing = document.querySelector(".approve-butt .not_pro")
const approveProcessing = document.querySelector(".approve-butt .pro")
const approveApplicationForm = document.querySelector(".approve-application")
const approveApplicationError = document.querySelector(".approve-application .info")



approveButt.addEventListener("click", (event)=>{
    event.preventDefault()

    const application_id = applicationId
    const company_email = document.querySelector(".approve-application .company-email").value;
    const applicant_email = document.querySelector(".approve-application .applicant-email").value;
    const message =  document.querySelector(".message").value;


    const formData = new FormData();
    formData.append("application_id", application_id)
    formData.append("company_email", company_email)
    formData.append("applicant_email", applicant_email)
    formData.append("message", message)

    approveNotProcessing.style.display = "none"
    approveProcessing.style.display = "block"
    
    approveButt.style.cursor = "not-allowed"
    
    fetch("/approve-application", {
        body: formData,
        method: "POST",
    }).then(res=>res.json()).then(data=>{
        console.table(data)
        approveNotProcessing.style.display = "block"
        approveProcessing.style.display = "none"
        if(data.input_error){
            approveApplicationError.textContent = data.input_error
            approveApplicationError.style.display = "block"
            approveApplicationForm.scrollTop = 0
            applyButt.style.cursor = "pointer"
        }
        else{
            location.reload()
        }
        
    })
    .catch(error=>{
        console.log(error)
    })
})








// cancel application
const cancelApplicationButts = document.querySelectorAll(".cancel-application-butt")

cancelApplicationButts.forEach(cancelApplicationButt=>{
    cancelApplicationButt.addEventListener("click", ()=>{
        confirmCancel = confirm("Are you sure you want to cancel this application?")

        if(confirmCancel){
            const application_id = cancelApplicationButt.dataset.id

            formData = new FormData()
            formData.append("application_id", application_id)

            fetch("/cancel-application", {
                body: formData,
                method: "POST",
            })
            .then(res=>res.json())
            .then(data=>{
                if(data.canceled){
                    location.reload()
                }
            })
        }
       

    })    
})