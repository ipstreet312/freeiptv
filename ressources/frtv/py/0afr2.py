#! /usr/bin/python3

import requests

session = requests.Session()
response = session.get('https://hdfauth.ftven.fr/esi/TA?url=https://simulcast-p.ftven.fr/simulcast/France_2/hls_fr2/index.m3u8')
linki = session.get(response)
print(linki)
