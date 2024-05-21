from django.shortcuts import render, redirect
from recruitment.models import AcceptanceForm
from django.contrib import messages
from django.urls import reverse
from functools import wraps
# Create your views here.

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
    letters = AcceptanceForm.objects.all()
    return render(request, 'it_coord/dashboard.html', {
        "letters": letters,
    })
