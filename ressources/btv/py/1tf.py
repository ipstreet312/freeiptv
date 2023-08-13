#! /usr/bin/python3

import requests
import os
import sys
import time
import re
import fileinput

headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Referer": "http://www.callofliberty.fr/"
}

s = requests.Session()
response = s.get('http://www.callofliberty.fr/stream/TF1/master.m3u8', headers=headers)

#print(response.text)



def extract_desired_part(url):
    pattern = r'http://www.callofliberty.fr/HLS-AES/(.*?)_4\.m3u8'
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


updated_content = f"{result}.m3u8"

# Open the file for in-place editing
with fileinput.FileInput("all.m3u", inplace=True) as file:
    for line in file:
        if "tf1-cmaf" in line:
            print(updated_content)
        else:
            print(line, end="")
