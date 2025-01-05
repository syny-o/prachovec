from django.shortcuts import render
from .data import drinks_menu, food_menu
from .models import DrinkCategory, FoodCategory


def restaurant(request):
    drinks_menu = DrinkCategory.objects.prefetch_related('items')
    food_menu = FoodCategory.objects.prefetch_related('items')

    context = {'drinks_menu': drinks_menu, 'food_menu': food_menu}
    return render(request, 'restaurant/obcerstveni.html', context)
