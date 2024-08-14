import requests

initial_url = "https://dygvideo.dygdigital.com/live/hls/kralpop?m3u8"

try:
    response = requests.get(initial_url)
    response.raise_for_status()

    final_url = response.url
    print(f"Final URL after redirection: {final_url}")

    modified_url = final_url.replace("kralpoptv", "ntv")
    print(f"Modified URL: {modified_url}")

except requests.RequestException as e:
    print(f"An error occurred: {e}")
