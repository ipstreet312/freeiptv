#! /usr/bin/python3
import requests
import json

print('#EXTM3U')

# Equidia TV
url = 'https://api.equidia.fr/api/public/racing/directs/live2/hls?urlOnly=true'
response = requests.get(url)
response_json = json.loads(response.text)

response = requests.get(response_json['url'])
response_json = json.loads(response.text)

print('#EXTINF:0,Equidia')
print(response_json['primary'])


# Racing Trot
url = 'https://api.equidia.fr/api/public/racing/directs/racingtrot/hls?urlOnly=true'
response = requests.get(url)
response_json = json.loads(response.text)

response = requests.get(response_json['url'])
response_json = json.loads(response.text)

print('#EXTINF:0,Racing Trot')
print(response_json['primary'])

# Racing Galop
url = 'https://api.equidia.fr/api/public/racing/directs/racinggalop/hls?urlOnly=true'
response = requests.get(url)
response_json = json.loads(response.text)

response = requests.get(response_json['url'])
response_json = json.loads(response.text)

print('#EXTINF:0, Racing Galop')
print(response_json['primary'])

# Racing Mag
url = 'https://api.equidia.fr/api/public/racing/directs/racingmag/hls?urlOnly=true'
response = requests.get(url)
response_json = json.loads(response.text)

response = requests.get(response_json['url'])
response_json = json.loads(response.text)

print('#EXTINF:0,Racing Galop')
print(response_json['primary'])

