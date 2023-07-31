#! /usr/bin/python3

import requests
import os
import sys
import time

headers={
        "Referer": "http://www.callofliberty.fr/"
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
}

s = requests.Session()
response = s.get('http://www.callofliberty.fr/stream/TF1/master.m3u8', headers=headers)
print(response.text)
