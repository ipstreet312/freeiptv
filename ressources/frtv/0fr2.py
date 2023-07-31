#! /usr/bin/python3

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

session = requests.Session()
response = session.get('https://hdfauth.ftven.fr/esi/TA?url=https://simulcast-p.ftven.fr/simulcast/France_2/hls_fr2/index.m3u8')

print(response)
