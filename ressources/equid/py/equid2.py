#! /usr/bin/python3

import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

session = requests.Session()
response = session.get('https://equidia-live2-p-api.hexaglobe.net/0d62898eeb26305306d2af3e6ec3d54d/64b8fb4b/equidia/equidia-website-web-1/live2/stream_info.php')

if response.status_code == 200:
    response_json = json.loads(response.text)
    g1 = response_json["primary"]
    print(g1)
else:
    print("La requête n'a pas abouti avec le code :", response.status_code)
