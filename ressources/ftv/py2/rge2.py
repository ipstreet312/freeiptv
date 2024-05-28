#!/usr/bin/python3

import requests
import re

proxies = {
  "http": "http://51.195.137.60:80",
  "https": "https://51.38.191.151:80",
}

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-STREAM-INF:CODECS="avc1.640029,mp4a.40.2",AVERAGE-BANDWIDTH=4611200,RESOLUTION=1280x720,FRAME-RATE=50.0,BANDWIDTH=7208960')

s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-event.ftven.fr/dai/v1/master/f6695408824c1f922e63365d0de48c5fa3251476/events_RG_2/out/v1/5ec6845a2f35467faa8e075ba0fe7752/index_france-domtom.m3u8')

string = response.text
response2 = s.get(string, proxies=proxies)

pattern = re.compile(r'/([\da-fA-F-]+?)/\d\.m3u8')
match = pattern.search(response2.text)
sessid = match.group(1)

new_string = string.replace("master", "manifest").replace("out/v1/5ec6845a2f35467faa8e075ba0fe7752/index_france-domtom.m3u8", f'{sessid}/4.m3u8')
print(new_string)
