#!/usr/bin/python3
import requests

headers = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-mpegURL'
}

master_url = "https://tvcdn.onrender.com/iptv-query"
params = {'url': 'https://www.fox.com.tr/canli-yayin?m3u8'}

response = requests.head(master_url, params=params, headers=headers)

final_url = response.url

print(final_url)
