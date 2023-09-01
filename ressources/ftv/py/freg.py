#! /usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:4')
print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=3019179,RESOLUTION=1280x720,FRAME-RATE=25.000,AUDIO="audio1",SUBTITLES="subs"')
s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-regions-p.ftven.fr/hls/live/2037716/F3_Paris_IDF/index.m3u8')

string = response.text
new_string = string.replace("index", "stream04/streamPlaylist")
print(new_string)
new2_string = string.replace("index", "stream05/streamPlaylist")
print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio1",NAME="FRA",DEFAULT=YES,AUTOSELECT=YES,LANGUAGE="FRA",URI="{new2_string}"')
