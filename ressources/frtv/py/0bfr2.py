#! /usr/bin/python3

import requests

session = requests.Session()
response = session.get('https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/frtv/py/0fr2.m3u8')

print(response)
