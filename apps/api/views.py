from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.serializers import CoordinateSerializer
from apps.api.utils import Position
from django.conf import settings
import re
import csv
import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup


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



def get_raw_data():
    url = "http://brumadinho.vale.com/listagem-pessoas-sem-contato.html"
    r = requests.get(url)
    return r.content

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.text
    ultima_atualizacao = re.search('(?<=atualização em ).+(?=\.)', text).group()
    ultima_atualizacao = datetime.strptime(ultima_atualizacao, '%d/%m/%Y às %H:%M')
    nomes = [i.text.strip() for i in soup.find_all('li')]
    return (ultima_atualizacao, nomes)

def crawler(request):
    html = get_raw_data()
    dt, pessoas = parse_html(html)
    dt = dt.strftime('%d/%m/%Y - %H:%M')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data_compare.csv"'

    with open(os.path.join(settings.BASE_DIR, 'static/data/persons.csv'), 'r') as csvfile:

        spamreader = csv.reader(csvfile)

        csv_writer = csv.writer(response)
        csv_writer.writerow(('Nome', 'Última Atualização', 'Status'))
        for row in spamreader:
            t = 'Encontrado'
            for pessoa in pessoas:
                if row[0] == pessoa:
                    t = ' - '
            csv_writer.writerow((row[0], dt, t))

    return response

