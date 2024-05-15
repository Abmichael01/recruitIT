from django.urls import path
from . views import *

app_name = "ubit"

urlpatterns = [
    path("dashboard", dashboard, name="dashboard"),
    path("students", students, name="students"),
    path("companies", companies, name="companies"),
    path("recruitments", recruitments, name="recruitments"),
    path("applications", applications, name="applications"),
    
]
