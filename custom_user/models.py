from django_use_email_as_username.models import BaseUser, BaseUserManager
from django.db import models



class User(BaseUser):
    objects = BaseUserManager()
    
    # fields added
    profile_completed = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=4, null=True, blank=True)
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

    