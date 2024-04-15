from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import json
from . models import Recruitment, Application, Saved_Recruitment, Notification
from django.contrib import messages
from django.utils import timezone
from functools import wraps
from django.urls import reverse

from django.core.mail import send_mail


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

def role_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_student == False and request.user.is_company == False:
                return redirect("select-role")
            return function(request, *args, **kwargs )
    return wrapper


@login_required
@role_required
def home(request):
    recruitments = Recruitment.objects.all()
    saved_recruitments = Saved_Recruitment.objects.filter(user=request.user)
    saved_recruitment_ids = set(saved_recruitment.recruitment_id for saved_recruitment in saved_recruitments)
    applications = Application.objects.filter(user=request.user)
    application_r_ids = set(application.recruitment_id for application in applications)

    
    application_objects = Application.objects.filter(id__in=application_r_ids)
    print(application_objects)

    application_dict = {application.recruitment.id: application for application in application_objects}

    current_time = timezone.now()


    # messages.info(request, "INformation testing")
    return render(request, "recruitment/home.html", {
        "page": "home",
        "recruitments": recruitments,
        "saved_recruitment_ids": saved_recruitment_ids,
        "application_r_ids": application_r_ids,
        "applications": applications,
        "application_dict": application_dict,
        "current_time": current_time,
}) 

@login_required
def recruitment(request, pk):
    recruitments = Recruitment.objects.filter(id=pk)
    saved_recruitments = Saved_Recruitment.objects.filter(user=request.user)
    saved_recruitment_ids = set(saved_recruitment.recruitment_id for saved_recruitment in saved_recruitments)
    current_time = timezone.now()
    return render(request, "recruitment/recruitment.html", {
        "page": "recruitment",
        "recruitments": recruitments,
        "saved_recruitment_ids": saved_recruitment_ids,
        "current_time": current_time,
    })

