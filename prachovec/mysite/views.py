from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .models import News


def home(request):
    news = News.objects.all()
    if len(news) > 2:
        news = news[:2]
        
    context = {
        'news': news
    }


    return render(request, 'mysite/home.html', context)


def ubytovani(request):
    return render(request, 'mysite/ubytovani.html')


def obcerstveni(request):
    return render(request, 'mysite/obcerstveni.html')


def email(request):    
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['synek.o@seznam.cz', 'synekjbc@gmail.com']   
    send_mail( subject, message, email_from, recipient_list )  
    return redirect('mysite:home')
    

