from django.contrib import admin
from .models import Contact, Service, Note, Photo, Introduction, Carousel

admin.site.register(Carousel)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'date_created', 'date_arrival', 'date_departure', 'persons', 'phone', 'email', 'note']
    list_filter = ['date_created', 'date_arrival', 'date_departure']
    search_fields = ['full_name', 'phone', 'email', 'note']
    # date_hierarchy = 'date_created'
    ordering = ['date_created']



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_main_season', 'price_off_season', 'position']
    ordering = ['position']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['name',]
    ordering = ['position']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title',]

@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']


