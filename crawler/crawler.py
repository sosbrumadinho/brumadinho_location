# -*- coding: utf-8 -*-

import re
import csv
import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup

class Crawler:

    def get_raw_data(self):
        url = "http://brumadinho.vale.com/listagem-pessoas-sem-contato.html"
        r = requests.get(url)
        r.encoding = 'utf-8'
        return r.content

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.text
        ultima_atualizacao = re.search('(?<=atualização em ).+(?=\.)', text).group()
        ultima_atualizacao = ultima_atualizacao[:10]
        nomes = [i.text.strip() for i in soup.find_all('li')]
        return (ultima_atualizacao, nomes)

if __name__ == "__main__":
    crawler = Crawler()
    html = crawler.get_raw_data()
    dt, pessoas = crawler.parse_html(html)
    
    with open('data.csv', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile)
        with open('data_compare.csv', 'w', encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(('Nome', 'Última Atualização', 'Status'))
            for row in spamreader:
                t = 'Não Encontrado'
                for pessoa in pessoas:
                    if row[0] == pessoa.encode('utf-8'):
                        t = ' - '
                csv_writer.writerow((row[0], dt, t))