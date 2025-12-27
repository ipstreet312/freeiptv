#! /usr/bin/python3
import requests
print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-STREAM-INF:BANDWIDTH=4569743,AVERAGE-BANDWIDTH=2962182,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.64001F,mp4a.40.2"')
s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-event.ftven.fr/out/v1/0182e82ea7dd4a35bac4ad93784ac239/index_france-domtom_5.m3u8')
string = response.text
print(string)
