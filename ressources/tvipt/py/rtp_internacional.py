import requests
import re

# === Config ===
cdn_url = "https://popcdn.day/cdn.php?stream=RTP_INT"
referer = "https://freeshot.live/"
output_file = "ressources/tvipt/py/rtp_internacional.m3u8"

headers = {
    "Referer": referer,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
    "Accept-Encoding": "gzip, deflate"
}

# === Step 1: Fetch the HTML that includes the iframe URL with token ===
response = requests.get(cdn_url, headers=headers)
iframe_match = re.search(r'src="([^"]+?token=[^"]+)"', response.text)

if iframe_match:
    iframe_url = iframe_match.group(1)
    print(f"[✅] Found iframe URL:\n{iframe_url}")

    # === Step 2: Extract the token ===
    token_match = re.search(r'token=([a-f0-9\-]+)', iframe_url)
    if token_match:
        token = token_match.group(1)

        # === Step 3: Build audio and video URLs ===
        audio_url = f"https://fullness.wideiptv.top/RTP_INT/tracks-a1/index.fmp4.m3u8?token={token}"
        video_url = f"https://fullness.wideiptv.top/RTP_INT/tracks-v1/index.fmp4.m3u8?token={token}"

        print(f"\n🎯 Audio URL:\n{audio_url}")
        print(f"\n🎯 Video URL:\n{video_url}")

        # === Step 4: Save M3U8 with full EXT-X structure ===
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            f.write(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="aac",NAME="undefined a1",DEFAULT=YES,URI="{audio_url}"\n')
            f.write('#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=1850000,BANDWIDTH=2320000,AUDIO="aac",RESOLUTION=1024x576,FRAME-RATE=25.000,CODECS="avc1.4d401e,mp4a.40.2",CLOSED-CAPTIONS=NONE\n')
            f.write(video_url + "\n")

        print(f"\n💾 Saved to file: {output_file}")

    else:
        print("[⚠️] Token not found in iframe URL.")
else:
    print("[❌] Could not find iframe with token in the response.")
