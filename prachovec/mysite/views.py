from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib import messages

from .models import News, HomeCarousel
from .forms import ContactForm
from .tasks import task_send_email


def home(request):

    carousel_images = HomeCarousel.objects.all()
    news = News.objects.all()
    if len(news) > 2:
        news = news[:2]
        
    context = {
        'carousel_images' : carousel_images,
        'news': news,
    }

    return render(request, 'mysite/home.html', context)



def ubytovani(request):

    base_url = reverse('mysite:ubytovani')
    contact_section = f"{base_url}#contact-form"  

    if request.method == 'GET':
        form = ContactForm()
        context = {
            'form': form
        }

        return render(request, 'mysite/ubytovani.html', context)        


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
            return render(request, 'mysite/ubytovani.html', context)
   






def obcerstveni(request):
    return render(request, 'mysite/obcerstveni.html')



# def handle_email(email_from, full_name, phone, email, note, date_arrival, date_departure):    
#     subject = 'Nová zpráva z webu Prachovec'
#     message = 'Jméno: ' + full_name + '\n' + 'Telefon: ' + phone + '\n' + 'Email: ' + email + '\n' + 'Poznámka: ' + note + '\n' + 'Datum příjezdu: ' + str(date_arrival) + '\n' + 'Datum odjezdu: ' + str(date_departure)
#     email_from = email_from
#     recipient_list = ['synek.o@seznam.cz',]   
#     send_mail( subject, message, email_from, recipient_list )  




    

