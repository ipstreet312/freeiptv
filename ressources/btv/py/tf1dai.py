#! /usr/bin/python3

import requests
import json

response = requests.get('https://raw.githubusercontent.com/Paradise-91/ParaTV/refs/heads/main/streams/tf1plus/tf1_ssai.m3u8')
lines = response.text.splitlines()
greplink = lines[2]

print('#EXTM3U')
print('#EXT-X-VERSION:6')
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-STREAM-INF:BANDWIDTH=3165091,AVERAGE-BANDWIDTH=2856368,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.4D401F,mp4a.40.2",AUDIO="audio_0"')
new_string = greplink.replace("index", "index_1")
print(new_string)
print('#EXT-X-STREAM-INF:BANDWIDTH=1070722,AVERAGE-BANDWIDTH=986404,RESOLUTION=640x360,FRAME-RATE=25.000,CODECS="avc1.42C01E,mp4a.40.2",AUDIO="audio_0"')
new2_string = greplink.replace("index", "index_4")
print(new2_string)
new3_string = greplink.replace("index", "index_12_0")
print('#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_0",CHANNELS="2",NAME="fra",LANGUAGE="fra",DEFAULT=YES,AUTOSELECT=YES,URI="{}"'.format(new3_string), end='')
