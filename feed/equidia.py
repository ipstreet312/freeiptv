#! /usr/bin/python3
# Thanks to pshanmu3 user on github
import requests
import os
import sys

proxies = {}
if len(sys.argv) == 3:
    proxies = {
                'http' : sys.argv[2],
                'https' : sys.argv[2]
              }

na = 'https://raw.githubusercontent.com/naveenland4/UTLive/main/assets/info.m3u8'
def grab(url):
    try:
        m3u = s.get(url, proxies=proxies).json()['primary']
    except Exception as e:
        m3u = na
    finally:
        print(m3u)

print('#EXTM3U')
print('#EXT-X-VERSION:3')
s = requests.Session()

if (sys.argv[1] == 'equidia'):
    url = 'https://equidia-live2-p-api.hexaglobe.net/0d62898eeb26305306d2af3e6ec3d54d/64b8fb4b/equidia/equidia-website-web-1/live2/stream_info.php'
elif (sys.argv[1] == 'trot'):
    url = 'https://equidia-racingtrot-p-api.hexaglobe.net/922e164eef4e2f1defad606e9e86b3bc/64be43f5/equidia/equidia-website-web-1/racingtrot/stream_info.php'
elif (sys.argv[1] == 'galop'):
    url = 'https://equidia-racinggalop-p-api.hexaglobe.net/80ae8d56ed752fb9f94b3f02bf1feb94/64be4408/equidia/equidia-website-web-1/racinggalop/stream_info.php'
elif (sys.argv[1] == 'mag'):
    url = 'https://equidia-racingmag-p-api.hexaglobe.net/fb5cf335df8269937855aff5e4734a3d/64b8fb7f/equidia/equidia-website-web-1/racingmag/stream_info.php'
else:
    sys.exit(1)

grab(url)
