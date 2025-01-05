from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'date_created', 'date_arrival', 'date_departure', 'persons', 'phone', 'email', 'note']
    list_filter = ['date_created', 'date_arrival', 'date_departure']
    search_fields = ['full_name', 'phone', 'email', 'note']
    # date_hierarchy = 'date_created'
    ordering = ['date_created']
