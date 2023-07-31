#! /usr/bin/python3

import requests
import os
import sys
import time

headers={
        "Referer": "http://www.callofliberty.fr/tv/1-TF1/1-TF1.php/"
}

s = requests.Session()
response = s.get('http://www.callofliberty.fr/stream/TF1/master.m3u8', headers=headers)
print(response.text)
