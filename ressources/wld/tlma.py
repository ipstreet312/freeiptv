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
restream_metadata_url = f"https://player-backend.restream.io/public/videos/{token}"

# Step 4: Fetch metadata JSON and extract videoUrlHls
meta_response = requests.get(restream_metadata_url)
meta_response.raise_for_status()
metadata = meta_response.json()

video_url_hls = metadata.get("videoUrlHls")
if not video_url_hls:
    raise ValueError("videoUrlHls not found in metadata")

# Step 5: Determine base URL
base_url = video_url_hls.rsplit("/", 1)[0] + "/"

# Step 6: Fetch and print the full M3U8 content with absolute paths
m3u8_response = requests.get(video_url_hls)
m3u8_response.raise_for_status()

lines = m3u8_response.text.strip().splitlines()

for line in lines:
    if line.startswith("#") or line.strip() == "":
        print(line)
    else:
        full_url = urljoin(base_url, line)
        print(full_url)
