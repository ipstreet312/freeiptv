#!/usr/bin/python3
# Thanks to azgaresncf/strm2hls
import requests
import sys

url = f'https://www.dailymotion.com/player/metadata/video/x3wqv8b'
response = requests.get(url).json()
stream_url = response['qualities']['auto'][0]['url']
m3u = requests.get(stream_url).text
print(m3u)
