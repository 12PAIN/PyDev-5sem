import osm2geojson
import json


file = open('map', 'r', encoding='utf-8')

newFile = open('shpFile.geojson', 'w', encoding='utf-8')

data = osm2geojson.xml2geojson(file.read(), filter_used_refs=False, raise_on_failure=False)

newFile.write(json.dumps(data))

