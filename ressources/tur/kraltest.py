import requests
import m3u8

url = "https://dygvideo.dygdigital.com/live/hls/kralpop?m3u8"

# headers = {
#     "Connection": "keep-alive",
# }

# response = requests.get(url, headers=headers)
#

response = requests.get(url)

playlist = m3u8.loads(response.text)
print(playlist.segments)
