from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class user_view(UserAdmin):
    list_display = ['email','username']

