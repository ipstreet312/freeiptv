#! /usr/bin/python3

import requests
import os
import sys

s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://simulcast-p.ftven.fr/simulcast/France_2/hls_fr2/index.m3u8')
initial_string = response.text

output_files = [
    {'file_name': 'fr2.m3u8', 'variant': 'France_2'},
    {'file_name': 'fr3.m3u8', 'variant': 'France_3'},
    {'file_name': 'fr4.m3u8', 'variant': 'France_4'},
    {'file_name': 'fr5.m3u8', 'variant': 'France_5'}
]

print('#EXTM3U')
print('#EXT-X-VERSION:5')

for output_info in output_files:
    output_file = f'ressources/ftv/py/{output_info["file_name"]}'
    variant = output_info['variant']
    
    print(f'#EXT-X-STREAM-INF:BANDWIDTH=3032655,AVERAGE-BANDWIDTH=2756959,CODECS="avc1.64001f,mp4a.40.2",RESOLUTION=1280x720,FRAME-RATE=25.000,AUDIO="audio-AACL-96",SUBTITLES="text"')
    
    new_string = initial_string.replace("index", f"{variant}-avc1_2500000=10001")
    print(new_string)
    
    new2_string = initial_string.replace("index", f"{variant}-mp4a_96000_fra=20000")
    print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-AACL-96",LANGUAGE="fr",NAME="Francais",DEFAULT=YES,AUTOSELECT=YES,CHANNELS="2",URI="{new2_string}"')
    
    with open(output_file, 'w') as f:
        f.write(new_string)
