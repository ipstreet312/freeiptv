#!/usr/bin/python3

import requests
import sys

def fetch_response(url):
    s = requests.Session()
    response = s.get(url)
    return response.text

def generate_frser_m3u8(string, output_file):
    newser_string = string.replace("index", "index_20")
    with open(output_file, "w") as f:
        print('#EXTM3U', file=f)
        print('#EXT-X-VERSION:3', file=f)
        print('#EXT-X-STREAM-INF:BANDWIDTH=2961690,AVERAGE-BANDWIDTH=2961690,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.64001F,mp4a.40.2",SUBTITLES="subtitles",AUDIO="audio_0"', file=f)
        print(newser_string, file=f)
    newser2_string = string.replace("index", "index_8_0")
    with open(output_file, "a") as f:
        print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_0",CHANNELS="2",NAME="fr",LANGUAGE="fr",DEFAULT=YES,AUTOSELECT=YES,URI="{newser2_string}"', file=f)

def generate_frdoc_m3u8(string, output_file):
    newdoc_string = string.replace("live-series", "live-thema").replace("index", "index_17")
    
    with open(output_file, "w") as f:
        print('#EXTM3U', file=f)
        print('#EXT-X-VERSION:3', file=f)
        print('#EXT-X-STREAM-INF:BANDWIDTH=2961326,AVERAGE-BANDWIDTH=2961326,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.64001F,mp4a.40.2",SUBTITLES="subtitles",AUDIO="audio_0"', file=f)
        print(newdoc_string, file=f)
    newdoc2_string = newdoc_string.replace("index_17", "index_13_0")
    with open(output_file, "a") as f:
        print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_0",CHANNELS="2",NAME="fr",LANGUAGE="fr",DEFAULT=YES,AUTOSELECT=YES,URI="{newdoc2_string}"', file=f)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 frfastv2.py <output_file_frser> <output_file_frdoc>")
        sys.exit(1)
    
    original_url = "https://live-series.ftven.fr/hls-francedomtom"
    string = fetch_response(f'https://hdfauth.ftven.fr/esi/TA?url={original_url}/index.m3u8')
    
    generate_frser_m3u8(string, sys.argv[1])
    generate_frdoc_m3u8(string, sys.argv[2])
