#! /usr/bin/python3

import requests
import json


headers={
        "Referer": "https://videojs.tmgrup.com.tr/getvideo/0fe2a405-8afa-4238-b429-e5f96aec3a5c/00000000-0000-0000-0000-000000000000"
}

s = requests.Session()
response = s.get('https://securevideotoken.tmgrup.com.tr/webtv/secure?url=https://trkvz.daioncdn.net/atv/atv.m3u8?ce=3&app=d1ce2d40-5256-4550-b02e-e73c185a314e', headers=headers).json()['Url']
print(response)
