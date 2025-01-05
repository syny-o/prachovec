from django.urls import path, include
from . import views


app_name = 'activities'


urlpatterns = [
    path('', views.activities, name='activities'),
]
