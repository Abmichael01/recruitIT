const picture = document.querySelector(".picture")
const pictureInput = document.querySelector("#picture-input")
const phoneInput = document.querySelector(".phone-input")


const skillInput = document.querySelector(".skill-input")
const skillInputField = document.querySelector(".skill-input-field")



const imgUrl = pictureInput.dir

pictureInput.addEventListener("input", ()=>{
    if (pictureInput.files && pictureInput.files[0]){

        var reader = new FileReader()

        reader.onload =  function (e) {
            var imgUrl = e.target.result

            picture.src = imgUrl
        }
        reader.readAsDataURL(pictureInput.files[0])
    }
})



phoneInput.addEventListener("input", ()=>{
    inputval = phoneInput.value
    phoneInput.value = inputval.replace(/[^0-9]/g, "")
})


skillInput.addEventListener("keydown", (e)=>{
    if (e.key == "Enter"){
        e.preventDefault()

        skillCont = document.createElement("div")
        skillCont.style.display = "flex"
        skillCont.classList.add("skill")
        skillInputField.appendChild(skillCont)

        newSkill = document.createElement("span")
        newSkill.textContent = skillInput.value
        skillCont.appendChild(newSkill)

        removeSkill = document.createElement("i")
        removeSkill.classList.add("fa-solid")
        removeSkill.classList.add("fa-xmark")
        removeSkill.classList.add("remove-skill")
        skillCont.appendChild(removeSkill)

        skillInput.value = ""

        removeSkill.addEventListener("click", (event)=>{
            clicked = event.target

            toBeRemoved = clicked.parentNode
            toBeRemoved.remove()
        })
    }

})

