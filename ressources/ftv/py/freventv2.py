#!/usr/bin/python3

import requests
import sys

def fetch_response(url):
    s = requests.Session()
    response = s.get(url)
    return response.text

def generate_frjo24v2_m3u8(string, output_file):
    frjo24v2_string = string.replace("master", "b0EF_720p/playlist")
    with open(output_file, "w") as f:
        print('#EXTM3U', file=f)
        print('#EXT-X-VERSION:3', file=f)
        print('#EXT-X-STREAM-INF:BANDWIDTH=2855600,AVERAGE-BANDWIDTH=2479236,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.640020,mp4a.40.2"', file=f)
        print(frjo24v2_string, file=f)

"""
def generate_frfescanv2_m3u8(string, output_file):
    fescanv2_string = string.replace("live-olympics", "live-event").replace("paris2024-francedomtom", "out/v1/65fb695a25404e08944943d011abca75").replace("master", "index_france-domtom_26")
    with open(output_file, "w") as f:
        print('#EXTM3U', file=f)
        print('#EXT-X-VERSION:3', file=f)
        print('#EXT-X-STREAM-INF:BANDWIDTH=4569457,AVERAGE-BANDWIDTH=2961824,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.64001F,mp4a.40.2"', file=f)
        print(fescanv2_string, file=f)
"""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 freventv2.py <output_file_frjo24v2>")
        sys.exit(1)
    
    string = fetch_response(f'https://hdfauth.ftven.fr/esi/TA?url=https%3A%2F%2Flive-olympics.ftven.fr%2Fparis2024-francedomtom%2Fmaster.m3u8')
    
    generate_frjo24v2_m3u8(string, sys.argv[1])
