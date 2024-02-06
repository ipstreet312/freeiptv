#!/usr/bin/python3

import requests
import re

print('#EXTM3U')
print('#EXT-X-VERSION:4')
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-STREAM-INF:CODECS="avc1.64001F,mp4a.40.2",AVERAGE-BANDWIDTH=2857132,RESOLUTION=1280x720,SUBTITLES="subtitles",FRAME-RATE=25.0,BANDWIDTH=3019038,AUDIO="audio_0"')

s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-ssai.ftven.fr/dai/v1/master/14bff07f70f2518f32f1c6cc13a91ef489dc83f1/SSARFrance2OTTEMTConfiguration/out/v1/535afd7806de45fea4e030b74cea3b8f/index.m3u8')

#string = response.text
#print(string)
pattern = re.compile(r'/([\da-fA-F-]+?)/\d\.m3u8')
match = pattern.search(response)
sessid = match.group(1)

new_string = string.replace("master", "manifest")
new_string2 = new_string.replace("out/v1/535afd7806de45fea4e030b74cea3b8f/index.m3u8", f'{sessid}/4.m3u8')
print(new_string2)

new2_string = new_string2.replace("/4.m3u8", "/6.m3u8")
print(f'#EXT-X-MEDIA:LANGUAGE="fra",AUTOSELECT=YES,CHANNELS="2",FORCED=NO,TYPE=AUDIO,URI="{new2_string}",GROUP-ID="audio_0",DEFAULT=YES,NAME="1 Francais"')
