from django.urls import path

from map.views import viewmap

app_name = 'database'

urlpatterns = [
    path('', viewmap, name='map'),
]
