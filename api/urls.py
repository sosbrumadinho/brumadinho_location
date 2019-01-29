from django.urls import path, include

from api.views import calculatecoordinate

app_name = 'api'

urlpatterns = [
    path('calculate', calculatecoordinate, name='coordinate_calculate')
]