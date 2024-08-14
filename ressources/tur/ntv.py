import requests

url = "https://dygvideo.dygdigital.com/live/hls/kralpop?m3u8"

try:
    response = requests.get(url)
    response.raise_for_status()

    playlist_url = response.text.strip()
    print(f"Original playlist URL: {playlist_url}")

    modified_url = playlist_url.replace("kralpoptv", "ntv")
    print(f"Modified playlist URL: {modified_url}")

    content_response = requests.get(modified_url)
    content_response.raise_for_status()

    content = content_response.text

    print("Content from the modified URL:")
    print(content)

except requests.RequestException as e:
    print(f"An error occurred: {e}")
