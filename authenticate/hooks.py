from custom_user.models import User
from django.shortcuts import redirect
from django.contrib import messages

def pre_login_user(user, request):
    messages.info(request, "nice one")
    user = request.user
    if not user.is_active:
        user.is_active = True
        user.save()
    
    