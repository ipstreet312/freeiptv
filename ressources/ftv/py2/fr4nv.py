#! /usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:5')
print('#EXT-X-STREAM-INF:BANDWIDTH=3032655,AVERAGE-BANDWIDTH=2756959,CODECS="avc1.64001f,mp4a.40.2",RESOLUTION=1280x720,FRAME-RATE=25.000,AUDIO="audio-AACL-96",SUBTITLES="text"')

s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://simulcast-b.ftven.fr/simulcast/France_4/hls_fr4/index.m3u8')

string = response.text
new_string = string.replace("index", "France_4-avc1_2500000=10001")
print(new_string)
new2_string = string.replace("index", "France_4-mp4a_96000_fra=20000")
print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-AACL-96",LANGUAGE="fr",NAME="Francais",DEFAULT=YES,AUTOSELECT=YES,CHANNELS="2",URI="{new2_string}"')
