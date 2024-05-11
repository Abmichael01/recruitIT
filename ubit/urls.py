from django.urls import path
from . views import *


urlpatterns = [
    path("dashboard", dashboard, name="dashboard"),
    path("students", students, name="students"),
    path("companies", companies, name="companies")
]
