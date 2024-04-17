from django.db import models
from custom_user.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50,  null=True, blank=True)
    matric_no = models.CharField(max_length=11, null=True, blank=True)
    avatar = models.ImageField(null=True, default="images/avatar.png", upload_to="images/", blank=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    avatar = models.ImageField(null=True, default="images/avatar.png", upload_to="images/", blank=True)

    address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)


    class Meta:
        verbose_name = "Company"
        

    def __str__(self):
        return str(self.company_name)
