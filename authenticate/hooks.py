from custom_user.models import User
from django.shortcuts import redirect

def pre_login_user(user, request):
    if not user.is_active:
        # Redirect the user to a specific URL
        user.is_active = True
        user.save()
        return redirect('profile', pk=user.id)
    # If no additional processing is needed, return None
    return None
    