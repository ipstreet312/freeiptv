#! /usr/bin/python3
import requests
import json
import time

print('#EXTM3U')
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Equidia TV
response = requests.get('https://equidia-live2-p-api.hexaglobe.net/0d62898eeb26305306d2af3e6ec3d54d/64b8fb4b/equidia/equidia-website-web-1/live2/stream_info.php')
response_json = json.loads(response.text)
print('#EXTINF:0, Equidia TV')
print(response_json['primary'])

# Racing Trot
response = requests.get('https://equidia-racingtrot-p-api.hexaglobe.net/922e164eef4e2f1defad606e9e86b3bc/64be43f5/equidia/equidia-website-web-1/racingtrot/stream_info.php')
response_json = json.loads(response.text)
print('#EXTINF:0, Equidia Racing Trot')
print(response_json['primary'])

# Racing Galop
response = requests.get('https://equidia-racinggalop-p-api.hexaglobe.net/80ae8d56ed752fb9f94b3f02bf1feb94/64be4408/equidia/equidia-website-web-1/racinggalop/stream_info.php')
response_json = json.loads(response.text)
print('#EXTINF:0, Equidia Racing Galop')
print(response_json['primary'])

# Racing Mag
response = requests.get('https://equidia-racingmag-p-api.hexaglobe.net/fb5cf335df8269937855aff5e4734a3d/64b8fb7f/equidia/equidia-website-web-1/racingmag/stream_info.php')
response_json = json.loads(response.text)
print('#EXTINF:0, Equidia Racing Mag')
print(response_json['primary'])

# Racing 1
response = requests.get('https://equidia-racing1-p-api.hexaglobe.net/65f919388823483b1e41b6d989a2aa01/64be44da/equidia/equidia-website-web-1/racing1/stream_info.php')
response_json = json.loads(response.text)
print('#EXTINF:0, Equidia Racing 1')
print(response_json['primary'])

# Racing 2
response = requests.get('https://equidia-racing2-p-api.hexaglobe.net/34b834c19250f9d04e9345266db8c6ed/64be4477/equidia/equidia-website-web-1/racing2/stream_info.php')
response_json = json.loads(response.text)
print('#EXTINF:0, Equidia Racing 2')
print(response_json['primary'])

# Racing 3
response = requests.get('https://equidia-racing3-p-api.hexaglobe.net/bc4c7ff834a82709c6bd8f4d5b7b9f05/64be4489/equidia/equidia-website-web-1/racing3/stream_info.php')
response_json = json.loads(response.text)
print('#EXTINF:0, Equidia Racing 3')
print(response_json['primary'])

# Racing 4
response = requests.get('https://equidia-racing4-p-api.hexaglobe.net/198ecb5e76739af5dfd046baa716511f/64be44e2/equidia/equidia-website-web-1/racing4/stream_info.php')
response_json = json.loads(response.text)
print('#EXTINF:0, Equidia Racing 4')
print(response_json['primary'])

# Racing 5
response = requests.get('https://equidia-racing5-p-api.hexaglobe.net/bea69d759f8fbdce323fe9f19d9a9831/64be4517/equidia/equidia-website-web-1/racing5/stream_info.php')
response_json = json.loads(response.text)
print('#EXTINF:0, Equidia Racing 5')
print(response_json['primary'])