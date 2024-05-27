#!/usr/bin/python3

import requests
import sys

def fetch_response(url):
    s = requests.Session()
    response = s.get(url)
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

def generate_rgc3(string, output_file):
    rgc3_string = string.replace("62d41da4cc404a34a0c30851c674f91c", "c0b0dea11d044ec0b649f043728b7650").replace("index_france-domtom", "index_france-domtom_10")
    with open(output_file, "w") as f:
        print('#EXTM3U', file=f)
        print('#EXT-X-VERSION:3', file=f)
        print('#EXT-X-STREAM-INF:BANDWIDTH=4569879,AVERAGE-BANDWIDTH=2962350,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.640029,mp4a.40.2"', file=f)
        print(rgc3_string, file=f)
      
def generate_rgc4(string, output_file):
    rgc4_string = string.replace("62d41da4cc404a34a0c30851c674f91c", "643489f068e04642ad8e3e19ca513a3d").replace("index_france-domtom", "index_france-domtom_10")
    with open(output_file, "w") as f:
        print('#EXTM3U', file=f)
        print('#EXT-X-VERSION:3', file=f)
        print('#EXT-X-STREAM-INF:BANDWIDTH=4569879,AVERAGE-BANDWIDTH=2962350,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.640029,mp4a.40.2"', file=f)
        print(rgc4_string, file=f)

def generate_rgc5(string, output_file):
    rgc5_string = string.replace("62d41da4cc404a34a0c30851c674f91c", "05f36ac80abe4ddcb02b249efc68f899").replace("index_france-domtom", "index_france-domtom_10")
    with open(output_file, "w") as f:
        print('#EXTM3U', file=f)
        print('#EXT-X-VERSION:3', file=f)
        print('#EXT-X-STREAM-INF:BANDWIDTH=4569879,AVERAGE-BANDWIDTH=2962350,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.640029,mp4a.40.2"', file=f)
        print(rgc5_string, file=f)

def generate_rgc6(string, output_file):
    rgc6_string = string.replace("62d41da4cc404a34a0c30851c674f91c", "1422d06a8b5045f18c6cf48e4ea2f486").replace("index_france-domtom", "index_france-domtom_10")
    with open(output_file, "w") as f:
        print('#EXTM3U', file=f)
        print('#EXT-X-VERSION:3', file=f)
        print('#EXT-X-STREAM-INF:BANDWIDTH=4569879,AVERAGE-BANDWIDTH=2962350,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.640029,mp4a.40.2"', file=f)
        print(rgc6_string, file=f)

def generate_rgc7(string, output_file):
    rgc7_string = string.replace("62d41da4cc404a34a0c30851c674f91c", "9bceaba8e68a4531b99aee079ad79205").replace("index_france-domtom", "index_france-domtom_10")
    with open(output_file, "w") as f:
        print('#EXTM3U', file=f)
        print('#EXT-X-VERSION:3', file=f)
        print('#EXT-X-STREAM-INF:BANDWIDTH=4569879,AVERAGE-BANDWIDTH=2962350,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.640029,mp4a.40.2"', file=f)
        print(rgc7_string, file=f)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 frrgc.py <output_file_rgc1> <output_file_rgc2> <output_file_rgc3> <output_file_rgc4> <output_file_rgc5> <output_file_rgc6> <output_file_rgc7>")
        sys.exit(1)
    
    string = fetch_response(f'https://live-event.ftven.fr/out/v1/62d41da4cc404a34a0c30851c674f91c/index_france-domtom.m3u8')
    
    generate_rgc1(string, sys.argv[1])
    generate_rgc2(string, sys.argv[2])
    generate_rgc3(string, sys.argv[3])
    generate_rgc4(string, sys.argv[4])
    generate_rgc5(string, sys.argv[5])
    generate_rgc6(string, sys.argv[6])
    generate_rgc7(string, sys.argv[7])
