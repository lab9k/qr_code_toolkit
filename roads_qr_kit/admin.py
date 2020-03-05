from django.contrib import admin
from reversion.admin import VersionAdmin

from roads_qr_kit.models import JobImage, Job, TrackedItem


class ImageInline(admin.StackedInline):
    model = JobImage
    extra = 0


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'current_items')
    inlines = [ImageInline]

    def current_items(self, obj):
        if obj.current_items and len(obj.current_items.all()) > 0:
            items = [str(x) for x in obj.current_items.all()]
            return ', '.join(items)
        else:
            return 'Not available'

    current_items.short_description = 'Currently Tracked Items'


@admin.register(TrackedItem)
class TrackedItemAdmin(VersionAdmin):
    list_display = ('name', 'job')


admin.site.site_header = "QR-toolkit admin"
admin.site.site_title = "Qr-toolkit admin portal"
admin.site.index_title = "Welcome to the Qr-toolkit admin page"
