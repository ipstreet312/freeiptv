#! /usr/bin/python3

import requests
import os
import sys
import time
import re

headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Referer": "http://www.callofliberty.fr/"
}

s = requests.Session()
response = s.get('http://www.callofliberty.fr/stream/TF1/master.m3u8', headers=headers)

#print(response.text)

def extract_desired_part(url):
    pattern = r'tf1\.fr/(.*?)/out/v1/780542f516f143fc8ad9bf14622316e7/tf1-cmaf/index_4'

    match = re.search(pattern, url)
    
    if match:
        extracted_part = match.group(1)
    else:
        extracted_part = None
    
    return extracted_part

links = re.findall(r'https?://\S+', response.text)

desired_parts = []

for link in links:
    extracted_part = extract_desired_part(link)
    if extracted_part:
        desired_parts.append(extracted_part)
            
result = ' '.join(desired_parts)
print(result)
