import re
import sys
import requests

def get_m3u8_url(broadcast_url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    # Fetch the broadcast page
    r = requests.get(broadcast_url, headers=headers)
    if r.status_code != 200:
        raise Exception(f"Failed to load page: {r.status_code}")

    html = r.text

    # Look for m3u8 in page source
    m3u8_matches = re.findall(r'(https://[^"]+\.m3u8[^"]*)', html)
    if not m3u8_matches:
        raise Exception("No m3u8 URL found in page source. Maybe requires auth or expired.")

    # Return the first match (usually master playlist)
    return m3u8_matches[0]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_m3u8.py <x_broadcast_url>")
        sys.exit(1)

    broadcast_url = sys.argv[1]
    try:
        m3u8_url = get_m3u8_url(broadcast_url)
        print("Found m3u8 URL:\n", m3u8_url)
    except Exception as e:
        print("Error:", e)
