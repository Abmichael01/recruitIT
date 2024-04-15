from django.urls import path
from . views import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LoginView



urlpatterns = [
    path("login", login_user, name="login"),
    path("logout", logout_user, name="logout"),
    path("register", register_user, name="register"),
    path("verify-email", verify_email, name="verify-email"),
    path("forgot-password", forgot_password ,name="forgot-password"),
    path("select-role", google_auth_role_selection, name="select-role"),
    

    path("validate-email", csrf_exempt(validateEmail), name="validate-email"),
    path("send-verification-code", csrf_exempt(send_verification_code), name="send-verification-code"),

]
