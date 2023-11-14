#!/usr/bin/python3

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Referer": "http://www.callofliberty.fr/"
}

print('#EXTM3U')
print('#EXT-X-STREAM-INF:RESOLUTION=848x477,FRAME-RATE=50.000000,BANDWIDTH=1667072,CODECS="avc1.64001f,mp4a.40.2",NAME="480@60"')

url = "http://s2.callofliberty.fr/direct/C8/02.m3u8"

response = requests.get(url)

if response.status_code == 200:
    lines = response.text.splitlines()
    if len(lines) >= 5:
        fifth_line = lines[4]
    else:
        print("The file has less than 5 lines.")
else:
    print("Failed to fetch the content. Status code:", response.status_code)

url_part = fifth_line.split('"')[1]

start_index = url_part.find('https://')
end_index = url_part.find('key')

required_url_segment = url_part[start_index:end_index]
print(required_url_segment + "m3u8")
