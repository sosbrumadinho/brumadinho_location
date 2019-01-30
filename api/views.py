from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CoordinateSerializer
from api.utils import Position

from django.conf import settings


class CalculateCoordinate(APIView):
    """
       View to return possible victims coordinates
    """

    def get(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = CoordinateSerializer(request.data)
        lat, lng = serializer.data['lat'], serializer.data['lng']
        vector_position = Position(lat, lng).calc_vector()
        return Response(vector_position, status=status.HTTP_200_OK)


def get_elevation(lat, lng):
    gmaps = googlemaps.Client(key=settings.GMAPS_API_KEY)
    geocode_result = gmaps.elevation((lat, lng))
    return geocode_result[0]['elevation']

calculatecoordinate = CalculateCoordinate.as_view()