@login_required
def add_recruitment(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        image_file = request.FILES.get('image')
        seats = request.POST.get('seats')

        if title == "":
            return JsonResponse({
                "input_error": "Title field cannot be empty"
            })

        if description == "":
            return JsonResponse({
                "input_error": "Description field cannot be empty"
            })

        if image_file is None:
            return JsonResponse({
                "input_error": "Image field cannot be empty"
            })

        if seats == "":
            return JsonResponse({
                "input_error": "Seats field cannot be empty"
            })
        elif int(seats) < 1:
            return JsonResponse({
                "input_error": "Seats cannot be lesser than 1"
            })

        recruitment = Recruitment.objects.create(
            user = request.user,
            title = title,
            description = description,
            image = image_file,
            seats = seats,
        )
        recruitment.save()
        print("worked")
        messages.success(request, "Recruitment posted successfully")
        return JsonResponse({
            "success": "it workledd"
        })
        
        
@login_required
def apply(request):
    if request.method == "POST":
        user = request.user
        recruitment_id = request.POST.get('recruitment_id')
        name = request.POST.get("name")
        email = request.POST.get("email")
        matric_no = request.POST.get("matric-no")
        letter = request.FILES.get("letter")

        if letter is None:
            return JsonResponse({
                "input_error": "Please upload your IT letter to apply"
            })
        
        recruitment = Recruitment.objects.get(id=recruitment_id)

        application, created = Application.objects.get_or_create(
            user=user,
            recruitment=recruitment,
            defaults={
                'name': name,
                'email': email,
                'matric_no': matric_no,
                'letter': letter,
            }
        )

        if created:
            print("created")
            base_url = request.scheme + '://' + request.get_host()
            link = reverse("recruitment-applications", kwargs={'pk': recruitment.id})
            new_notification = Notification.objects.create(
                user = recruitment.user,
                title = "New Application",
                description = name + 'just applied for "'  + str(recruitment) + '"',
                link =  base_url+link,
            )

            new_notification.save()
        else:
            # Check if the letter is different
            if application.letter != letter:
                # Update the existing application's letter
                application.letter = letter
                application.save()
                print("letter updated")
                base_url = request.scheme + '://' + request.get_host()
                link = reverse("recruitment-applications", kwargs={'pk': recruitment.id})
                new_notification = Notification.objects.create(
                    user = recruitment.user,
                    title = "Re-Application",
                    description = name + ' just re-applied for "'  + str(recruitment) + '"',
                    link =  base_url+link,
                )

                new_notification.save()
            else:
                print("re-applied with the same letter")
            
        
        return JsonResponse({
            "success": True,
        })



def approve_application(request):
    if request.method == "POST":
        application_id = request.POST.get("application_id")
        company_email = request.POST.get("company_email")
        applicant_email = request.POST.get("applicant_email")
        approval_message = request.POST.get("message")

        if len(approval_message) < 100:
            return JsonResponse({
                "input_error": "Message cannot be lesser than 100 characters"
            })

        application = Application.objects.get(id=application_id)

        subject = "Your Application Has been approved"
        sender = company_email
        reciever = [applicant_email]
        message = f"""{application.name}\nYour Application to {str(application.recruitment.title)} has been approved\n{approval_message}"""
        
        try:
            send_mail(
                subject,
                message,
                sender,
                reciever,
                fail_silently=False,
            )
            print("sent")
            messages.success(request, "Application, applicant will recieve your email and contact you")
            application.approved = True
            application.save()

            new_notification = Notification.objects.create(
                user = application.user,
                title = "Application Approved",
                description = 'Your application to "'  + str(application.recruitment) + '" has been approved. Check your email to continue',
            )

            new_notification.save()
        except Exception as e:
            return JsonResponse({
                "input_error": f"An error occured: {str(e)}"
            })
        else:

            return JsonResponse({
                "success": "Application, applicant will recieve your email and contact you"
            })




                


@login_required
def cancel_application(request):
    if request.method == "POST":
        application_id = request.POST.get("application_id")
        application = Application.objects.get(id=application_id) 

        new_notification = Notification.objects.create(
            user = application.recruitment.user,
            title = "Canceled Application",
            description = str(application.name) + 'Canceled application for "'  + str(application.recruitment) + '"', 
        )

        new_notification.save()
        
        application.delete()
        messages.success(request, "Application was canceled successfully")
        return JsonResponse({
            "canceled": True
        })


@login_required
def save_recruitment(request):
    if request.method == "POST":
        user = request.user
        recruitment_id = request.POST.get("recruitment_id")

        recruitment = Recruitment.objects.get(id=recruitment_id)

        saved_recruitment, created = Saved_Recruitment.objects.get_or_create(
                user = user,
                recruitment = recruitment
            )
        
        if not created:
            saved_recruitment.delete()
            return JsonResponse({
                "status": "Save"
            })
        else:
            saved_recruitment.save()
            return JsonResponse({
                "status": "Saved"
            })


@login_required
def company_recruitments(request):
    recruitments = Recruitment.objects.filter(user=request.user)
    return render(request, "recruitment/company-recruitments.html", {
        "page": "company_recruitments",
        "recruitments": recruitments,

    })  

@login_required
def recruitment_application(request, pk):
    recruitment = Recruitment.objects.get(id=pk)
    r_applications = Application.objects.filter(recruitment=recruitment)
    return render(request, "recruitment/recruitment-applications.html", {
        "page": "recruitment_application",
        "r_applications": r_applications,
    }) 

@login_required
def student_applications(request):
    s_applications = Application.objects.filter(user=request.user)
    return render(request, "recruitment/student-applications.html", {
        "page": "student_applications",
        "s_applications": s_applications,
    })

@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user)

    for notification in notifications:
        notification.seen = True
        notification.save()

    return render(request, "recruitment/notifications.html", {
        "page": "notifications",
        "notifications": notifications,
    })

def get_unseen_notifications(request):
    notifications = Notification.objects.filter(user=request.user)

    unseen_count = 0

    for notification in notifications:
        if notification.seen == False:
            unseen_count += 1
    
    return JsonResponse({
        "unseen_count": unseen_count,
    })

def get_application_info(request):
    if request.method == "POST":
        application_id = request.POST.get("application_id")
        application = Application.objects.get(id=application_id)

        return JsonResponse({
            "applicant_email": str(application.user.email),
        })
