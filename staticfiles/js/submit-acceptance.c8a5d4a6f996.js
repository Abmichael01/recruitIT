const letterLabel = document.querySelector(".upload-cont label span")
const letterP = document.querySelector(".upload-cont p")
const letterInput = document.querySelector(".upload-cont input")
const letterUrl = letterInput.dir

letterInput.addEventListener("input", ()=>{
    letterP.textContent = letterInput.files[0].name
    letterLabel.textContent = "Edit IT letter"

})


const phoneInputs = document.querySelectorAll(".phone-input")

phoneInputs.forEach(phoneInput => {
    phoneInput.addEventListener("input", ()=>{
        phoneInput.value = phoneInput.value.replace(/[^0-9]/g, '')
    
    })
});

const matricInput = document.querySelector(".matric-input")