# from django.contrib import admin
# from django_use_email_as_username.admin import BaseUserAdmin

# from .models import User

# admin.site.register(User, BaseUserAdmin)


from django.contrib import admin
from django_use_email_as_username.admin import BaseUserAdmin
from .models import User

class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'is_student', 'is_company', 'is_active', 'date_joined', 'last_login')
    list_filter = ('is_student', 'is_company', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'verification_code')}),
        ('Permissions', {'fields': ('is_student', 'is_company', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_student', 'is_company', 'is_active'),
        }),
    )


    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)