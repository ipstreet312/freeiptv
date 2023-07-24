#! /usr/bin/python3
import requests
import json
import time

print('#EXTM3U')
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get('https://equidia-live2-p-api.hexaglobe.net/0d62898eeb26305306d2af3e6ec3d54d/64b8fb4b/equidia/equidia-website-web-1/live2/stream_info.php')
response_json = json.loads(response.text)
print('#EXTINF:0, Equidia TV')
print(response_json['primary'])