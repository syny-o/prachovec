from django.shortcuts import render

def home(request):
    return render(request, 'mysite/home.html')


def ubytovani(request):
    return render(request, 'mysite/ubytovani.html')


def obcerstveni(request):
    return render(request, 'mysite/obcerstveni.html')

