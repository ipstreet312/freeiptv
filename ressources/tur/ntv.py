import requests

base_url = "https://mn-nl.mncdn.com/dogusdyg_ntv/dogusdyg_ntv.smil/"
url = "https://dygvideo.dygdigital.com/live/hls/kralpop?m3u8"

try:
    response = requests.get(url)
    response.raise_for_status()

    playlist_content = response.text.strip()
    print(f"Original playlist content: {playlist_content[:500]}...")

    modified_playlist_content = playlist_content.replace("kralpoptv", "ntv")

    print(f"Modified playlist content: {modified_playlist_content[:500]}...")

    modified_content = ""
    lines = modified_playlist_content.split("\n")

    for line in lines:
        if line.startswith("chunklist"):
            full_url = base_url + line
            modified_content += full_url + "\n"
        else:
            modified_content += line + "\n"

    print(modified_content)

except requests.RequestException as e:
    print(f"An error occurred: {e}")
