from django.urls import path, include
from . import views


app_name = 'mysite'


urlpatterns = [
    path('', views.home, name='home'),
    path('ubytovani', views.ubytovani, name='ubytovani'),
    path('obcerstveni', views.obcerstveni, name='obcerstveni'),


]
