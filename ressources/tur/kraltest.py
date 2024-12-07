import requests

url = "https://dygvideo.dygdigital.com/live/hls/kralpop?m3u8"

headers = {
    "Connection": "keep-alive",
}

response = requests.get(url, headers=headers)

print(response.text)
