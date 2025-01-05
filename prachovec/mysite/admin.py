from django.contrib import admin
from .models import News, HomeCarousel


admin.site.register(HomeCarousel)




# customizing the admin interface
# 1. titles
admin.site.site_header = "Prachovec - Administrace"
admin.site.index_title = "Prachovec - Administrace"
admin.site.site_title = "Prachovec"

# 2. customizing the list of items

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['date', 'title',]





