#! /usr/bin/python3

import requests
import os
import sys
import json

headers={
        "User-Agent": "Equidia/6036 CFNetwork/1220.1 Darwin/20.3.0",
        "Referer": "https://fr.equidia.app/"
}
s = requests.Session()
response = s.get('https://api.equidia.fr/api/public/racing/equidia-mobileapp-ios-1/equidia-live2', headers=headers).json()['primary']
#print(response)
print('#EXTM3U')
print('#EXT-X-VERSION:3')
response2 = response.replace("playlist", "slot09_audio_french")
print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="group_aud",NAME="audio_0",DEFAULT=YES,LANGUAGE="fra",URI="{response2}"')
print('#EXT-X-STREAM-INF:BANDWIDTH=2270400,RESOLUTION=1280x720,AUDIO="group_aud"')
print(response.replace("playlist", "slot09_720p"))
