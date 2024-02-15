import requests
import re

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:BANDWIDTH=1755600,RESOLUTION=1280x720,CODECS="avc1.64001f,mp4a.40.2"')

url = "https://tvmi.mt/live/2"
response = requests.get(url)

if response.status_code == 200:
    site_content = response.text
    match = re.search(r'data-jwt="(.*?)"', site_content)
    
    if match:
        data_jwt_value = match.group(1)
        live_url_main = f"https://dist9.tvmi.mt/{data_jwt_value}/live/2/0/index.m3u8"
        print(live_url_main)
    else:
        print("https://Live URL not found in the content.")
else:
    print("https://Failed to fetch the website content.")
