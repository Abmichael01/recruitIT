from django.shortcuts import render, redirect
from django.urls import reverse
from profiles.models import *
from recruitment.models import *
from functools import wraps
from django.contrib import messages


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

def super_admin_only(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.info(request, "You are not allowed to access the page")
            return redirect("home")
        return function(request, *args, **kwargs)
    return wrapper

@login_required
@super_admin_only
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

@login_required
@super_admin_only
def students(request):
    students = Student.objects.all()
    return render(request, "ubit/students.html", {
        "page": "students",
        "students": students,
    })

@login_required
@super_admin_only
def companies(request):
    companies = Company.objects.all()
    return render(request, "ubit/companies.html", {
        "page": "companies",
        "companies": companies,
    })

@login_required
@super_admin_only
def applications(request):
    applications = Application.objects.all()
    return render(request, "ubit/applications.html", {
        "page": "applications",
        "applications": applications,
    })

@login_required
@super_admin_only
def recruitments(request):
    recruitments = Recruitment.objects.all()
    return render(request, "ubit/recruitments.html", {
        "page": "recruitments",
        "recruitments": recruitments,
    })
