from django.contrib import admin
from .models import Department, Schedule
from django.contrib.auth.models import Group, User


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
admin.site.unregister(User)