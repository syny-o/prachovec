from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib import messages

from .forms import ContactForm
from .tasks import task_send_email
from .data import images_ubytovani, places, food_menu, drinks_menu



def accommodation(request):

    base_url = reverse('accommodation:accommodation')
    contact_section = f"{base_url}#contact-form"  

    if request.method == 'GET':

        form = ContactForm()
        context = {
            'form': form,
            'images': images_ubytovani,
        }

        return render(request, 'accommodation/ubytovani.html', context)        


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            # handle_email(form.cleaned_data['email'], form.cleaned_data['full_name'], form.cleaned_data['phone'], form.cleaned_data['email'], form.cleaned_data['note'], form.cleaned_data['date_arrival'], form.cleaned_data['date_departure'])

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
            return render(request, 'accommodation/ubytovani.html', context)
