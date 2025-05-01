#!/usr/bin/python3

import requests
import re

print('#EXTM3U')
print('#EXT-X-VERSION:4')
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-STREAM-INF:CODECS="avc1.64001F,mp4a.40.2",AVERAGE-BANDWIDTH=2855564,RESOLUTION=1280x720,FRAME-RATE=25.0,BANDWIDTH=3266590,AUDIO="audio_0"')

s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-ssai-p.ftven.fr/dai/v1/master/c6f323e65336fbba9ea766d582216fd61ed74452/SSAIIna70OTTEMTConfiguration/out/v1/cb104b21fb234159b4642dd2975fbd53/index.m3u8')

string = response.text
response2 = s.get(string)

pattern = re.compile(r'/([\da-fA-F-]+?)/\d\.m3u8')
match = pattern.search(response2.text)
sessid = match.group(1)

new_string = string.replace("master", "manifest")
new_string2 = new_string.replace("out/v1/cb104b21fb234159b4642dd2975fbd53/index.m3u8", f'{sessid}/4.m3u8')
print(new_string2)

new2_string = new_string2.replace("/4.m3u8", "/6.m3u8")
print(f'#EXT-X-MEDIA:LANGUAGE="fra",AUTOSELECT=YES,CHANNELS="2",FORCED=NO,TYPE=AUDIO,URI="{new2_string}",GROUP-ID="audio_0",DEFAULT=YES,NAME="1 Francais"')
