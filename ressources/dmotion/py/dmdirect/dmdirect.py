#! /usr/bin/python3
import requests
import sys

def snif(line):
    try:
        idvideo = line.split('/')[4]
        url = f'https://www.dailymotion.com/player/metadata/video/{idvideo}'
        response = requests.get(url).json()
        stream_url = response['qualities']['auto'][0]['url']
        m3u = requests.get(stream_url).text
    except Exception as e:
        m3u = 'https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/infos/barkers/info.m3u8'
    finally:
        print(m3u)

with open('ressources/dmotion/py/dmdirect/dmid.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            nom = line.strip()
            print(f'{nom}')
        else:
            snif(line)
