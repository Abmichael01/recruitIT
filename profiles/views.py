from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Student, Company
from django.contrib.auth.decorators import login_required
from custom_user.models import User
from recruitment.models import Recruitment, Application, Saved_Recruitment
from django.utils import timezone


@login_required(login_url="login")
def profile_setup(request):
    user = request.user
    if request.method == "POST":
        if user.is_student == True:
            first_name = request.POST["first_name"]
            avatar = request.FILES["image"]
            last_name = request.POST["last_name"]
            matric_no = request.POST["matric_no"]

            user_profile =  Student.objects.get(user=user)
            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.matric_no = matric_no
            
            if avatar is not None:
                user_profile.avatar = avatar
            else:
                user_profile.avatar = user_profile.avatar
            
            user_profile.save()

        if user.is_company == True:
            company_name = request.POST["company_name"]
            bio = request.POST["bio"]
            phone_number = request.POST["phone_number"]
            avatar = request.FILES.get("image")
            address = request.POST["address"]
            city = request.POST["city"]
            state = request.POST["state"]

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
            avatar = request.FILES["image"]
            last_name = request.POST["last_name"]
            matric_no = request.POST["matric_no"]

            user_profile =  Student.objects.get(user=user)
            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.matric_no = matric_no
            
            if avatar is not None:
                user_profile.avatar = avatar
            else:
                user_profile.avatar = user_profile.avatar
            
            user_profile.save()

        if user.is_company == True:
            company_name = request.POST["company_name"]
            bio = request.POST["bio"]
            phone_number = request.POST["phone_number"]
            avatar = request.FILES.get("image")
            address = request.POST["address"]
            city = request.POST["city"]
            state = request.POST["state"]

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
