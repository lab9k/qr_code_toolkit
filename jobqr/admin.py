from django.contrib import admin
from jobqr.models import Job, TrackedItem


class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'items_str')


class TrackedItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')


admin.site.register(Job, JobAdmin)
admin.site.register(TrackedItem, TrackedItemAdmin)
