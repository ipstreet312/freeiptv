#! /usr/bin/python3

import streamlink
import requests
streams = streamlink.streams('https://vimeo.com/event/4819137')
master = streams["best"].multivariant.uri

hls_v1 = master.replace("hls.", "chunklist_b3000000_cmaf_v.")
hls_v2 = master.replace("hls.", "chunklist_b600000_cmaf_v.")
hls_a1 = master.replace("hls.", "chunklist_b256000_cmaf_a.")
hls_a2 = master.replace("hls.", "chunklist_b128000_cmaf_a.")

print('#EXTM3U')
print('#EXT-X-VERSION:6')
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-MEDIA:GROUP-ID="audio_256000",TYPE=AUDIO,LANGUAGE="en",NAME="English",AUTOSELECT=YES,DEFAULT=YES,CHANNELS="2",URI="{}"'.format(hls_a1))
print('#EXT-X-MEDIA:GROUP-ID="audio_128000",TYPE=AUDIO,LANGUAGE="en",NAME="English",AUTOSELECT=YES,DEFAULT=YES,CHANNELS="2",URI="{}"'.format(hls_a2))
print('#EXT-X-STREAM-INF:BANDWIDTH=3256000,AVERAGE-BANDWIDTH=2959999,CODECS="avc1.640020,mp4a.40.2",FRAME-RATE=30,RESOLUTION=1280x720,AUDIO="audio_256000"')
print(hls_v1)
print('#EXT-X-STREAM-INF:BANDWIDTH=728000,AVERAGE-BANDWIDTH=661817,CODECS="avc1.64001e,mp4a.40.2",FRAME-RATE=30,RESOLUTION=640x360,AUDIO="audio_128000"')
print(hls_v2)
