#!/usr/bin/python3

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Referer": "http://www.callofliberty.fr/"
}

print('#EXTM3U')
print('#EXT-X-STREAM-INF:BANDWIDTH=7680000')

url = "http://s2.callofliberty.fr/direct/CSTAR/index.m3u8"

response = requests.get(url, headers=headers)

my_line = None  # Initialize my_line outside the if block

if response.status_code == 200:
    lines = response.text.splitlines()
    if len(lines) >= 3:  # The index should be 3 for the third line
        my_line = lines[2]
    else:
        print("The file has less than 3 lines.")
else:
    print("Failed to fetch the content. Status code:", response.status_code)

if my_line is not None:
    # Extract the URL part directly
    url_part_start = my_line.find('https://')
    url_part_end = my_line.find('m3u8') + 4  # Include 'm3u8' in the result

    url_part = my_line[url_part_start:url_part_end]
    print(url_part)
