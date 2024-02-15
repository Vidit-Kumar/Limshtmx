from django.contrib import admin
from .models import Library
# Register your models here.


class LibraryAdmin(admin.ModelAdmin):
    list_display = ('titlle','author','publisher','category','page_count','shelf_location','publish_date','is_in_stock','checked_out',)

admin.site.register(Library,LibraryAdmin)