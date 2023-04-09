from django.contrib import admin
from notify.models import *


admin.site.register(Timeoff)
admin.site.register(Warn)

@admin.register(Lateness)
class LatenessAdmin(admin.ModelAdmin):
    list_display = ('user', 'hour', 'minutes', 'created_datetime')
    exclude = ('total',)
    
@admin.register(Remote)
class RemoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'reason')

