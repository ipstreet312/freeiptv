#! /usr/bin/python3

import requests

s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-regions-p.ftven.fr/hls/live/2037716/F3_Paris_IDF/index.m3u8')
string = response.text
print(string)
