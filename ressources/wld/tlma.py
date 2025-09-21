import requests
import re
from urllib.parse import urljoin

# Step 1: Fetch the HTML page from telemaroc.tv
html_url = "https://www.telemaroc.tv/liveTV"
html_response = requests.get(html_url)
html_response.raise_for_status()
html_content = html_response.text

# Step 2: Extract the token from the iframe src
token_match = re.search(r'src="https://player\.restream\.io/\?token=([a-f0-9]+)"', html_content)
if not token_match:
    raise ValueError("Token not found in HTML")
token = token_match.group(1)

# Step 3: Build the restream metadata URL
restream_metadata_url = f"https://player-backend.restream.io/public/videos/{token}?instant=true"

# Step 4: Fetch metadata JSON and extract videoUrlHls
meta_response = requests.get(restream_metadata_url)
meta_response.raise_for_status()
metadata = meta_response.json()

video_url_hls = metadata.get("videoUrlHls")
if not video_url_hls:
    raise ValueError("videoUrlHls not found in metadata")

# Step 5: Download the master playlist and compute base URL
m3u8_response = requests.get(video_url_hls)
m3u8_response.raise_for_status()
lines = m3u8_response.text.strip().splitlines()

# base for resolving relative URIs/paths
base_url = video_url_hls.rsplit("/", 1)[0] + "/"

audio_line = None
video_line = None
video_url = None

# Step 6: Extract audio + 1280x720 stream and make URLs absolute
for i, line in enumerate(lines):
    if line.startswith("#EXT-X-MEDIA") and "TYPE=AUDIO" in line:
        m = re.search(r'URI="([^"]+)"', line)
        if m:
            raw_uri = m.group(1).strip()
            abs_uri = raw_uri if re.match(r'https?://', raw_uri) else urljoin(base_url, raw_uri)
            audio_line = re.sub(r'URI="[^"]+"', f'URI="{abs_uri}"', line)

    if line.startswith("#EXT-X-STREAM-INF") and "RESOLUTION=1280x720" in line:
        video_line = line
        if i + 1 < len(lines):
            raw_video = lines[i + 1].strip()
            video_url = raw_video if re.match(r'https?://', raw_video) else urljoin(base_url, raw_video)

# Step 7: Print minimal playlist in required format
print("#EXTM3U")
print("#EXT-X-VERSION:6")
print("#EXT-X-INDEPENDENT-SEGMENTS")

if audio_line:
    print(audio_line)
else:
    print("# (no audio line found)")

if video_line and video_url:
    print(video_line)
    print(video_url)
else:
    print("# (1280x720 stream not found)")
