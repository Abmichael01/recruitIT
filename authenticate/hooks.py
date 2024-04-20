def pre_login_user(user, request):
    if user.is_active == False:
        user.is_active = True
        user.save()
    
    