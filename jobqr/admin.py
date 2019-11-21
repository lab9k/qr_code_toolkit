from django.contrib import admin
from jobqr.models import Job, TrackedItem
from reversion.admin import VersionAdmin


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'items_str')


@admin.register(TrackedItem)
class TrackedItemAdmin(VersionAdmin):
    list_display = ('name', 'job')


admin.site.site_header = "QR-toolkit admin"
admin.site.site_title = "Qr-toolkit admin portal"
admin.site.index_title = "Welcome to the Qr-toolkit admin page"
