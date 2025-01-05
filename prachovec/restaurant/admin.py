from django.contrib import admin
from .models import DrinkItem, DrinkCategory, FoodItem, FoodCategory

admin.site.register(DrinkItem)
admin.site.register(DrinkCategory)
admin.site.register(FoodItem)
admin.site.register(FoodCategory)

