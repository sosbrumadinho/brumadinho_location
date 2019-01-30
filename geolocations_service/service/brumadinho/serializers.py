# from django.contrib.auth.models import Group
from brumadinho.models import Geolocation, VisitedLocation
from rest_framework import serializers


class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = "__all__"


class VisitedLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitedLocation
        fields = "__all__"
