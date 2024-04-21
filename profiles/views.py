from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Student, Company
from django.contrib.auth.decorators import login_required
from custom_user.models import User
from recruitment.models import Recruitment, Application, Saved_Recruitment
from django.utils import timezone
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


@login_required
def profile_setup(request):
    user = request.user
    if request.method == "POST":
        if user.is_student == True:
            first_name = request.POST["first_name"]
            avatar = request.FILES.get("image")
            last_name = request.POST["last_name"]
            matric_no = request.POST["matric_no"]
            phone_number = request.POST["phone_number"]

            if first_name == "":
                messages.error(request, "Please enter your first name")
                return redirect("profile-setup")
            if last_name == "":
                messages.error(request, "Please enter your last name")
                return redirect("profile-setup")
            if phone_number == "":
                messages.error(request, "Please enter your phone number")
                return redirect("profile-setup")
            elif len(phone_number) < 11:
                messages.error(request, "Please enter a valid phone number")
                return redirect("profile-setup")
            if matric_no == "":
                messages.error(request, "Please enter your matric number")
                return redirect("profile-setup")
            elif len(matric_no) < 10:
                messages.error(request, "Please enter a valid matric number")
                return redirect("profile-setup")

            user_profile =  Student.objects.get(user=user)
            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.matric_no = matric_no
            user_profile.phone_number = phone_number
            
            if avatar is not None:
                user_profile.avatar = avatar
            else:
                user_profile.avatar = user_profile.avatar
            
            user_profile.save()
            user.profile_completed = True
            user.save()

        if user.is_company == True:
            company_name = request.POST["company_name"]
            bio = request.POST["bio"]
            phone_number = request.POST["phone_number"]
            avatar = request.FILES.get("image")
            address = request.POST["address"]
            city = request.POST["city"]
            state = request.POST["state"]

            if company_name == "":
                messages.error(request, "Please enter your company name")
                return redirect("profile-setup")
            if bio == "":
                messages.error(request, "Please enter your bio")
                return redirect("profile-setup")
            if phone_number == "":
                messages.error(request, "Please enter your phone number")
                return redirect("profile-setup")
            if address == "":
                messages.error(request, "Please enter your address")
                return redirect("profile-setup")
            if city == "":
                messages.error(request, "Please enter your city")
                return redirect("profile-setup")
            if state == "State":
                messages.error(request, "Please select your state")
                return redirect("profile-setup")
            

            user_profile =  Company.objects.get(user=user)
            user_profile.company_name = company_name
            user_profile.bio = bio
            user_profile.phone_number = phone_number
            user_profile.address = address
            user_profile.city = city
            user_profile.state = state

            if avatar is not None:
                user_profile.avatar = avatar
            else:
                user_profile.avatar = user_profile.avatar
            user_profile.save()
            user.profile_completed = True
            user.save()

        messages.success(request, "Profile setup was successful")
        return redirect("home")

            
    is_company = ""
    is_student = ""
    if user.is_student == True:
        is_student = "True"
    else:
        is_company = "True"

    return render(request, "profiles/profile-setup.html", {
        "page": "profile-setup",
        "is_student": is_student,
        "is_company": is_company,
    })


@login_required
def profile(request, pk):
    user = User.objects.get(id=pk)
    recruitments = Recruitment.objects.filter(user=user)
    saved_recruitments = Saved_Recruitment.objects.filter(user=request.user)
    saved_recruitment_ids = set(saved_recruitment.recruitment_id for saved_recruitment in saved_recruitments)
    applications = Application.objects.filter(user=request.user)
    application_r_ids = set(application.recruitment_id for application in applications)
    current_time = timezone.now()
    return render(request, "profiles/profile.html", {
        "page": "profile",
        "recruitments": recruitments,
        "saved_recruitment_ids": saved_recruitment_ids,
        "application_r_ids": application_r_ids,
        "current_time": current_time,
        "user": user,       
    })



@login_required
def edit_profile(request):
    user = request.user

    profile = ""
    if user.is_student == True:
        profile = Student.objects.get(user=user)
    if user.is_company == True:
        profile = Company.objects.get(user=user)

    if request.method == "POST":
        if user.is_student == True:
            first_name = request.POST["first_name"]
            avatar = request.FILES.get("image")
            last_name = request.POST["last_name"]
            matric_no = request.POST["matric_no"]
            phone_number = request.POST["phone_number"]

            if first_name == "":
                messages.error(request, "Please enter your first name")
                return redirect("profile-setup")
            if last_name == "":
                messages.error(request, "Please enter your last name")
                return redirect("profile-setup")
            if phone_number == "":
                messages.error(request, "Please enter your phone number")
                return redirect("profile-setup")
            elif len(phone_number) < 11:
                messages.error(request, "Please enter a valid phone number")
                return redirect("profile-setup")
            if matric_no == "":
                messages.error(request, "Please enter your matric number")
                return redirect("profile-setup")
            elif len(matric_no) < 10:
                messages.error(request, "Please enter a valid matric number")
                return redirect("profile-setup")

            user_profile =  Student.objects.get(user=user)
            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.matric_no = matric_no
            user_profile.phone_number = phone_number
            
            if avatar is not None:
                user_profile.avatar = avatar
            else:
                user_profile.avatar = user_profile.avatar
            
            user_profile.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile", pk=user.id)

        if user.is_company == True:
            company_name = request.POST["company_name"]
            bio = request.POST["bio"]
            phone_number = request.POST["phone_number"]
            avatar = request.FILES.get("image")
            address = request.POST["address"]
            city = request.POST["city"]
            state = request.POST["state"]

            if company_name == "":
                messages.error(request, "Please enter your company name")
                return redirect("profile-setup")
            if bio == "":
                messages.error(request, "Please enter your bio")
                return redirect("profile-setup")
            if phone_number == "":
                messages.error(request, "Please enter your phone number")
                return redirect("profile-setup")
            if address == "":
                messages.error(request, "Please enter your address")
                return redirect("profile-setup")
            if city == "":
                messages.error(request, "Please enter your city")
                return redirect("profile-setup")
            if state == "State":
                messages.error(request, "Please select your state")
                return redirect("profile-setup")

            user_profile =  Company.objects.get(user=user)
            user_profile.company_name = company_name
            user_profile.bio = bio
            user_profile.phone_number = phone_number
            user_profile.address = address
            user_profile.city = city
            user_profile.state = state

            if avatar is not None:
                user_profile.avatar = avatar
            else:
                user_profile.avatar = user_profile.avatar
            user_profile.save()

            messages.success(request, "Profile updated successfully")
            return redirect("profile", pk=user.id)

            
    is_company = ""
    is_student = ""
    if user.is_student == True:
        is_student = "True"
    else:
        is_company = "True"

    return render(request, "profiles/profile-setup.html", {
        "page": "edit-profile",
        "is_student": is_student,
        "is_company": is_company,
        "profile": profile
    })
