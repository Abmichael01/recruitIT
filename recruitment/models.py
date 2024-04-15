from django.db import models
from custom_user.models import User


class Recruitment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/")
    seats = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
    

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    matric_no = models.CharField(max_length=20)
    letter = models.FileField(upload_to="documents/")
    created = models.DateTimeField(auto_now_add=True, null=True)
    approved = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ["-created"]
    def __str__(self):
        return str(self.name) +" APPLIED FOR "+ str(self.recruitment)
    
class Saved_Recruitment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.student.first_name) +" SAVED "+ str(self.recruitment)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, null=True)
    seen = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return str(self.title) + " - " + str(self.user)

    