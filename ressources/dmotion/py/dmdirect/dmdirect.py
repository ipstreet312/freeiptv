import requests
import os

def snif(line):
    try:
        idvideo = line.split('/')[-1]
        url = f'https://www.dailymotion.com/player/metadata/video/{idvideo}'
        response = requests.get(url).json()
        stream_url = response['qualities']['auto'][0]['url']
        m3u = requests.get(stream_url).text
    except Exception as e:
        m3u = 'https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/infos/barkers/info.m3u8'
    
    return m3u

output_directory = 'ressources/dmotion/py/dmdirect'
os.makedirs(output_directory, exist_ok=True)

with open('ressources/dmotion/py/dmdirect/dmid.txt') as f:
    current_category = None
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        elif line.startswith('#'):
            current_category = line[1:]
        elif line.startswith('https://'):
            if current_category:
                file_name = f"{current_category.strip()}.m3u8"
                file_path = os.path.join(output_directory, file_name)
                m3u_content = snif(line)
                with open(file_path, 'w') as file:
                    file.write(m3u_content)
