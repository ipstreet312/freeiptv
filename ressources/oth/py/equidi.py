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
print('#EXT-X-STREAM-INF:BANDWIDTH=2270400,RESOLUTION=1280x720')
print(response.replace("playlist.m3u8", "eqdlive2" + "_fre_1.m3u8"))
