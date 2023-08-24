#!/usr/bin/python3

import requests
import os
import sys

na = 'https://empty'
print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000')

try:
    s = requests.Session()
    response = s.get(f'https://www.dailymotion.com/player/metadata/video/x8i9j7s').json()['qualities']['auto'][0]['url']
    m3u = s.get(response).text
    m3u = m3u.strip().split('\n')[1:]
    d = {}
    cnd = True
    for item in m3u:
        if cnd:
            resolution = item.strip().split(',')[2].split('=')[1]
            if resolution not in d:
                d[resolution] = []
            else:
                d[resolution] = item
            cnd = not cnd
    m3u = d[max(d, key=int)]
except Exception as e:
    m3u = na
finally:
    print(m3u)
