from django.contrib import admin
from . models import Recruitment, Application, Saved_Recruitment, Notification, AcceptanceForm


admin.site.register([Recruitment, Application, Saved_Recruitment, Notification, AcceptanceForm])
