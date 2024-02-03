#!/usr/bin/python3
import requests
response = requests.head('https://tvcdn.onrender.com/iptv-query?url=https://www.fox.com.tr/canli-yayin?m3u8')
final_url = response.url
print(final_url)
