#! /usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:6')
print('#EXT-X-STREAM-INF:BANDWIDTH=3412864,AVERAGE-BANDWIDTH=2891084,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.4D401F,mp4a.40.2",SUBTITLES="subtitles",AUDIO="audio_0"')

s = requests.Session()
response = s.get(f'https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/btv/py/lci.m3u8')
string = response.text.strip()  # Strip newline characters
new_string = string.replace("index", "index_1")
print(new_string)
print('#EXT-X-STREAM-INF:BANDWIDTH=1168895,AVERAGE-BANDWIDTH=1021120,RESOLUTION=640x360,FRAME-RATE=25.000,CODECS="avc1.42C01E,mp4a.40.2",SUBTITLES="subtitles",AUDIO="audio_0"')
new2_string = string.replace("index", "index_4")
print(new2_string)
new3_string = string.replace("index", "index_12_0")
print('#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_0",CHANNELS="2",NAME="français",LANGUAGE="frb",DEFAULT=YES,AUTOSELECT=YES,URI="{}"'.format(new3_string), end='')
