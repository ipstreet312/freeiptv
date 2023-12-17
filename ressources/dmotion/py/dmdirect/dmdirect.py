#!/usr/bin/python3
import requests

def snif(line):
    try:
        idvideo = line.split('/')[4]
        url = f'https://www.dailymotion.com/player/metadata/video/{idvideo}'
        response = requests.get(url).json()
        stream_url = response['qualities']['auto'][0]['url']
        m3u = requests.get(stream_url).text
    except Exception as e:
        m3u = 'https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/infos/barkers/info.m3u8'
    
    return m3u

output_fb = 'ressources/dmotion/py/dmdirect/fb.m3u8'
output_porto = 'ressources/dmotion/py/dmdirect/porto.m3u8'

with open('ressources/dmotion/py/dmdirect/dmid.txt') as f:
    fb_lines = []
    porto_lines = []
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        else:
            if '#fb' in line:
                fb_lines.append(line)
            elif '#porto' in line:
                porto_lines.append(line)

    if fb_lines:
        with open(output_fb, 'a') as file_fb:
            for line in fb_lines:
                file_fb.write(line + '\n')
                m3u_content = snif(line)
                file_fb.write(m3u_content + '\n')

    if porto_lines:
        with open(output_porto, 'a') as file_porto:
            for line in porto_lines:
                file_porto.write(line + '\n')
                m3u_content = snif(line)
                file_porto.write(m3u_content + '\n')
