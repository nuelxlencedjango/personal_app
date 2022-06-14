from django.contrib import admin
from numpy import product

# Register your models here.

from .models import *




# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','selected_properties', 'message']