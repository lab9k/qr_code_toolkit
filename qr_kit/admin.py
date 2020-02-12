from django.contrib import admin
from reversion.admin import VersionAdmin

from qr_kit.models import JobImage, Job, TrackedItem


class ImageInline(admin.StackedInline):
    model = JobImage
    extra = 1


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'current_items')
    inlines = [ImageInline]


@admin.register(TrackedItem)
class TrackedItemAdmin(VersionAdmin):
    list_display = ('name', 'job')


admin.site.site_header = "QR-toolkit admin"
admin.site.site_title = "Qr-toolkit admin portal"
admin.site.index_title = "Welcome to the Qr-toolkit admin page"
