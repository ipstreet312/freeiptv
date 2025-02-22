import requests
import re

url = 'https://hls-players.dzsecurity.net/live/player/elhayattv'
referer = 'https://elhayat.dz/'

headers = {
    'Referer': referer
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    m3u8_url = re.search(r'https://.*?\.m3u8', response.text)
    if m3u8_url:
        m3u8_url = m3u8_url.group()
        print(f'Found m3u8 URL: {m3u8_url}')
    else:
        print('No m3u8 URL found.')
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
