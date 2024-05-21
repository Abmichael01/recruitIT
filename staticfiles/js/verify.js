const input = document.querySelector('.code-input')
const getBtn = document.querySelector(".get")
const verifyBtn = document.querySelector(".verify")
const overlay = document.querySelector(".overlay")
const loading = document.querySelector(".loader-cont")
const codeSent = document.querySelector(".code-sent")
const okButt = document.querySelector(".code-sent button")
const codeSentInfo = document.querySelector(".code-sent p")



okButt.addEventListener("click", ()=>{
    overlay.style.display = "none"
})

var buttonText = "Get Code"

getBtn.addEventListener("click", (event)=>{
    event.preventDefault()
    
    overlay.style.display = "flex"
    loading.style.display = "flex"
    codeSent.style.display = "none"
    fetch("send-verification-code")
    .then(res=>res.json())
    .then(data=>{
        if(data.code_sent){
            loading.style.display = "none"
            codeSent.style.display = "block"
            codeSentInfo.textContent = data.code_sent
            time = 60
            interval = setInterval(()=>{   
        
                if(time > 0){
                    if(time > 9){
                        buttonText = `00:${time}`
                    }else{
                        buttonText = `00:0${time}`
                    }
        
                    getBtn.textContent = buttonText
                    time--
                    getBtn.disabled = true
                    getBtn.classList.add("disabled")
                }else{
                    buttonText = "Resend Code"
                    getBtn.textContent = buttonText
                    getBtn.disabled = false
                    getBtn.classList.remove("disabled")
                    clearInterval(interval)
                }
                    
            }, 1000)
        }else if(data.email_is_none){
            window.href = "/authenticate/login"
        } else{
            loading.style.display = "none"
            codeSent.style.display = "block"
            codeSentInfo.textContent = "An error occured while sending the code"
        }
    })



})


input.addEventListener("input", ()=>{
    inputval = input.value
    input.value = inputval.replace(/[^0-9]/g, "")

    if(input.value.length == 4){
        verifyBtn.style.display = "inline-block"
        getBtn.style.display = "none"
    }else{
        verifyBtn.style.display = "none"
        getBtn.style.display = "inline-block"
    }
})