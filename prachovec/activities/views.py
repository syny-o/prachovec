from django.shortcuts import render
from .data import places


def activities(request):
    context = {
        'places': places,
    }
    return render(request, 'activities/activities.html', context)
