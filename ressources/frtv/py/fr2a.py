#! /usr/bin/python3

import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
	'Connection': 'keep-alive',
	'Content-Type': 'application/x-mpegURL',
	'Location': '.$link
}

session = requests.Session()
response = session.get('https://hdfauth.ftven.fr/esi/TA?format=json&url=https://simulcast-p.ftven.fr/simulcast/France_2/hls_fr2/index.m3u8')

response_json = json.loads(response.text)
g1 = response_json["url"]
res2 = requests.get(g1)
data = res2.text
print(data)
