import requests
from bs4 import BeautifulSoup
import re

url = 'https://hls-players.dzsecurity.net/live/player/elhayattv'
referer_url = 'https://elhayat.dz/'

headers = {
    'Referer': referer_url
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

script_tags = soup.find_all('script')

m3u8_url = None

m3u8_pattern = re.compile(r'https?://[^\s]+\.m3u8[^\s]*')

for script in script_tags:
    if script.string:
        match = m3u8_pattern.search(script.string)
        if match:
            m3u8_url = match.group()
            break

if m3u8_url:
    print(f'Found m3u8 URL: {m3u8_url}')
else:
    print('No m3u8 URL found.')
