from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ContactForm
from .tasks import task_send_email
from .models import Service, Note, Photo, Introduction, Carousel



def accommodation(request):
    # Carousel
    carousel_images = Carousel.objects.all()

    # Intro
    introduction = Introduction.objects.last()

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


    # Price list / services + notes
    services = Service.objects.all()
    notes = Note.objects.all()

    # Contact
    base_url = reverse('accommodation:accommodation')
    contact_section = f"{base_url}#contact-form"

    if request.method == 'GET':
        if photos_only:  # AJAX request for another page of photos
            return render(
                request,
                'accommodation/photos.html',
                {'photos': one_page_photos,}
        )

        form = ContactForm()
        context = {
            'form': form,
            'photos': page_obj,  # Pass paginated photos
            'total_pages': paginator.num_pages,
            'services': services,
            'notes': notes,
            'introduction': introduction,
            'carousel_images': carousel_images,
            'contact_section': contact_section,  # Added for completeness
        }
        return render(request, 'accommodation/accommodation.html', context)
    
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()                

            # CELEERY
            task_send_email.delay(form.cleaned_data['email'], form.cleaned_data['full_name'], form.cleaned_data['phone'], form.cleaned_data['email'], form.cleaned_data['note'], form.cleaned_data['date_arrival'], form.cleaned_data['date_departure'])

            messages.success(request, 'Děkujeme za zprávu. Ozveme se Vám co nejdříve.')
            
            return redirect(contact_section)
        

        else:
            # issues = form.errors
            messages.error(request, 'Něco je špatně. Zkontrolujte prosím email, popřípadě další pole.')
            context = {
                'form': form,  # Re-render the form with the existing data and errors
                'contact_section': contact_section,  # Include the fragment identifier in the context
                }
            return render(request, 'accommodation/accommodation.html', context)
