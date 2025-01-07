from django.shortcuts import render
from .models import Photo
from .data import places


def activities(request):
    # photo Gallery
    photos = Photo.objects.all()

    context = {
        'places': places,
        'photos': photos,
    }
    return render(request, 'activities/activities.html', context)
