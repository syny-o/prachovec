from django.shortcuts import render
from .data import drinks_menu, food_menu


def restaurant(request):
    context = {'drinks_menu': drinks_menu, 'food_menu': food_menu}
    return render(request, 'restaurant/obcerstveni.html', context)
