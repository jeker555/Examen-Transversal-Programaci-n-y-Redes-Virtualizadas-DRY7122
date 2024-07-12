import requests
import urllib.parse
geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Santiago, Región Metropolitana"
loc2 = "Buenos Aires"
key = "92ace2b8-44cc-462e-96ca-1992e558063b" # Reemplazar con su clave de API de Graphhopper

url = geocode_url + urllib.parse.urlencode ({"q": loc1, "limit": "1", "key": key})

replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code
print(json_data)