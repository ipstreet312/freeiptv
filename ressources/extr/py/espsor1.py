#! /usr/bin/python3

import requests
import os
import sys
import json


headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34",
        "Referer": "https://player.castr.com/"
}

s = requests.Session()
response = s.get('https://stream.castr.com/63b43410861d94a9eee067fb/live_947330308dd911edb85c8181cb9b11a8/index.m3u8', headers=headers)
base_url = "https://stream.castr.com/63b43410861d94a9eee067fb/live_947330308dd911edb85c8181cb9b11a8/"
lines = (response.text).split('\n')
modified_line = base_url + lines[2]
lines[2] = modified_line
modified_response = '\n'.join(lines)
print(modified_response)
