from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from apps.api.serializers import CoordinateSerializer
from apps.api.utils import Position



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


calculatecoordinate = CalculateCoordinate.as_view()

