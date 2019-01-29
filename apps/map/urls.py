from django.urls import path

from apps.map.views import viewmap

app_name = 'map'

urlpatterns = [
    path('', viewmap, name='map'),
]
