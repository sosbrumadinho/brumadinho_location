from brumadinho.views import GeolocationViewSet, VisitedLocationViewSet, FoundPeopleViewSet
from rest_framework import renderers
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


geolocation_list = GeolocationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

geolocation_detail = GeolocationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

visited_location_list = VisitedLocationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

visited_location_detail = VisitedLocationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

found_people_list = FoundPeopleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

found_people_detail = FoundPeopleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('geolocations/', geolocation_list, name="geolocation-list"),
    path('visited_locations/', visited_location_list, name="visited_location-list"),
    path('found_people/', found_people_list, name="found_people-list"),
])
