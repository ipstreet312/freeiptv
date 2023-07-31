#! /usr/bin/python3

import requests
import os
import sys

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000')
s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://simulcast-p.ftven.fr/simulcast/France_2/hls_fr2/index.m3u8')
print(response.text)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
