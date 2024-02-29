#! /usr/bin/python3

import requests
import json

print('#EXTM3U')
print('#EXT-X-VERSION:6')
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-STREAM-INF:BANDWIDTH=3165091,AVERAGE-BANDWIDTH=2856368,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.4D401F,mp4a.40.2",AUDIO="audio_0"')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}
s = requests.Session()
resplink = s.get('https://mediainfo.tf1.fr/mediainfocombo/L_LCI?format=hls')
response_json = json.loads(resplink.text)
mastlnk = response_json["delivery"]["url"]
new_string = mastlnk.replace("index", "index_1")
print(new_string)
print('#EXT-X-STREAM-INF:BANDWIDTH=1070722,AVERAGE-BANDWIDTH=986404,RESOLUTION=640x360,FRAME-RATE=25.000,CODECS="avc1.42C01E,mp4a.40.2",AUDIO="audio_0"')
new2_string = mastlnk.replace("index", "index_4")
print(new2_string)
new3_string = mastlnk.replace("index", "index_13_0")
print('#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_0",CHANNELS="2",NAME="fra",LANGUAGE="fra",DEFAULT=YES,AUTOSELECT=YES,URI="{}"'.format(new3_string), end='')
