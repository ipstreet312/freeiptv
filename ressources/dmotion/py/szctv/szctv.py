#!/usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:RESOLUTION=1280x720,FRAME-RATE=25.000000,BANDWIDTH=2179072,CODECS="avc1.64001f,mp4a.40.2",NAME="720"')

url = 'https://www.dailymotion.com/player/metadata/video/x8i9j7s'
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    video_data = response.json()
    master_url = video_data['qualities']['auto'][0]['url']
    
    def get_specific_line_online(url, line_number):
        response = requests.get(url)
        if response.status_code == 200:
            lines = response.text.split('\n')
            if 1 <= line_number <= len(lines):
                return lines[line_number - 1]
            else:
                return None
        else:
            return None
    
    chunks = get_specific_line_online(master_url, 15)
    print(chunks)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
except KeyError:
    print("Key 'qualities' or its subkeys not found in the JSON data.")
except (ValueError, IndexError):
    print("Error parsing JSON or accessing array index.")
