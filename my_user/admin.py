from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from my_user.models import My_User

# Register your models here.
admin.site.register(My_User, UserAdmin)
