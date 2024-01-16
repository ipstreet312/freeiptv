#!/usr/bin/python3

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Referer": "http://www.callofliberty.fr/"
}

print('#EXTM3U')
print('#EXT-X-STREAM-INF:BANDWIDTH=7680000')

url = "http://s2.callofliberty.fr/direct/CSTAR/master.m3u8"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    lines = response.text.splitlines()
    if len(lines) >= 3:
        my_line = lines[2]
    else:
        print("The file has less than 3 lines.")
else:
    print("Failed to fetch the content. Status code:", response.status_code)

url_part = my_line.split('"')[1]

start_index = url_part.find('https://')
end_index = url_part.find('m3u8')

required_url_segment = url_part[start_index:end_index]
print(required_url_segment + "m3u8")
