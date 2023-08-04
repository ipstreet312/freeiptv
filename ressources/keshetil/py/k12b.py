#! /usr/bin/python3

import requests
import os
import sys

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-STREAM-INF:BANDWIDTH=2622400,AVERAGE-BANDWIDTH=2525600,CODECS="avc1.4d4028,mp4a.40.2",RESOLUTION=1280x720,FRAME-RATE=50.000')
s = requests.Session()
chunky = s.get('https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/keshetil/py/k12.m3u8')

def get_specific_line_online(url, line_number):
    response = requests.get(url)
    if response.status_code == 200:
        lines = response.text.split('\n')
        if 1 <= line_number <= len(lines):
            return lines[line_number - 1]
        else:
            return None
    else:
        return None

chunkres = get_specific_line_online(chunky, 11)
if chunkres:
    chunked = f'https://mako-streaming.akamaized.net/direct/hls/live/2033791/k12/{chunkres}'
    print(chunked)
else:
    print("Failed to get the specific line from the online file.")
