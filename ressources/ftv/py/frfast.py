#!/usr/bin/python3

import requests
import sys

def fetch_response(url):
    s = requests.Session()
    response = s.get(url)
    return response.text

def generate_frser_m3u8(original_url):
    string = fetch_response(f'https://hdfauth.ftven.fr/esi/TA?url={original_url}/manifest.m3u8')

    newser_string = string.replace("manifest", "video_7201280_p_0")
    print(newser_string)
    newser2_string = string.replace("manifest", "A_audio_1000017564_128_fr")
    print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_1000017564_128",LANGUAGE="fr",NAME="fr",DEFAULT=YES,AUTOSELECT=YES,URI="{newser2_string}"')

def generate_frdoc_m3u8(original_url, replacement_url):
    string = fetch_response(f'https://hdfauth.ftven.fr/esi/TA?url={original_url}/manifest.m3u8')

    newdoc_string = string.replace(original_url, replacement_url).replace("manifest", "video_7201280_p_0")
    print(newdoc_string)
    newdoc2_string = string.replace(original_url, replacement_url).replace("manifest", "A_audio_1000017564_128_fr")
    print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_1000017564_128",LANGUAGE="fr",NAME="fr",DEFAULT=YES,AUTOSELECT=YES,URI="{newdoc2_string}"')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 frfast.py <output_file>")
        sys.exit(1)
    
    output_file = sys.argv[1]
    original_url = "https://live-series.ftven.fr/bde12330-fbf2-44e7-8a7c-c5f31806460c_1000017564_HLS-francedomtom"
    replacement_url = "https://live-thema.ftven.fr/docs/735e9260-bb63-11ee-a1a7-0200170265fd_0_HLS-francedomtom"
    
    with open(output_file, "w") as f:
        sys.stdout = f
        generate_frser_m3u8(original_url)
        generate_frdoc_m3u8(original_url, replacement_url)
