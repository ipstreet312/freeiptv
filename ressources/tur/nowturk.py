#!/usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:BANDWIDTH=1050000,AVERAGE-BANDWIDTH=950000,RESOLUTION=1280x720')

master_url = "https://tvcdn.onrender.com/iptv-query?url=https://www.fox.com.tr/canli-yayin?m3u8"
s = requests.Session()

def get_specific_line_online(url, line_number):
    response = s.get(url)
    if response.status_code == 200:
        lines = response.text.split('\n')
        if 1 <= line_number <= len(lines):
            return lines[line_number - 1]
        else:
            return None
    else:
        return None

chunks = get_specific_line_online(master_url, 4)
prefix = "https://foxtv.daioncdn.net/foxtv/"
shortchunks = chunks + str(len(prefix))

print(shortchunks)
print('#EXT-X-STREAM-INF:BANDWIDTH=800000,AVERAGE-BANDWIDTH=700000,RESOLUTION=854x480')
modified_url01 = shortchunks.replace("720p", "480p")
print(modified_url01)
print('#EXT-X-STREAM-INF:BANDWIDTH=550000,AVERAGE-BANDWIDTH=500000,RESOLUTION=640x360')
modified_url02 = shortchunks.replace("720p", "360p")
print(modified_url02)
