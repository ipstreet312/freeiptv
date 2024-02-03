#!/usr/bin/python3
import requests

s = requests.Session()
response = s.get('https://tvcdn.onrender.com/iptv-query?url=https://www.fox.com.tr/canli-yayin?m3u8')
print(response.text)
