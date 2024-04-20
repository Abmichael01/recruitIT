from custom_user.models import User
from django.shortcuts import redirect

def pre_login_user(user, request):
    user = request.user
    if not user.is_active:
        user.is_active = True
        user.save()
    
    