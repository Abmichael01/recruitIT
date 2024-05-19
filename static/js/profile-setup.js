const picture = document.querySelector(".picture")
const pictureInput = document.querySelector("#picture-input")


const skillInput = document.querySelector(".skill-input")
const skillInputField = document.querySelector(".skill-input-field")
const skillsCont = document.querySelector(".skills-cont")



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


const phoneInputs = document.querySelectorAll(".phone-input")

phoneInputs.forEach(phoneInput => {
    phoneInput.addEventListener("input", ()=>{
        phoneInput.value = phoneInput.value.replace(/[^0-9]/g, '')
    
    })
});

const matricInput = document.querySelector(".matric-input")







skillInput.addEventListener("keydown", (e)=>{
    if (e.key == "Enter"){
        e.preventDefault()

        const skillCont = document.createElement("div")
        skillCont.style.display = "flex"
        skillCont.classList.add("skill")
        skillsCont.appendChild(skillCont)

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

