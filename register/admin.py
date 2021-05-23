from register.models import Profile
from django.contrib.admin.options import TabularInline
from django.db import models
from orders.models import User
from django.contrib import admin
from register.models import Profile
# Register your models here.

class ProfileInline(admin.TabularInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    inlines =[ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)