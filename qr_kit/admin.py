from django.contrib import admin
from qr_kit.models import Category, InputValue, QrCode


class InputValueInline(admin.StackedInline):
    model = InputValue
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [InputValueInline]
    list_display = ('name',)


@admin.register(QrCode)
class QrCodeAdmin(admin.ModelAdmin):
    fields = ('category', 'uuid', 'values')
    readonly_fields = ('uuid', 'values')
