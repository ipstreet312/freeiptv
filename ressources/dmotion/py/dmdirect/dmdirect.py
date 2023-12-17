#! /usr/bin/python3
import requests
import sys

def snif(line):
    try:
        idvideo = line.split('/')[4]
        url = f'https://www.dailymotion.com/player/metadata/video/{idvideo}'
        response = requests.get(url).json()
        m3u8 = response["qualities"]["auto"][0]["url"]
        master = requests.get(m3u8).text
    except Exception as e:
        master = 'https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/infos/barkers/info.m3u8'
    finally:
        print(master)

with open('liste/dmid.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        else:
            snif(line)
