import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from configparser import ConfigParser
from utils import return_vector


class Handler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        json_data = self.rfile.read(int(self.headers['Content-Length']))

        geo_point = json.loads(json_data)
        # lat, lng = -20.135896, -44.123509
        lat, lng = geo_point['lat'], geo_point['lng']
        position = return_vector(lat, lng)

        response = {
            'lat': position[0],
            'lng': position[1],
        }

        self.wfile.write(json.dumps(response).encode())



def run(host='127.0.0.1', port=8080):
    server_address = (host, port)
    httpd = HTTPServer(server_address, Handler)
    # run_server
    httpd.serve_forever()


if __name__ == '__main__':
    cfg = ConfigParser()
    cfg.read('config.ini')
    cfg_port = cfg.getint('server', 'port')
    cfg_host = cfg.get('server', 'host')

    HOST_NAME = cfg_host
    PORT_NUMBER = cfg_port

    run(HOST_NAME, PORT_NUMBER)
