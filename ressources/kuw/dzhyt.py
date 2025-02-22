#! /usr/bin/python3

import requests

s = requests.Session()

link = "https://cdnet.alwaysdata.net/dzhayat.php?m3u8"

headers = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-mpegURL'
}

response = s.get(link, headers=headers)

print(response.text)
