#! /usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=3022199,CODECS="avc1.64001F, mp4a.40.2", RESOLUTION=1280x720, SUBTITLES="subs", AUDIO="audio_1000017564_128"')
s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-series.ftven.fr/bde12330-fbf2-44e7-8a7c-c5f31806460c_1000017564_HLS-francedomtom/manifest.m3u8')

string = response.text
new_string = string.replace("manifest", "video_7201280_p_0")
print(new_string)
new2_string = string.replace("manifest", "A_audio_1000017564_128_fr")
print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_1000017564_128",LANGUAGE="fr",NAME="fr",DEFAULT=YES,AUTOSELECT=YES,URI="{new2_string}"')
