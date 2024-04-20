def pre_login_user(user, request):
    print("is it working at all")
    if user.is_active == False:
        user.is_active = True
        user.save()
    
    