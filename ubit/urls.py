from django.urls import path
from . views import *
from django.views.decorators.csrf import csrf_exempt

app_name = "ubit"

urlpatterns = [
    path("dashboard", dashboard, name="dashboard"),
    path("students", students, name="students"),
    path("companies", companies, name="companies"),
    path("recruitments", recruitments, name="recruitments"),
    path("applications", applications, name="applications"),
    

    path("delete-student", csrf_exempt(delete_student), name="delete-student"),
    path("delete-company", csrf_exempt(delete_company), name="delete-company"),
    
]
