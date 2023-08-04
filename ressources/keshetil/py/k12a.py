#! /usr/bin/python3

import requests
import os
import sys
import json

s = requests.Session()
toki = s.get('https://mass.mako.co.il/ClicksStatistics/entitlementsServicesV2.jsp?et=ngt&lp=/direct/hls/live/2033791/k12/index.m3u8?as=1&rv=AKAMAI').json()['tickets'][0]['ticket']
master = 'https://mako-streaming.akamaized.net/direct/hls/live/2033791/k12/index.m3u8'
final_master = f'{master}?{toki}'
#print(final_master)
chunks = s.get(final_master)
print(chunks.text)
