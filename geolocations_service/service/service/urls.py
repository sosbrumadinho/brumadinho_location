from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from rest_framework import routers

from brumadinho import views


router = routers.DefaultRouter()
router.register(r'geolocations', views.GeolocationViewSet)
router.register(r'visited_locations', views.VisitedLocationViewSet)
router.register(r'found_people', views.FoundPeopleViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'api/', include(router.urls)),
    # url(r'ˆapi-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
