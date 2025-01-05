from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib import messages

from .models import News, HomeCarousel
from .data import images_ubytovani, places, food_menu, drinks_menu


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




   









# def handle_email(email_from, full_name, phone, email, note, date_arrival, date_departure):    
#     subject = 'Nová zpráva z webu Prachovec'
#     message = 'Jméno: ' + full_name + '\n' + 'Telefon: ' + phone + '\n' + 'Email: ' + email + '\n' + 'Poznámka: ' + note + '\n' + 'Datum příjezdu: ' + str(date_arrival) + '\n' + 'Datum odjezdu: ' + str(date_departure)
#     email_from = email_from
#     recipient_list = ['synek.o@seznam.cz',]   
#     send_mail( subject, message, email_from, recipient_list )  




    

