from django.urls import path, include

from apps.api.views import calculatecoordinate, crawler

app_name = 'api'

urlpatterns = [
    path('calculate', calculatecoordinate, name='coordinate_calculate'),
]
