#! /usr/bin/python3

import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

session = requests.Session()
response = session.get('https://mediainfo.tf1.fr/mediainfocombo/L_LCI?format=hls')

response_json = json.loads(response.text)
g1 = response_json["delivery"]["url"]
print(g1)
