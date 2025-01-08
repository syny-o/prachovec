from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Photo
from .data import places

def activities(request):
    # Photo Gallery
    photos = Photo.objects.all()

    
    paginator = Paginator(photos, 6)  # Paginate photos (6 photos per page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page = request.GET.get('page')
    photos_only = request.GET.get('photos_only')
    try:
        one_page_photos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        one_page_photos = paginator.page(1)
    except EmptyPage:
        if photos_only:
            # If AJAX request and page out of range
            # return an empty page
            return HttpResponse('')
        # If page out of range return last page of results
        one_page_photos = paginator.page(paginator.num_pages)

    if photos_only:  # AJAX request for another page of photos
        return render(
            request,
            'activities/photos.html',
            {'photos': one_page_photos,}
        )

    # Pass the paginated photos to the template
    context = {
        'places': places,
        'photos': page_obj,  # This now contains only the photos for the current page
        'total_pages': paginator.num_pages,
    }
    return render(request, 'activities/activities.html', context)
