# Django
from django.contrib import admin

# Project
from .models import User, Position, HardwareAddress, AssignedDevice, WorkType, OfficeHours


class MacInline(admin.StackedInline):
    model = HardwareAddress
    extra = 3


class WorkTypeInline(admin.StackedInline):
    model = WorkType

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'telegram')
    inlines = [WorkTypeInline, MacInline]

admin.site.register(Position)

admin.site.register(AssignedDevice)

admin.site.register(OfficeHours)