from django.contrib import admin

from url_minion.models import ShortUrl


@admin.register(ShortUrl)
class ShortUrlAdmin(admin.ModelAdmin):
    readonly_fields = ('url', 'index')
    list_display = ('url', 'index')
