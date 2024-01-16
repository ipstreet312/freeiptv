#!/usr/bin/python3

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Referer": "http://www.callofliberty.fr/"
}

print('#EXTM3U')
print('#EXT-X-STREAM-INF:RESOLUTION=848x477,FRAME-RATE=50.000000,BANDWIDTH=1667072,CODECS="avc1.64001f,mp4a.40.2",NAME="480@60"')

url = "http://s2.callofliberty.fr/direct/C8/master.m3u8"

try:
    response = requests.get(url)

    if response.status_code == 200:
        lines = response.text.splitlines()
        if len(lines) >= 5:
            third_line = lines[2]
        else:
            print("The file has less than 5 lines.")
            exit(1)
    else:
        print("Failed to fetch the content. Status code:", response.status_code)
        exit(1)

    url_part = third_line.split('"')[1]

    start_index = url_part.find('https://')
    end_index = url_part.find('m3u8')

    required_url_segment = url_part[start_index:end_index]
    print(required_url_segment + "m3u8")

except Exception as e:
    print("An error occurred:", e)
    exit(1)
