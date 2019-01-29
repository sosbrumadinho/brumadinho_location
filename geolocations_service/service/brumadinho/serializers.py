# from django.contrib.auth.models import Group
from brumadinho.models import Geolocation, VisitedLocation, FoundPeople
from rest_framework import serializers


class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = "__all__"


class VisitedLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitedLocation
        fields = "__all__"

    location = GeolocationSerializer(
        read_only=True
    )
    location_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Geolocation.objects.all(),
        source="location",
        help_text="Geoposition ID list."
    )

    def validate_encounter_number(self, number):
        return 0 if number < 0 else number

class FoundPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundPeople
        fields = "__all__"

    location = GeolocationSerializer(
        read_only=True,
        required=False,
        allow_null=True
    )
    location_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Geolocation.objects.all(),
        help_text="Geoposition ID list.",
        source="location",
        required=False,
        allow_null=True
    )
