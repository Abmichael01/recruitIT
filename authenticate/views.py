from django.shortcuts import render, redirect
import json
from validate_email import validate_email
from django.http import JsonResponse
from django.contrib import messages
from custom_user.models import User
from profiles.models import Student, Company
import random
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from functools import wraps
from django.urls import reverse





def login_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            next_url = request.get_full_path()
            login_url = '{}?next={}'.format(reverse('login'), next_url)
            messages.info(request, "Please log in to access this page.")
            return redirect(login_url)
        return function(request, *args, **kwargs)
    return wrapper



def validateEmail(request):
    data = json.loads(request.body)
    email = data["email"]

    if not validate_email(email):
        return JsonResponse({
            "email_error": "email is invalid"
        })
    
    if User.objects.filter(email=email).exists():
        return JsonResponse({
            "email_error": "email is taken, choose another email"
        })

    return JsonResponse({
            "email_valid": True
        })




def login_user(request):
    next_url = request.GET.get('next', None)
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        
        user_from_backend = ""
        if not User.objects.filter(email=email).exists():
            messages.error(request, "Email or password is incorrect")
            return redirect("login")
        
        user_from_backend = User.objects.get(email=email)
        
        if not user_from_backend.is_active:
            request.session["verification_email"] = email
            messages.info(request, "Please verify your email to login")
            return redirect("verify-email")
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            messages.success(request, "Login was successful")
            login(request, user)
            if next_url is not None:
                return redirect(next_url)
            else:
                return redirect("home")
            
        else:
            messages.error(request, "Email or password is incorrect")

    

    return render(request, "authenticate/login.html", {
        "page": "login",
        "next_url": next_url
    })


def logout_user(request):
    logout(request)
    return redirect("login")


def register_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]


        if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(email=email, password=password)
            user.is_active = True
            
            if role == "student":
                user.is_student = True
                user.save()
                user_profile = Student.objects.create(user=user)
                user_profile.save()
            else:
                user.is_company = True
                user.save()
                user_profile = Company.objects.create(user=user)
                user_profile.save()
            
            messages.success(request, "Your account was successfuly created")

            request.session["verification_email"] = email
            return redirect('verify-email')
        
    
    return render(request, "authenticate/register.html", {
        "page": "register"
    })

    

def send_verification_code(request):
    email = request.session.get("verification_email", None)
    
    if email is None:
        messages.info(request, "Please login to continue")
        return JsonResponse(
            {
                "email_is_none": True
            }
        )
        
    user = User.objects.get(email=email)

    num1 = str(random.randint(0, 9))
    num2 = str(random.randint(0, 9))
    num3 = str(random.randint(0, 9))
    num4 = str(random.randint(0, 9))

    code = num1+num2+num3+num4
    
    user.verification_code = code
    user.save()

    subject = "Verify Your Email Address"
    sender = "abmichael109@gmail.com"
    reciever = [user.email, ]
    html_message = render_to_string("authenticate/verification-email.html", {"code": code, "email": email})
    plain_message = strip_tags(html_message)

    
    try:
        message = EmailMultiAlternatives(
        subject = subject,
        body= plain_message,
        from_email= sender,
        to= reciever, 
        )

        message.attach_alternative(html_message, "text/html")
        message.send()
    except Exception as e:
        print(str(e))
        return JsonResponse({
            "code_error": f"An error occured: {str(e)}"
        })
        print("error dey ooo")
    else:
        user.verification_code = code
        user.save()
        print(code)

        return JsonResponse({
            "code_sent": "Code sent, check your email"
        })
    


def verify_email(request):
    print(request.user)
    email = request.session.get("verification_email", None)
        
    user = User.objects.get(email=email)

    print(email)
    if request.method == "POST":
        code = request.POST["code"]

        if user.verification_code == code:
            user.is_active = True
            user.save()

            login(request, user)
            messages.success(request, "Email verification was successful")
            return redirect("profile-setup")
        else:
            if user.verification_code == "":
                messages.error(request, "Get code and check your email to copy code")
            else:
                messages.error(request, "Verification code does not match, check your email and enter code again")
            
            

    return render(request, "authenticate/verify-email.html", {
        "page": "verify-email"
    })


def forgot_password(request):
    if request.method == "POST":
        email = request.POST["email"]
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            subject = "Forgot Password"
            sender = "recruit.it000@gmail.com"
            reciever = [email]
            message = f"""Hello {email} \n Your password is: {str(user.password)} """
            
            try:
                send_mail(
                    subject,
                    message,
                    sender,
                    reciever,
                    fail_silently=False,
                )
                print("sent")
                messages.success(request, "Your password has been sent to your email")
            except Exception as e:
                messages.error(request, f"An error occured: {str(e)}")
            else:
                messages.success(request, "Your password has been sent to ypur email")
                return redirect("login")
        else:
            messages.error(request, "Email does not exist")

    return render(request, "authenticate/forgot-password.html", {
        "page": "forgot-password"
    })


def google_auth_role_selection(request):
    user = request.user
    if request.method == "POST":
        role = request.POST["role"]

        if role == "student":
            user.is_student = True
            student = Student.objects.create(user=user)
            student.save()
        else:
            user.is_company = True
            company = Company.objects.create(user=user)
            company.save()

        user.save()

        return redirect("profile-setup")

    return render(request, "authenticate/select-role.html", {
        "page": "select-role"
    })


