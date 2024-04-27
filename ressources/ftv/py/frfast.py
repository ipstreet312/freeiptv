#!/usr/bin/python3

import requests
import sys

def fetch_response(url):
    s = requests.Session()
    response = s.get(url)
    return response.text

def generate_frser_m3u8(original_url, output_file):
    string = fetch_response(f'https://hdfauth.ftven.fr/esi/TA?url={original_url}/manifest.m3u8')

    newser_string = string.replace("manifest", "video_7201280_p_0")
    with open(output_file, "w") as f:
        print(newser_string, file=f)
    newser2_string = string.replace("manifest", "A_audio_1000017564_128_fr")
    with open(output_file, "a") as f:
        print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_1000017564_128",LANGUAGE="fr",NAME="fr",DEFAULT=YES,AUTOSELECT=YES,URI="{newser2_string}"', file=f)

def generate_frdoc_m3u8(original_url, replacement_url, output_file):
    string = fetch_response(f'https://hdfauth.ftven.fr/esi/TA?url={original_url}/manifest.m3u8')

    newdoc_string = string.replace(original_url, replacement_url).replace("manifest", "video_7201280_p_0")
    with open(output_file, "w") as f:
        print(newdoc_string, file=f)
    newdoc2_string = string.replace(original_url, replacement_url).replace("manifest", "A_audio_1000017564_128_fr")
    with open(output_file, "a") as f:
        print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_1000017564_128",LANGUAGE="fr",NAME="fr",DEFAULT=YES,AUTOSELECT=YES,URI="{newdoc2_string}"', file=f)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 frfast.py <output_file_frser> <output_file_frdoc>")
        sys.exit(1)
    
    original_url = "https://live-series.ftven.fr/bde12330-fbf2-44e7-8a7c-c5f31806460c_1000017564_HLS-francedomtom"
    replacement_url = "https://live-thema.ftven.fr/docs/735e9260-bb63-11ee-a1a7-0200170265fd_0_HLS-francedomtom"
    
    generate_frser_m3u8(original_url, sys.argv[1])
    generate_frdoc_m3u8(original_url, replacement_url, sys.argv[2])
