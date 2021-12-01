from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Team, Task
from .forms import *

admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'role')
    list_filter = ('role', 'team')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    form = TeamForm
    list_display = ('id', 'name')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'worker', 'status')
    list_filter = ('status',)


