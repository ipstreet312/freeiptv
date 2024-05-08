#!/usr/bin/python3

import requests
import re

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:BANDWIDTH=2855600,AVERAGE-BANDWIDTH=2479236,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.640020,mp4a.40.2"')

s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https%3A%2F%2Flive-olympics.ftven.fr%2Fparis2024-francedomtom%2Fmaster.m3u8')
string = response.text

new_string = string.replace("master", "b0EF_720p/playlist")
print(new_string)
