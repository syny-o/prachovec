from django.contrib import admin
from .models import News, Contact




# customizing the admin interface
# 1. titles
admin.site.site_header = "Prachovec - Administrace"
admin.site.index_title = "Prachovec - Administrace"
admin.site.site_title = "Prachovec"

# 2. customizing the list of items

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['date', 'title',]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'date_created', 'date_arrival', 'date_departure', 'persons', 'phone', 'email', 'note']
    list_filter = ['date_created', 'date_arrival', 'date_departure']
    search_fields = ['full_name', 'phone', 'email', 'note']
    # date_hierarchy = 'date_created'
    ordering = ['date_created']


