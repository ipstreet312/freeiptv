#! /usr/bin/python3
import requests
import os
import sys
import json
import time
os.system("clear")

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-STREAM-INF:BANDWIDTH=2622400,AVERAGE-BANDWIDTH=2525600,CODECS="avc1.4d4028,mp4a.40.2",RESOLUTION=1280x720,FRAME-RATE=50.000')

session = requests.Session()
response = session.post('https://mass.mako.co.il/ClicksStatistics/entitlementsServicesV2.jsp', params={'et':'gt', 'lp':'/direct/hls/live/2033791/k12/index.m3u8?as=1','rv':'AKAMAI'})

response_json = json.loads(response.text)
g1 = 'https://mako-streaming.akamaized.net/direct/hls/live/2033791/k12/index.m3u8?' + response_json['tickets'][0]['ticket']

res2 = requests.get(g1)
data = res2.text

print(data)
sys.stdout=open("k12a.txt","w")
print(data)
sys.stdout.close()

content = data.readlines()[10:10]
g3 = 'https://mako-streaming.akamaized.net/direct/hls/live/2033791/k12/' + content

print(g3)
