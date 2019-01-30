from django.urls import path

from apps.api.views import calculatecoordinate, crawler

app_name = 'api'

urlpatterns = [
    path('calculate', calculatecoordinate, name='coordinate_calculate'),
]
