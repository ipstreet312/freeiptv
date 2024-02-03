#!/usr/bin/python3
import requests
master_url = "https://tvcdn.onrender.com/iptv-query?url=https://www.fox.com.tr/canli-yayin?m3u8"
s = requests.Session()
response = s.get(master_url)
print(response)
