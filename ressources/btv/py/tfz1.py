import requests
import re

playlist_url = "https://raw.githubusercontent.com/paradise-91/paratv/main/playlists/paratv/main/filter/raw.m3u"

def get_stream_url(playlist_url):
    try:
        response = requests.get(playlist_url)
        response.raise_for_status()
        lines = response.text.splitlines()
        
        for i, line in enumerate(lines):
            if line.strip() == "#EXTINF:-1,TF1 [720p-tf1.fr]":
                stream_line = lines[i + 1].strip()
                #print(f"[+] Found intermediate URL: {stream_line}")

                stream_response = requests.get(stream_line)
                stream_response.raise_for_status()

                match = re.search(r'https://[^\s"\']+', stream_response.text)
                if match:
                    final_url = match.group(0)
                    print(final_url)
                else:
                    print("[-] No HTTPS URL found in stream.")
                return

        print("[-] [720p-tf1.fr] not found in playlist.")
    
    except Exception as e:
        print(f"[!] Error: {e}")

# Run it
get_stream_url(playlist_url)
