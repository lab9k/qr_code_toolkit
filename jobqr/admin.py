from django.contrib import admin
from jobqr.models import Job, TrackedItem

# Register your models here.
admin.site.register(Job)
admin.site.register(TrackedItem)
