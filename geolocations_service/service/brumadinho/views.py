# from django.contrib.auth.models import Group
from brumadinho.models import Geolocation, VisitedLocation, FoundPeople
from rest_framework import viewsets
from brumadinho.serializers import GeolocationSerializer, VisitedLocationSerializer, FoundPeopleSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'users': reverse('user-list', request=request, format=format),
        'geolocations': reverse('geolocation-list', request=request, format=format)
    })


class GeolocationViewSet(viewsets.ModelViewSet):
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer


class VisitedLocationViewSet(viewsets.ModelViewSet):
    queryset = VisitedLocation.objects.all()
    serializer_class = VisitedLocationSerializer


class FoundPeopleViewSet(viewsets.ModelViewSet):
    queryset = FoundPeople.objects.all()
    serializer_class = FoundPeopleSerializer