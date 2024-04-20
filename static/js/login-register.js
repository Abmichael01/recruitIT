const emailInput = document.querySelector(".email-input");
const emailField = document.querySelector(".email-field");
const emailError = document.querySelector(".email-error");
const loader = document.querySelector(".loader");
const submitBtn = document.querySelector(".submit");


submitBtn.disabled = true
submitBtn.classList.add("submit-disabled")

emailInput.addEventListener("keyup", (event)=>{
    emailVal = event.target.value;
    
    emailError.textContent = "";
    emailField.classList.remove("error");

    if(emailVal.length > 0){
        loader.style.display = "inline-block"
        fetch("/authenticate/validate-email", {
            body: JSON.stringify({email: emailVal}),
            method: "POST"
        }).then(res=>res.json()).then(data=>{
            loader.style.display = "none"
            if(data.email_error){
                emailError.textContent = data.email_error;
                emailField.classList.add("error");
                submitBtn.disabled = true
                submitBtn.classList.add("submit-disabled")
                
            }else{
                submitBtn.disabled = false
                submitBtn.classList.remove("submit-disabled")
                
            }
        })
    }
})


const passwordInput = document.querySelector(".password-input")
const passwordError = document.querySelector(".pswd-error")
const passwordField = document.querySelector(".password-field")
const form = document.querySelector("form")


passwordInput.addEventListener("input", ()=>{
    passwordError.textContent = ""
    passwordError.classList.remove("error")
    passwordField.classList.remove("error") 
    if(passwordInput.value.length < 8){
        passwordError.textContent = "Password cannot be less than 8 characters"
        passwordError.classList.add("error")
        passwordField.classList.add("error") 
    }
})




function checkInputs(){

    if(emailInput.value == ""){
        emailError.textContent = "email field cannot be empty";
        emailField.classList.add("error");
        submitBtn.classList.add("submit-disabled")
    }else if(passwordInput.value.length < 8){
        passwordError.textContent = "Password cannot be less than 8 characters"
        passwordError.classList.add("error")
        passwordField.classList.add("error") 
    }else{
        form.submit()
    }
}

form.addEventListener("submit", (e)=>{
    e.preventDefault()

    checkInputs()

})

