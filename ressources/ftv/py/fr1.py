#! /usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2985400,AVERAGE-BANDWIDTH=2714532,CODECS="avc1.64001F, mp4a.40.2",RESOLUTION=1280x720')
s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-outremer.ftven.fr/372a0c4d-b466-4c86-9e40-73ee3e1b7073_0_HLS-m/video_7201280_p_0.m3u8')
string = response.text
print(string)
