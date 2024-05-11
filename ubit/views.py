from django.shortcuts import render
from profiles.models import *



def dashboard(request):
    companies = Company.objects.all()
    students = Student.objects.all()

    return render(request, "ubit/dashboard.html", {
        "page": "dashboard",
        "companies": companies,
        "students": students,

    })

def students(request):
    students = Student.objects.all()
    return render(request, "ubit/students.html", {
        "page": "students",
        "students": students,
    })

def companies(request):
    companies = Company.objects.all()
    return render(request, "ubit/companies.html", {
        "page": "companies",
        "companies": companies,
    })
