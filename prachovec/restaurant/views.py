from django.shortcuts import render
from .models import DrinkCategory, FoodCategory, Carousel


def restaurant(request):

    carousel_images = Carousel.objects.all()

    drinks_menu = DrinkCategory.objects.prefetch_related('items')
    food_menu = FoodCategory.objects.prefetch_related('items')

    context = {'carousel_images' : carousel_images, 
               'drinks_menu': drinks_menu, 
               'food_menu': food_menu}
    
    return render(request, 'restaurant/restaurant.html', context)
