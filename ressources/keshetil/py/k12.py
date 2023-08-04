#! /usr/bin/python3

import requests
import os
import sys
import json

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-STREAM-INF:BANDWIDTH=2622400,AVERAGE-BANDWIDTH=2525600,CODECS="avc1.4d4028,mp4a.40.2",RESOLUTION=1280x720,FRAME-RATE=50.000')
s = requests.Session()
toki = s.get('https://mass.mako.co.il/ClicksStatistics/entitlementsServicesV2.jsp?et=ngt&lp=/direct/hls/live/2033791/k12/index.m3u8?as=1&rv=AKAMAI').json()['tickets'][0]['ticket']
master = 'https://mako-streaming.akamaized.net/direct/hls/live/2033791/k12/index.m3u8'
final_master = f'{master}?{toki}'
print(final_master)

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

chunks = get_specific_line_online(final_master, 11)
if chunks:
    chunked = f'https://mako-streaming.akamaized.net/direct/hls/live/2033791/k12/{chunks}'
    print(chunked)
else:
    print("Failed to get the specific line from the online file.")
