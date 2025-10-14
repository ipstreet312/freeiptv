import requests
import re

# Base URL for building full segment URLs
base_url = "https://ciner-live.ercdn.net/showmax/"

# Page containing the player setup
url = "http://www.showmax.com.tr/canliyayin"

# Optional headers to avoid blocking
headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "http://www.showmax.com.tr/"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    site_content = response.text

    # Look for direct m3u8 URL inside data-hope-video attribute
    match = re.search(r'"src":"(https:[^"]+\.m3u8[^"]*)"', site_content)

    if match:
        m3u8_url = match.group(1).replace("\\/", "/")
        #print(f"[+] Found Live URL: {m3u8_url}")

        # Fetch the m3u8 playlist content
        playlist_response = requests.get(m3u8_url, headers=headers)

        if playlist_response.status_code == 200:
            content = playlist_response.text
            lines = content.split("\n")
            modified_content = ""

            for line in lines:
                # Replace relative TS paths like "showmax/..."
                if line.startswith("showmax"):
                    full_url = base_url + line
                    modified_content += full_url + "\n"
                else:
                    modified_content += line + "\n"

            #print("\n===== MODIFIED PLAYLIST =====\n")
            print(modified_content)
        else:
            print("[x] Error fetching content from the Live URL.")
    else:
        print("[x] Could not detect .m3u8 link in HTML (pattern mismatch).")
else:
    print(f"[x] Error fetching page, HTTP {response.status_code}")
