#! /usr/bin/python3

import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

session = requests.Session()
response = session.get('https://mediainfo.tf1.fr/mediainfocombo/L_LCI?format=hls')

if response.status_code == 200:
    response_json = json.loads(response.text)
    g1 = response_json["delivery"][0]["url"]
    res2 = requests.get(g1)
    data = res2.text
    print(data)
else:
    print("La requête n'a pas abouti avec le code :", response.status_code)
