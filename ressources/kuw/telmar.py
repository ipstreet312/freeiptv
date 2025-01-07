import requests
import json

url = "https://vimeo.com/live_event/4819137/status"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    # Extract the video ID
    video_id = data["next_live_clip"]["id"]
    # Construct the second URL
    video_url = f"https://player.vimeo.com/video/{video_id}/config"
else:
    print("Failed to fetch data from status URL. HTTP Status Code:", response.status_code)
    exit()

response = requests.get(video_url)
if response.status_code == 200:
    data = response.json()
    fastly_live_url = data["request"]["files"]["hls"]["cdns"]["fastly_live"]["url"]
else:
    print("Failed to fetch data from config URL. HTTP Status Code:", response.status_code)
    exit()

response = requests.get(fastly_live_url, allow_redirects=True)
if response.status_code == 200:
    master_url = response.url  # Get the final redirected URL
else:
    print("Failed to fetch master playlist. HTTP Status Code:", response.status_code)
    exit()

hls_v1 = master_url.replace("hls.", "chunklist_b3256000.")
hls_v2 = master_url.replace("hls.", "chunklist_b728000.")

print('#EXTM3U')
print('#EXT-X-VERSION:6')
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-STREAM-INF:BANDWIDTH=3256000,AVERAGE-BANDWIDTH=2959999,CODECS="avc1.640020,mp4a.40.2",FRAME-RATE=30,RESOLUTION=1280x720')
print(hls_v1)
print('#EXT-X-STREAM-INF:BANDWIDTH=728000,AVERAGE-BANDWIDTH=661817,CODECS="avc1.64001e,mp4a.40.2",FRAME-RATE=30,RESOLUTION=640x360')
print(hls_v2)
