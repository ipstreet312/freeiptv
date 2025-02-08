#! /usr/bin/python3

import requests

s = requests.Session()
response = s.get('http://eqpetv.php?m3u8')

print(response.text)
