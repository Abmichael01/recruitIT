from django.shortcuts import render
from profiles.models import *
from recruitment.models import *


def dashboard(request):
    companies = Company.objects.all()
    students = Student.objects.all()
    recruitments = Recruitment.objects.all()
    applications = Application.objects.all()

    return render(request, "ubit/dashboard.html", {
        "page": "dashboard",
        "companies": companies,
        "students": students,
        "recruitments": recruitments,
        "applications": applications,

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

def applications(request):
    applications = Application.objects.all()
    return render(request, "ubit/applications.html", {
        "page": "applications",
        "applications": applications,
    })

def recruitments(request):
    recruitments = Recruitment.objects.all()
    return render(request, "ubit/recruitments.html", {
        "page": "recruitments",
        "recruitments": recruitments,
    })
