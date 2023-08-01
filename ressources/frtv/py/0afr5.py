#! /usr/bin/python3

import requests
import os
import sys

s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://simulcast-p.ftven.fr/simulcast/France_5/hls_fr5/index.m3u8')
print(response.text)
