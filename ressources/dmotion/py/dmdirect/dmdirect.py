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
    current_category = None
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        elif line.startswith('https://'):
            if current_category == 'fb':
                with open(output_fb, 'a') as file_fb:
                    m3u_content = snif(line)
                    file_fb.write(m3u_content + '\n')
            elif current_category == 'porto':
                with open(output_porto, 'a') as file_porto:
                    m3u_content = snif(line)
                    file_porto.write(m3u_content + '\n')
        else:
            current_category = line  # Update current category for the URLs to follow
