#!/usr/bin/python3

import requests
import sys

proxies = {
  "http": "http://51.195.137.60:80",
  "https": "https://51.38.191.151:80",
}

def fetch_response(url):
    s = requests.Session()
    response = s.get(url, proxies=proxies)
    return response.text

def generate_rgc1(string, output_file):
    rgc1_string = string.replace("index_france-domtom", "index_france-domtom_10")
    with open(output_file, "w") as f:
        print('#EXTM3U', file=f)
        print('#EXT-X-VERSION:3', file=f)
        print('#EXT-X-STREAM-INF:BANDWIDTH=4569879,AVERAGE-BANDWIDTH=2962350,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.640029,mp4a.40.2"', file=f)
        print(rgc1_string, file=f)

def generate_rgc2(string, output_file):
    rgc2_string = string.replace("62d41da4cc404a34a0c30851c674f91c", "4cfd7750a803405a8e7d860f01ca00e9").replace("index_france-domtom", "index_france-domtom_10")
    with open(output_file, "w") as f:
        print('#EXTM3U', file=f)
        print('#EXT-X-VERSION:3', file=f)
        print('#EXT-X-STREAM-INF:BANDWIDTH=4569879,AVERAGE-BANDWIDTH=2962350,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.640029,mp4a.40.2"', file=f)
        print(rgc2_string, file=f)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 frrgc.py <output_file_rgc1> <output_file_rgc2>")
        sys.exit(1)
    
    string = fetch_response(f'https://live-event.ftven.fr/out/v1/62d41da4cc404a34a0c30851c674f91c/index_france-domtom.m3u8')
    
    generate_rgc1(string, sys.argv[1])
    generate_rgc2(string, sys.argv[2])
