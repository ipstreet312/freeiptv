#!/usr/bin/python3

import requests
import sys

def fetch_response(url):
    s = requests.Session()
    response = s.get(url)
    return response.text

def generate_frser_m3u8(string, output_file):
    newser_string = string.replace("manifest", "video_7201280_p_0")
    with open(output_file, "w") as f:
        print('#EXTM3U', file=f)
        print('#EXT-X-VERSION:3', file=f)
        print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=3022199,CODECS="avc1.64001F, mp4a.40.2", RESOLUTION=1280x720, SUBTITLES="subs", AUDIO="audio_1000017564_128"', file=f)
        print(newser_string, file=f)
    newser2_string = string.replace("manifest", "A_audio_1000017564_128_fr")
    with open(output_file, "a") as f:
        print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_1000017564_128",LANGUAGE="fr",NAME="fr",DEFAULT=YES,AUTOSELECT=YES,URI="{newser2_string}"', file=f)

def generate_frdoc_m3u8(string, output_file):
    newdoc_string = string.replace("live-series", "live-thema").replace("bde12330-fbf2-44e7-8a7c-c5f31806460c_1000017564_HLS-francedomtom", "docs/735e9260-bb63-11ee-a1a7-0200170265fd_0_HLS-francedomtom").replace("manifest", "video_7201280_p_0")
    
    with open(output_file, "w") as f:
        print('#EXTM3U', file=f)
        print('#EXT-X-VERSION:3', file=f)
        print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=3022199,CODECS="avc1.64001F, mp4a.40.2", RESOLUTION=1280x720, SUBTITLES="subs", AUDIO="audio_1000017564_128"', file=f)
        print(newdoc_string, file=f)
    newdoc2_string = newdoc_string.replace("video_7201280_p_0", "A_audio_1000017564_128_fr")
    with open(output_file, "a") as f:
        print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_1000017564_128",LANGUAGE="fr",NAME="fr",DEFAULT=YES,AUTOSELECT=YES,URI="{newdoc2_string}"', file=f)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 frfastv2.py <output_file_frser> <output_file_frdoc>")
        sys.exit(1)
    
    original_url = "https://live-series.ftven.fr/bde12330-fbf2-44e7-8a7c-c5f31806460c_1000017564_HLS-francedomtom"
    string = fetch_response(f'https://hdfauth.ftven.fr/esi/TA?url={original_url}/manifest.m3u8')
    
    generate_frser_m3u8(string, sys.argv[1])
    generate_frdoc_m3u8(string, sys.argv[2])
