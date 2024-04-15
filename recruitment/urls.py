from django.urls import path
from . views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", home, name="home"),
    path("company/recruitments", company_recruitments, name="company-recruitments"),
    path("notifications", notifications, name="notifications" ),
    path("company/recruitments/<str:pk>/applications", recruitment_application, name="recruitment-applications"),
    path("student/applications", student_applications, name="student-applications"),
    path("recruitments/<str:pk>", recruitment, name="recruitment"),




    path("add-recruitment", csrf_exempt(add_recruitment), name="add-recruitment"),
    path("apply", csrf_exempt(apply), name="apply"),
    path("save-recruitment", csrf_exempt(save_recruitment), name="save-recruitment"),
    path("cancel-application", csrf_exempt(cancel_application), name="cancel-application"),
    path("get-unseen-notifications", csrf_exempt(get_unseen_notifications), name="get-unseen-notifications"),
    path("get-application-info", csrf_exempt(get_application_info), name="get-application-info"),
    path("approve-application", csrf_exempt(approve_application), name="approve-application")
    
]
 