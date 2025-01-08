from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import ContactForm
from .tasks import task_send_email
from .models import Service, Note, Photo, Introduction, Carousel



from django.shortcuts import render
from django.http import HttpResponse

def accommodation(request):
    # Carousel
    carousel_images = Carousel.objects.all()

    # Intro
    introduction = Introduction.objects.last()

    # Photo Gallery
    photos = Photo.objects.all()

    # Paginate photos (e.g., 6 photos per page)
    paginator = Paginator(photos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Price list / services + notes
    services = Service.objects.all()
    notes = Note.objects.all()

    # Contact
    base_url = reverse('accommodation:accommodation')
    contact_section = f"{base_url}#contact-form"

    if request.headers.get('HX-Request'):  # Check if the request is from HTMX
        return render(request, 'accommodation/partials/photo_gallery.html', {'photos': page_obj})

    if request.method == 'GET':
        form = ContactForm()
        context = {
            'form': form,
            'photos': page_obj,  # Pass paginated photos
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
