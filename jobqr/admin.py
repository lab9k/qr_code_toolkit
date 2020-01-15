from django.contrib import admin

from jobqr.models import Job, TrackedItem, MethodTemplate, Method, JobImage
from reversion.admin import VersionAdmin


class ImageInline(admin.StackedInline):
    model = JobImage
    extra = 1


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'items_str')
    inlines = [ImageInline]


@admin.register(TrackedItem)
class TrackedItemAdmin(VersionAdmin):
    list_display = ('name', 'job')


@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    pass


@admin.register(MethodTemplate)
class MethodTemplateAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = "QR-toolkit admin"
admin.site.site_title = "Qr-toolkit admin portal"
admin.site.index_title = "Welcome to the Qr-toolkit admin page"
