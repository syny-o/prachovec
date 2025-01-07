from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Photo
from .data import places

def activities(request):
    # Fetch all photos
    photos = Photo.objects.all()

    # Paginate the photos (e.g., 6 photos per page)
    paginator = Paginator(photos, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the paginated photos to the template
    context = {
        'places': places,
        'photos': page_obj,  # This now contains only the photos for the current page
    }
    return render(request, 'activities/activities.html', context)
