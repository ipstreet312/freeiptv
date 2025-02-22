import requests
import re

url = 'https://hls-players.dzsecurity.net/live/player/elhayattv'
referer_url = 'https://elhayat.dz/'

headers = {
    'Referer': referer_url
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    pattern = r"(https?://[^\s'\"]+\.m3u8[^\s'\"]*)"
    match = re.search(pattern, response.text)
  
    if match:
        strm = match.group(1)
        print(f"Found m3u8 URL: {strm}")
    else:
        print("m3u8 URL not found in the content.")
else:
    print(f"Failed to fetch content. HTTP Status code: {response.status_code}")
