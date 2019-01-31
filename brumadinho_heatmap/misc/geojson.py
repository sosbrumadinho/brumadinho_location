#! usr/bin/env python

from sys import argv
from os.path import exists
import json

script, in_file, out_file = argv

with open(in_file) as f:
    data = json.load(f)

new_data = []
for row in data['results']:
    new_data.append(row)

geojson = {
    "type": "FeatureCollection",
    "features": [{
      "type": "Feature",
      "properties":{},
      "geometry": {
            "type": "Point",
            "coordinates": [
            d['longitude'],
            d['latitude']
            ]
        }
    } for d in new_data]
        
}


output = open(out_file, 'w')
json.dump(geojson, output)

print geojson