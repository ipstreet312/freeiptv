#! /usr/bin/python3

import requests
import json

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:BANDWIDTH=2270400,RESOLUTION=1280x720')

json_url = "https://evangiletv-live1-p-api.hexaglobe.net/6f03aa16ae355fbda86e6d0cb1751001/1720076464/evangiletv/EvangileTV-website-web-1/live1/stream_info.php"
response = requests.get(json_url)
data = response.json()
primary_url = data.get("primary")
new_string = primary_url.replace("playlist", "evangiletvlive1_fre_1")
print(new_string)
