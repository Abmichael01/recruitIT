from django.urls import path
from . views import *


urlpatterns = [
    path("profile-setup", profile_setup ,name="profile-setup"),
    path("profile/<str:pk>", profile, name="profile"),
    path("edit-profile", edit_profile, name="edit-profile"),
]
